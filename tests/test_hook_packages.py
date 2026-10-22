import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]


class PackagedHookTest(unittest.TestCase):
    def test_native_adapter_commands_load_once_and_restore_after_compaction(self):
        cases = [
            ("cpp-dev", "Fix the C++ parser crash", {"clean-code", "cpp-guidelines"}),
            ("java-dev", "Fix the Java parser crash", {"clean-code"}),
            ("cpp-dev", "Create a C++ header order.hpp", {"clean-code", "cpp-guidelines", "clean-architecture"}),
            ("cpp-dev", "Review the C++ architecture", {"clean-code", "cpp-guidelines", "clean-architecture"}),
            ("dev-workflow", "Implement the parser feature", {"canon-tdd", "test-strategy"}),
            ("doc-tools", "Write a guide with a sequence diagram", {"text-writing", "uml-diagrams"}),
        ]
        for host in ("codex", "claude"):
            for plugin, prompt, expected in cases:
                with self.subTest(host=host, plugin=plugin), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    package = root / "package with spaces" / plugin
                    source = REPO / "plugins" / plugin
                    shutil.copytree(source / "hooks", package / "hooks")
                    # References are deliberately absent: hook loading must stay at main bodies.
                    for main in (source / "skills").glob("*/SKILL.md"):
                        target = package / "skills" / main.parent.name / "SKILL.md"
                        target.parent.mkdir(parents=True)
                        shutil.copy2(main, target)
                    filename = "codex.json" if host == "codex" else "hooks.json"
                    config = json.loads((package / "hooks" / filename).read_text())
                    env = dict(os.environ)
                    for key in ("PLUGIN_DATA", "CLAUDE_PLUGIN_DATA", "VIBE_CONTEXT_PLUGIN_ROOT"):
                        env.pop(key, None)
                    prefix = "PLUGIN" if host == "codex" else "CLAUDE_PLUGIN"
                    env[prefix + "_ROOT"] = str(package)
                    env[prefix + "_DATA"] = str(root / "data")
                    payload = {"session_id": "adapter-session", "cwd": str(root), "hook_event_name": "UserPromptSubmit", "prompt": prompt}

                    def run(event):
                        handler = config["hooks"][event["hook_event_name"]][0]["hooks"][0]
                        result = subprocess.run(["sh", "-c", handler["command"]], input=json.dumps(event), env=env, cwd=root, text=True, capture_output=True)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertEqual(result.stderr, "")
                        return json.loads(result.stdout) if result.stdout.strip() else {}

                    loaded = run(payload)
                    context = loaded["hookSpecificOutput"]["additionalContext"]
                    names = set(re.findall(r"^Skill: " + plugin + r":([^\n]+)", context, re.M))
                    self.assertEqual(names, expected)
                    self.assertLess(len(context), 10000, "Claude would spill the body to a preview file")
                    self.assertEqual(run(payload), {})
                    restored = run(dict(payload, hook_event_name="SessionStart", source="compact"))
                    self.assertEqual(restored["hookSpecificOutput"]["additionalContext"], context)
                    self.assertEqual(run(payload), {})

    def test_codex_precompact_does_not_set_context_output_limit(self):
        for name in ("cpp-dev", "java-dev", "dev-workflow", "doc-tools"):
            config = json.loads((REPO / "plugins" / name / "hooks/codex.json").read_text())
            self.assertNotIn("additionalContextLimit", config["hooks"]["PreCompact"][0]["hooks"][0])

    def test_generated_bundles_match_canonical_source(self):
        result = subprocess.run(["python3", str(REPO / "tools/skill-context/sync.py"), "--check"], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
