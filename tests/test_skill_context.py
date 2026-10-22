import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
LOADER = REPO / "tools/skill-context/loader.py"

class SkillContextTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.plugin = self.root / "cpp-dev"
        (self.plugin / "hooks").mkdir(parents=True)
        (self.plugin / "skills/clean-code").mkdir(parents=True)
        self.skill = self.plugin / "skills/clean-code/SKILL.md"
        self.skill.write_text("---\nname: clean-code\ndescription: demo\n---\n# Unique C++ guidance\nKeep behavior.\n")
        (self.plugin / "hooks/routes.json").write_text(json.dumps({"plugin": "cpp-dev", "skills": {"clean-code": ["cpp"]}}))
        self.project = self.root / "project"
        self.project.mkdir()
        (self.project / "example.cpp").write_text("int main() {}\n")
        self.env = dict(os.environ, VIBE_CONTEXT_PLUGIN_ROOT=str(self.plugin), PLUGIN_DATA=str(self.root / "data"))
        self.base = {"session_id": "session-1", "cwd": str(self.project), "hook_event_name": "PreToolUse", "tool_name": "Read", "tool_input": {"file_path": str(self.project / "example.cpp")}}

    def hook(self, skill="clean-code", **changes):
        event = dict(self.base, **changes)
        result = subprocess.run([sys.executable, str(LOADER), skill], input=json.dumps(event), text=True, capture_output=True, env=self.env)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"] if result.stdout.strip() else ""

    def add_skill(self, name, selectors):
        folder = self.plugin / "skills" / name
        folder.mkdir(exist_ok=True)
        (folder / "SKILL.md").write_text("---\nname: " + name + "\ndescription: demo\n---\n# Guidance " + name + "\n")
        config = self.plugin / "hooks/routes.json"
        routes = json.loads(config.read_text())
        routes["skills"][name] = selectors
        config.write_text(json.dumps(routes))

    def test_repeated_cpp_edits_load_body_only_once(self):
        first = self.hook()
        self.assertIn("# Unique C++ guidance", first)
        self.assertNotIn("description: demo", first)
        self.assertEqual(self.hook(tool_name="Edit"), "")
        self.assertEqual(self.hook(tool_name="Write"), "")

    def test_compaction_restores_body_then_repeated_edit_is_quiet(self):
        self.hook()
        restored = self.hook(hook_event_name="SessionStart", source="compact", tool_input={})
        self.assertIn("# Unique C++ guidance", restored)
        self.assertEqual(self.hook(), "")

    def test_cpp_prompt_loads_before_the_first_edit(self):
        context = self.hook(hook_event_name="UserPromptSubmit", prompt="Fix the C++ parser crash", tool_input={})
        self.assertIn("# Unique C++ guidance", context)
        self.assertEqual(self.hook(), "")

    def test_fixing_readme_does_not_start_tdd(self):
        self.add_skill("canon-tdd", ["behavior"])
        self.assertEqual(self.hook(skill="canon-tdd", hook_event_name="UserPromptSubmit", prompt="Fix the README instructions", tool_input={}), "")

    def test_test_strategy_planning_is_independent_from_tdd(self):
        self.add_skill("test-strategy", ["verification"])
        self.add_skill("canon-tdd", ["behavior"])
        prompt = {"hook_event_name": "UserPromptSubmit", "prompt": "Choose integration tests for the database migration", "tool_input": {}}
        self.assertIn("# Guidance test-strategy", self.hook(skill="test-strategy", **prompt))
        self.assertEqual(self.hook(skill="canon-tdd", **prompt), "")
        self.assertEqual(self.hook(skill="test-strategy", **prompt), "")

    def test_java_sources_do_not_load_cpp_guidance(self):
        self.add_skill("java-code", ["java"])
        path = self.project / "Example.java"
        path.write_text("class Example {}")
        args = {"tool_input": {"file_path": str(path)}}
        self.assertEqual(self.hook(**args), "")
        self.assertIn("# Guidance java-code", self.hook(skill="java-code", **args))

    def test_plain_c_header_is_not_assumed_to_be_cpp(self):
        path = self.project / "c_api.h"
        path.write_text("int value(void);")
        self.assertEqual(self.hook(tool_input={"file_path": str(path)}), "")

    def test_header_with_neighboring_cpp_source_loads_cpp(self):
        path = self.project / "model.h"
        path.write_text("struct Model;")
        path.with_suffix(".cpp").write_text("// implementation")
        self.assertIn("# Unique C++ guidance", self.hook(tool_input={"file_path": str(path)}))

    def test_cmake_cxx_context_identifies_header(self):
        (self.project / "CMakeLists.txt").write_text("project(example LANGUAGES CXX)")
        path = self.project / "other.h"
        path.write_text("struct Other;")
        self.assertIn("# Unique C++ guidance", self.hook(tool_input={"file_path": str(path)}))

    def test_apply_patch_target_routes_before_tool_execution(self):
        patch = "*** Begin Patch\n*** Add File: src/new file.cpp\n+int value = 1;\n*** End Patch"
        self.assertIn("# Unique C++ guidance", self.hook(tool_name="apply_patch", tool_input={"command": patch}))

    def test_simple_shell_read_routes_source_without_running_shell(self):
        self.assertIn("# Unique C++ guidance", self.hook(tool_name="Bash", tool_input={"command": "sed -n '1,20p' example.cpp"}))

    def test_generated_and_vendor_files_are_ignored(self):
        path = self.project / "vendor" / "widget.cpp"
        path.parent.mkdir()
        path.write_text("int x;")
        self.assertEqual(self.hook(tool_input={"file_path": str(path)}), "")
        self.assertEqual(self.hook(tool_name="Write", tool_input={"file_path": "message.pb.h"}), "")

    def test_document_edit_loads_writing_but_instruction_file_does_not(self):
        self.add_skill("text-writing", ["prose"])
        self.assertEqual(self.hook(skill="text-writing", tool_name="Write", tool_input={"file_path": "SKILL.md"}), "")
        result = self.hook(skill="text-writing", tool_name="Write", tool_input={"file_path": "README.md"})
        self.assertIn("# Guidance text-writing", result)
        self.assertEqual(self.hook(skill="text-writing", tool_name="Edit", tool_input={"file_path": "docs/guide.md"}), "")

    def test_diagram_tex_loads_diagram_guidance_only(self):
        self.add_skill("uml-diagrams", ["diagram"])
        self.add_skill("text-writing", ["prose"])
        payload = {"tool_name": "Write", "tool_input": {"file_path": "diagram.tex", "content": r"\begin{tikzpicture}\end{tikzpicture}"}}
        self.assertIn("# Guidance uml-diagrams", self.hook(skill="uml-diagrams", **payload))
        self.assertEqual(self.hook(skill="text-writing", **payload), "")

    def test_cpp_header_write_loads_architecture_once(self):
        self.add_skill("clean-architecture", ["cpp-header", "cpp-architecture"])
        args = {"tool_name": "Write", "tool_input": {"file_path": "include/order.hpp", "content": "struct Order {};"}}
        self.assertIn("# Guidance clean-architecture", self.hook(skill="clean-architecture", **args))
        self.assertEqual(self.hook(skill="clean-architecture", **args), "")

    def test_cpp_architecture_guidance_is_language_scoped(self):
        self.add_skill("clean-architecture", ["cpp-header", "cpp-architecture"])
        self.assertEqual(self.hook(skill="clean-architecture"), "")
        args = {"hook_event_name": "UserPromptSubmit", "tool_input": {}}
        self.assertEqual(self.hook(skill="clean-architecture", prompt="Review the Java architecture", **args), "")
        self.assertIn("# Guidance clean-architecture", self.hook(skill="clean-architecture", prompt="Review C++ dependency direction", **args))

    def test_architecture_intent_waits_for_cpp_evidence(self):
        self.add_skill("clean-architecture", ["cpp-header", "cpp-architecture"])
        self.assertEqual(self.hook(skill="clean-architecture", hook_event_name="UserPromptSubmit", prompt="Review dependency direction", tool_input={}), "")
        self.assertIn("# Guidance clean-architecture", self.hook(skill="clean-architecture"))

    def test_cpp_header_prompt_loads_before_the_edit(self):
        self.add_skill("clean-architecture", ["cpp-header", "cpp-architecture"])
        self.assertIn("# Guidance clean-architecture", self.hook(skill="clean-architecture", hook_event_name="UserPromptSubmit", prompt="Create order.hpp", tool_input={}))

    def test_header_architecture_restores_after_source_reads_and_compaction(self):
        self.add_skill("clean-architecture", ["cpp-header", "cpp-architecture"])
        self.assertIn("# Guidance clean-architecture", self.hook(skill="clean-architecture", tool_name="Read", tool_input={"file_path": "order.hpp"}))
        self.assertEqual(self.hook(skill="clean-architecture"), "")
        self.assertIn("# Guidance clean-architecture", self.hook(skill="clean-architecture", hook_event_name="SessionStart", source="compact", tool_input={}))
        self.assertEqual(self.hook(skill="clean-architecture", tool_name="Edit", tool_input={"file_path": "order.hpp"}), "")

    def test_c_and_generated_headers_do_not_load_cpp_architecture(self):
        self.add_skill("clean-architecture", ["cpp-header", "cpp-architecture"])
        for path in ["c_api.h", "vendor/widget.hpp", "message.pb.hpp"]:
            with self.subTest(path=path):
                self.assertEqual(self.hook(skill="clean-architecture", tool_name="Write", tool_input={"file_path": path}), "")

    def test_dot_h_architecture_uses_cpp_context(self):
        self.add_skill("clean-architecture", ["cpp-header", "cpp-architecture"])
        self.hook(skill="clean-architecture", hook_event_name="UserPromptSubmit", prompt="Fix the C++ parser", tool_input={})
        args = {"tool_name": "Edit", "tool_input": {"file_path": "parser.h"}}
        self.assertIn("# Guidance clean-architecture", self.hook(skill="clean-architecture", **args))
        self.assertEqual(self.hook(skill="clean-architecture", **args), "")

    def test_patch_creation_loads_header_architecture(self):
        self.add_skill("clean-architecture", ["cpp-header", "cpp-architecture"])
        patch = "*** Begin Patch\n*** Add File: include/new.hpp\n+struct New {};\n*** End Patch"
        self.assertIn("# Guidance clean-architecture", self.hook(skill="clean-architecture", tool_name="apply_patch", tool_input={"command": patch}))

    def test_formatting_does_not_activate_behavior_workflow(self):
        self.add_skill("canon-tdd", ["behavior"])
        self.hook(skill="canon-tdd", hook_event_name="UserPromptSubmit", prompt="Format the C++ sources", tool_input={})
        self.assertEqual(self.hook(skill="canon-tdd", tool_name="Edit"), "")

    def test_refactor_uses_verification_without_manufacturing_tdd_red(self):
        self.add_skill("canon-tdd", ["behavior"])
        self.add_skill("test-strategy", ["verification"])
        args = {"hook_event_name": "UserPromptSubmit", "prompt": "Refactor the parser while preserving behavior", "tool_input": {}}
        self.assertEqual(self.hook(skill="canon-tdd", **args), "")
        self.assertIn("# Guidance test-strategy", self.hook(skill="test-strategy", **args))

    def test_conversations_and_agents_do_not_share_emitted_state(self):
        self.hook()
        self.assertIn("# Unique C++ guidance", self.hook(session_id="session-2"))
        self.assertIn("# Unique C++ guidance", self.hook(agent_id="child-1"))
        self.assertEqual(self.hook(agent_id="child-1"), "")

    def test_skill_content_change_reloads_only_that_body(self):
        self.hook()
        self.skill.write_text(self.skill.read_text() + "Updated requirement.\n")
        self.assertIn("Updated requirement.", self.hook())
        self.assertEqual(self.hook(), "")

    def test_supporting_references_are_not_injected(self):
        folder = self.skill.parent / "references"
        folder.mkdir()
        (folder / "details.md").write_text("Reference should stay on demand")
        self.assertNotIn("Reference should stay on demand", self.hook())

    def test_resume_restores_active_guidance(self):
        self.hook()
        self.assertIn("# Unique C++ guidance", self.hook(hook_event_name="SessionStart", source="resume", tool_input={}))
        self.assertEqual(self.hook(), "")

    def test_compaction_does_not_restore_an_inactive_language(self):
        self.hook()
        self.hook(hook_event_name="UserPromptSubmit", prompt="Write the README documentation", tool_input={})
        self.assertEqual(self.hook(hook_event_name="SessionStart", source="compact", tool_input={}), "")

    def test_precompact_invalidation_works_when_sessionstart_is_unavailable(self):
        self.hook()
        self.assertEqual(self.hook(hook_event_name="PreCompact", tool_input={}), "")
        self.assertIn("# Unique C++ guidance", self.hook())
        self.assertEqual(self.hook(), "")

    def test_missing_identity_does_not_suppress_other_conversations(self):
        self.assertEqual(self.hook(session_id=""), "")
        self.assertIn("# Unique C++ guidance", self.hook())

    def test_claude_plugin_data_environment_is_supported(self):
        self.env.pop("PLUGIN_DATA")
        self.env["CLAUDE_PLUGIN_DATA"] = str(self.root / "claude-data")
        self.assertIn("# Unique C++ guidance", self.hook())
        self.assertEqual(self.hook(), "")

    def test_parallel_reads_emit_guidance_once(self):
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=8) as pool:
            contexts = list(pool.map(lambda _: self.hook(), range(8)))
        self.assertEqual(sum("# Unique C++ guidance" in value for value in contexts), 1)

    def test_explicit_no_tdd_is_respected_on_following_edits(self):
        self.add_skill("canon-tdd", ["behavior"])
        args = {"hook_event_name": "UserPromptSubmit", "prompt": "Fix the C++ parser without TDD", "tool_input": {}}
        self.assertEqual(self.hook(skill="canon-tdd", **args), "")
        self.assertEqual(self.hook(skill="canon-tdd", tool_name="Edit"), "")

    def test_mixed_implementation_and_docs_load_workflow(self):
        self.add_skill("canon-tdd", ["behavior"])
        self.assertIn("# Guidance canon-tdd", self.hook(skill="canon-tdd", hook_event_name="UserPromptSubmit", prompt="Implement a C++ parser and update the README", tool_input={}))

    def test_cmake_comment_does_not_turn_c_header_into_cpp(self):
        (self.project / "CMakeLists.txt").write_text("# Example: LANGUAGES CXX\nproject(actual LANGUAGES C)")
        path = self.project / "c_header.h"
        path.write_text("int c_function(void);")
        self.assertEqual(self.hook(tool_input={"file_path": str(path)}), "")

    def test_hook_input_is_not_executed_as_a_shell_command(self):
        marker = self.root / "must-not-exist"
        self.assertEqual(self.hook(tool_name="Bash", tool_input={"command": "touch " + str(marker)}), "")
        self.assertFalse(marker.exists())

    def test_cache_failure_does_not_block_the_tool(self):
        path = self.root / "not-a-directory"
        path.write_text("existing data")
        self.env["PLUGIN_DATA"] = str(path)
        self.assertEqual(self.hook(), "")
        self.assertEqual(path.read_text(), "existing data")

    def test_corrupted_cache_recovers_with_one_fresh_injection(self):
        self.hook()
        path = next((self.root / "data/skill-context").glob("*.json"))
        path.write_text("{broken")
        self.assertIn("# Unique C++ guidance", self.hook())
        self.assertEqual(self.hook(), "")

    def test_clear_starts_a_fresh_loading_context(self):
        self.hook()
        self.assertEqual(self.hook(hook_event_name="SessionStart", source="clear", tool_input={}), "")
        self.assertIn("# Unique C++ guidance", self.hook())

    def test_transcript_rotation_does_not_lose_compaction_state(self):
        self.hook(transcript_path="before-compaction.jsonl")
        restored = self.hook(hook_event_name="SessionStart", source="compact", transcript_path="after-compaction.jsonl", tool_input={})
        self.assertIn("# Unique C++ guidance", restored)
        self.assertEqual(self.hook(transcript_path=None), "")

    def test_partial_tex_edit_keeps_existing_diagram_classification(self):
        self.add_skill("uml-diagrams", ["diagram"])
        self.add_skill("text-writing", ["prose"])
        path = self.project / "diagram.tex"
        path.write_text(r"\begin{tikzpicture}\node{first};\end{tikzpicture}")
        payload = {"tool_name": "Edit", "tool_input": {"file_path": str(path), "old_string": "first", "new_string": "second"}}
        self.assertIn("# Guidance uml-diagrams", self.hook(skill="uml-diagrams", **payload))
        self.assertEqual(self.hook(skill="text-writing", **payload), "")

if __name__ == "__main__":
    unittest.main()
