import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]

class CodexRegistrationTest(unittest.TestCase):
    def test_registers_concrete_plugin_commands_and_preserves_other_hooks(self):
        spec = importlib.util.spec_from_file_location("registration", REPO / "tools/skill-context/install_codex_hooks.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        existing = {"description": "My hooks", "hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [{"type": "command", "command": "my-existing-hook"}]}]}}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "plugin with spaces"
            root.mkdir()
            hooks = root / "hooks"
            hooks.mkdir()
            (hooks / "codex.json").write_bytes((REPO / "plugins/dev-workflow/hooks/codex.json").read_bytes())
            (hooks / "skill_context.py").write_text("# fixture")
            retired = {"type": "command", "command": "old-architecture-loader", "statusMessage": "vibe-coding context (dev-architecture)"}
            migrating = json.loads(json.dumps(existing))
            migrating["hooks"]["PreToolUse"].append({"hooks": [retired]})
            result = module.registered_hooks(migrating, {"dev-workflow": root}, Path(temp) / "data")
            self.assertEqual(result["description"], "My hooks")
            self.assertEqual(result["hooks"]["PreToolUse"][0], existing["hooks"]["PreToolUse"][0])
            self.assertEqual(len(result["hooks"]["PreToolUse"]), 2)
            command = result["hooks"]["PreToolUse"][1]["hooks"][0]["command"]
            self.assertIn("plugin with spaces", command)
            self.assertNotIn("${PLUGIN_ROOT}", command)
            self.assertIn("PLUGIN_DATA=", command)
            self.assertEqual(module.registered_hooks(result, {"dev-workflow": root}, Path(temp) / "data"), result)
            self.assertEqual(existing["hooks"].keys(), {"PreToolUse"})
            native = module.registered_hooks(result, {"dev-workflow": root}, Path(temp) / "data", native_names={"dev-workflow"})
            self.assertEqual(native, existing)

if __name__ == "__main__":
    unittest.main()
