"""Register reviewed plugin hooks when the installed Codex cannot discover them."""
import argparse
import copy
import json
import os
from pathlib import Path
import queue
import shlex
import shutil
import subprocess
import tempfile
import threading
import time

NAMES = ('cpp-dev', 'java-dev', 'dev-workflow', 'doc-tools')
RETIRED_NAMES = ('dev-architecture',)


def registered_hooks(existing, profiles, data_root, native_names=()):
    result = copy.deepcopy(existing)
    events = result.setdefault('hooks', {})
    if not isinstance(events, dict):
        raise ValueError('existing hooks must be an object')
    markers = {f'vibe-coding context ({name})' for name in NAMES + RETIRED_NAMES}
    for event, groups in list(events.items()):
        kept = []
        for group in groups:
            handlers = [h for h in group['hooks'] if h.get('statusMessage') not in markers]
            if handlers:
                kept.append(dict(group, hooks=handlers))
        if kept or not groups:
            events[event] = kept
        else:
            events.pop(event)
    for name, root in profiles.items():
        if name in native_names:
            continue
        config = json.loads((root / 'hooks/codex.json').read_text(encoding='utf-8'))
        for event, groups in config['hooks'].items():
            for original in groups:
                group = copy.deepcopy(original)
                for handler in group['hooks']:
                    handler['command'] = (f'PLUGIN_DATA={shlex.quote(str(data_root / name))} '
                                          f'python3 {shlex.quote(str(root / "hooks/skill_context.py"))}')
                    handler['statusMessage'] = f'vibe-coding context ({name})'
                    if event == 'PreCompact':
                        handler.pop('additionalContextLimit', None)
                events.setdefault(event, []).append(group)
    return result


def native_plugin_names(cwd):
    """Ask the installed harness, without starting a model turn or altering trust."""
    proc = subprocess.Popen(['codex', 'app-server'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL, text=True, bufsize=1)
    messages = queue.Queue()
    def read():
        for line in proc.stdout:
            try:
                messages.put(json.loads(line))
            except ValueError:
                continue
    threading.Thread(target=read, daemon=True).start()
    def send(message):
        proc.stdin.write(json.dumps(message) + '\n')
        proc.stdin.flush()
    def receive(ident):
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            try:
                result = messages.get(timeout=1)
            except queue.Empty:
                continue
            if result.get('id') == ident:
                if 'error' in result:
                    raise RuntimeError(result['error']['message'])
                return result['result']
        raise TimeoutError('Codex hook discovery timed out')
    try:
        send({'id':1,'method':'initialize','params':{'clientInfo':{'name':'vibe-hook-setup','version':'1.0.0'},'capabilities':{'experimentalApi':True,'requestAttestation':False,'explicitGatewayOauth':True}}})
        receive(1)
        send({'method':'initialized'})
        send({'id':2,'method':'hooks/list','params':{'cwds':[str(cwd)]}})
        listing = receive(2)
        events = {}
        for entry in listing['data']:
            if entry.get('errors'):
                raise RuntimeError('Resolve hook discovery errors before registration')
            for hook in entry['hooks']:
                plugin = hook.get('pluginId') or ''
                if plugin.endswith('@vibe-coding'):
                    events.setdefault(plugin.split('@')[0], set()).add(hook['eventName'][0].lower() + hook['eventName'][1:])
        required = {'userPromptSubmit','preToolUse','preCompact','sessionStart'}
        return {name for name, found in events.items() if required <= found}
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
        proc.stdin.close()
        proc.stdout.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='write compatibility registrations; default is a preview')
    args = parser.parse_args()
    if os.name == 'nt':
        raise SystemExit('This compatibility installer currently targets POSIX shells; native plugin hooks remain portable.')
    home = Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')).expanduser().resolve()
    listing = json.loads(subprocess.check_output(['codex','plugin','list','--marketplace','vibe-coding','--json'], text=True))
    profiles = {}
    for plugin in listing['installed']:
        name = plugin['name']
        if name in NAMES and plugin['enabled']:
            root = home / 'plugins/cache/vibe-coding' / name / plugin['version']
            if not (root / 'hooks/skill_context.py').is_file():
                raise FileNotFoundError(f'Update {name} before registering hooks')
            profiles[name] = root
    native = native_plugin_names(Path.cwd())
    target = home / 'hooks.json'
    existing = json.loads(target.read_text(encoding='utf-8')) if target.exists() else {}
    desired = registered_hooks(existing, profiles, home / 'vibe-coding-context-data', native)
    changed = desired != existing
    if args.apply and changed:
        if target.exists():
            shutil.copy2(target, target.with_name('hooks.json.vibe-backup-' + str(time.time_ns())))
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=home, delete=False) as out:
            temporary = Path(out.name)
            json.dump(desired, out, indent=2)
            out.write('\n')
        try:
            os.replace(temporary, target)
        finally:
            temporary.unlink(missing_ok=True)
    print(json.dumps({'changed': changed, 'applied': bool(args.apply), 'native_plugins': sorted(native),
                      'compatibility_plugins': sorted(set(profiles) - native), 'config': str(target)}))


if __name__ == '__main__':
    main()
