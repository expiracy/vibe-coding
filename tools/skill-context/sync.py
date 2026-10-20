"""Bundle the shared context loader into each independently installable plugin."""
import argparse
import json
from pathlib import Path

PROFILES = {
    'cpp-dev': {'clean-code': ['cpp'], 'cpp-guidelines': ['cpp']},
    'java-dev': {'clean-code': ['java']},
    'dev-architecture': {'clean-architecture': ['architecture']},
    'dev-workflow': {'canon-tdd': ['behavior'], 'test-strategy': ['verification']},
    'doc-tools': {'text-writing': ['prose'], 'uml-diagrams': ['diagram']},
}


def configuration(host):
    variable = 'PLUGIN_ROOT' if host == 'codex' else 'CLAUDE_PLUGIN_ROOT'
    handler = {'type': 'command', 'command': 'python3 "${' + variable + '}/hooks/skill_context.py"', 'timeout': 5}
    if host == 'codex':
        handler.update({'additionalContextLimit': 4096, 'statusMessage': 'Loading relevant skill context'})
    return {'hooks': {
        'UserPromptSubmit': [{'hooks': [handler]}],
        'PreToolUse': [{'matcher': '^(Read|Edit|Write|MultiEdit|Bash|apply_patch|exec_command|shell_command|read_file|write_file|edit_file|mcp__.*)$', 'hooks': [handler]}],
        'PreCompact': [{'hooks': [handler]}],
        'SessionStart': [{'matcher': '^(startup|resume|clear|compact|fork)$', 'hooks': [handler]}],
    }}


def sync(repo, check=False):
    source = Path(__file__).with_name('loader.py').read_bytes()
    different = []
    for name, skills in PROFILES.items():
        root = repo / 'plugins' / name / 'hooks'
        files = {
            'skill_context.py': source,
            'routes.json': (json.dumps({'plugin': name, 'skills': skills}, indent=2) + '\n').encode(),
            'hooks.json': (json.dumps(configuration('claude'), indent=2) + '\n').encode(),
            'codex.json': (json.dumps(configuration('codex'), indent=2) + '\n').encode(),
        }
        for filename, data in files.items():
            target = root / filename
            if not target.is_file() or target.read_bytes() != data:
                different.append(str(target.relative_to(repo)))
                if not check:
                    root.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
    if check and different:
        raise SystemExit('Out-of-date hook bundles: ' + ', '.join(different))
    return different


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    changed = sync(Path(__file__).resolve().parents[2], args.check)
    print('Hook bundles match source.' if args.check else f'Updated {len(changed)} bundled files.')
