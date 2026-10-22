"""Select bundled skill context for lifecycle hooks, using only Python's stdlib."""
from contextlib import contextmanager
import hashlib
import json
import os
import re
import shlex
from pathlib import Path
import sys
import tempfile
import time


@contextmanager
def state_lock(path):
    lock = path.with_suffix('.lock')
    deadline = time.monotonic() + 1
    while True:
        try:
            lock.mkdir()
            break
        except FileExistsError:
            try:
                if time.time() - lock.stat().st_mtime > 30:
                    lock.rmdir()
                    continue
            except FileNotFoundError:
                continue
            if time.monotonic() >= deadline:
                raise OSError('context cache is busy')
            time.sleep(0.01)
    try:
        yield
    finally:
        lock.rmdir()


def read_state(path):
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
        return value if isinstance(value, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_state(path, value):
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False) as out:
        temporary = Path(out.name)
        json.dump(value, out)
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


CPP_SUFFIXES = {'.cpp', '.cc', '.cxx', '.c++', '.hpp', '.hh', '.hxx', '.h++', '.ipp', '.inl', '.tpp'}
CPP_HEADER_SUFFIXES = {'.h', '.hpp', '.hh', '.hxx', '.h++', '.ipp', '.inl', '.tpp'}
CODE_SUFFIXES = CPP_SUFFIXES | {'.h', '.c', '.java', '.py', '.js', '.jsx', '.ts', '.tsx', '.rs', '.go', '.cs', '.swift', '.rb', '.sh'}
DOC_SUFFIXES = {'.md', '.mdx', '.rst', '.adoc'}
IGNORED_PARTS = {'vendor', 'third_party', 'third-party', 'node_modules', '.git', 'build', 'dist', '_build', 'target', 'generated', '.venv', 'fixtures', 'testdata', '__snapshots__'}
INSTRUCTION_FILES = {'agents.md', 'agents.override.md', 'claude.md', 'skill.md'}


def ignored(path):
    return bool(set(part.lower() for part in path.parts) & IGNORED_PARTS) or bool(re.search(r'\.(generated|pb)\.', path.name, re.I))


def prompt_intent(prompt):
    # Conservative hints, not an LLM intent classifier. Do not treat quoted code as a request.
    text = re.sub(r'```.*?```', '', prompt, flags=re.S).lower()
    text = re.sub(r'(?m)^>.*$', '', text)
    flags = set()
    formatting = bool(re.search(r'\b(format(?:ting)?|whitespace|typos?|comment[- ]only)\b', text))
    prose = bool(re.search(r'\b(write|draft|rewrite|revise|edit|update|improve|review|fix)\b.{0,60}\b(docs?|documentation|readme|proposals?|reports?|emails?|paragraphs?|articles?|guides?|pr description)\b|\bdocument (the|this|our)\b', text))
    diagram = bool(re.search(r'\b(tikz|uml|sequence diagram|class diagram|object diagram|component diagram|architecture diagram|activity diagram|workflow diagram)\b', text))
    code_request = bool(re.search(r'\b(implement|fix|debug|add|build)\s+(?:(?:a|an|the|new|c\+\+|java)\s+){0,3}(code|feature|bug|crash|parser|handler|function|method|endpoint|module|service|test)\b', text))
    prose_only = prose and not code_request
    diagram_only = diagram and not code_request
    architecture = bool(re.search(r'\b(architecture|module boundaries|dependency direction|decouple|dependency inversion)\b', text)) and not prose_only and not diagram_only
    behavior = bool(re.search(r'\b(implement|fix|debug|add|build|change behavior|change behaviour)\b', text)) and not prose_only and not diagram_only and not formatting
    refactor = bool(re.search(r'\b(refactor|restructure)\b', text)) and not prose_only and not formatting
    verification = bool(re.search(r'\b(tests?|testing|test strategy|coverage|verify correctness|verification)\b', text)) and not prose_only and not formatting
    # Explicit opt-outs take precedence over inferred implementation intent.
    skip_workflow = bool(re.search(r"\b(no|without|skip|don't|do not)\s+(?:use\s+)?(?:tdd|tests?|testing)\b", text))
    if skip_workflow:
        behavior = False
        verification = False
    if prose:
        flags.add('prose')
    if diagram:
        flags.add('diagram')
    if architecture:
        flags.add('architecture')
    if behavior:
        flags.update({'behavior', 'verification'})
    if verification or refactor:
        flags.add('verification')
    if not prose_only and not diagram_only:
        if re.search(r'(?<!\w)c\+\+(?!\w)|\bcpp\b|\S+\.(?:cpp|cc|cxx|c\+\+|hpp|hh|hxx|h\+\+|ipp|inl|tpp)(?!\w)', text):
            flags.add('cpp')
        if re.search(r'\bjava\b|\S+\.java\b', text):
            flags.add('java')
    if 'cpp' in flags:
        if architecture:
            flags.add('cpp-architecture')
        if re.search(r'\bheaders?\b|\S+\.(?:hpp|hh|hxx|h\+\+|ipp|inl|tpp)(?!\w)', text):
            flags.add('cpp-header')
    if prose_only or diagram_only:
        mode = 'prose'
    elif formatting:
        mode = 'formatting'
    elif skip_workflow:
        flags.difference_update({'behavior', 'verification'})
        mode = 'no-workflow'
    elif re.search(r'\b(review|inspect|explain|read[- ]only)\b', text) and not behavior:
        mode = 'review'
    elif behavior:
        mode = 'behavior'
    elif refactor:
        mode = 'refactor'
    elif verification:
        mode = 'verification'
    else:
        mode = 'unknown'
    return flags, mode


def tool_paths(event):
    name = event.get('tool_name', '')
    args = event.get('tool_input', {})
    if isinstance(args, str):
        args = {'command': args}
    if not isinstance(args, dict):
        return [], False, ''
    writing = name in {'Edit', 'Write', 'MultiEdit', 'apply_patch', 'write_file', 'edit_file'}
    paths = []
    for key in ('file_path', 'path'):
        if isinstance(args.get(key), str):
            paths.append(args[key])
    command = args.get('command', args.get('cmd', ''))
    if name == 'apply_patch' or (isinstance(command, str) and command.lstrip().startswith('*** Begin Patch')):
        command = command or args.get('patch', args.get('input', ''))
        paths.extend(re.findall(r'^\*\*\* (?:Add|Update|Delete|Move to) File: (.+)$', command, flags=re.M))
        # apply_patch uses "*** Move to:" without "File:".
        paths.extend(re.findall(r'^\*\*\* Move to: (.+)$', command, flags=re.M))
        writing = True
    elif name in {'Bash', 'exec_command', 'shell_command'} and isinstance(command, str):
        # Never execute or interpret arbitrary shell/Python programs to find paths.
        # Recognize simple source reads; structured Edit/Write/apply_patch cover writes.
        try:
            tokens = shlex.split(command)
        except ValueError:
            tokens = []
        if tokens and tokens[0] in {'cat', 'head', 'tail', 'sed', 'rg', 'less', 'wc'}:
            cwd = Path(event.get('cwd', '.'))
            for token in tokens[1:]:
                if not token.startswith('-') and '\n' not in token and (cwd / token).is_file():
                    paths.append(token)
    content = args.get('content', args.get('new_string', command if writing else ''))
    return paths, writing, content if isinstance(content, str) else ''


def cpp_header(path, state, cwd):
    if 'cpp' in state.get('intent', []):
        return True
    if any(path.with_suffix(suffix).is_file() for suffix in (CPP_SUFFIXES | {'.C'}) - {'.inl', '.ipp', '.tpp'}):
        return True
    for parent in [path.parent] + list(path.parents)[:3]:
        cmake = parent / 'CMakeLists.txt'
        if cmake.is_file():
            with cmake.open(encoding='utf-8', errors='replace') as source:
                text = source.read(16384)
            text = re.sub(r'#[^\n]*', '', text)
            if re.search(r'\b(CXX|CXX_STANDARD|CMAKE_CXX_STANDARD|cxx_std_\d+)\b', text):
                return True
        if parent == cwd:
            break
    return False


def file_signals(event, state):
    paths, writing, content = tool_paths(event)
    flags = set()
    recognized = False
    cwd = Path(event.get('cwd', '.')).resolve()
    for raw in paths:
        path = Path(raw)
        if not path.is_absolute():
            path = cwd / path
        try:
            relative = path.relative_to(cwd)
        except ValueError:
            relative = path
        if ignored(relative):
            continue
        suffix = path.suffix.lower()
        if path.suffix == '.C' or suffix in CPP_SUFFIXES or (suffix == '.h' and cpp_header(path, state, cwd)):
            flags.add('cpp')
            intent = set(state.get('intent', [])) | {'cpp'}
            if suffix in CPP_HEADER_SUFFIXES:
                intent.add('cpp-header')
            if 'cpp-header' in intent:
                flags.add('cpp-header')
            if 'architecture' in intent:
                flags.add('cpp-architecture')
            state['intent'] = sorted(intent)
        if suffix == '.java':
            flags.add('java')
        code = suffix in CODE_SUFFIXES or path.suffix == '.C'
        if code:
            recognized = True
            mode = state.get('mode', 'unknown')
            if (mode == 'behavior' or (writing and mode == 'unknown')):
                flags.update({'behavior', 'verification'})
            elif mode in {'refactor', 'verification'}:
                flags.add('verification')
            if 'architecture' in state.get('intent', []):
                flags.add('architecture')
        if suffix in DOC_SUFFIXES and path.name.lower() not in INSTRUCTION_FILES:
            flags.add('prose')
            recognized = True
        if suffix == '.tex':
            sample = content
            if path.is_file():
                with path.open(encoding='utf-8', errors='replace') as source:
                    sample += '\n' + source.read(16384)
            flags.add('diagram' if re.search(r'\\(?:begin\{tikzpicture\}|usetikzlibrary|tikzset)', sample) else 'prose')
            recognized = True
    return flags if recognized else None


def select_signals(event, state):
    if event['hook_event_name'] == 'UserPromptSubmit':
        flags, mode = prompt_intent(event.get('prompt', ''))
        if flags or mode != 'unknown':
            state['intent'] = sorted(flags)
            state['mode'] = mode
            return flags
        return None  # "continue" and status messages do not erase task context.
    return file_signals(event, state)

def skill_context(event, root, routes, skill):
    name = event['hook_event_name']
    session = event['session_id']
    selectors = set(routes['skills'][skill])
    source = (root / 'skills' / skill / 'SKILL.md').resolve()
    if not source.is_relative_to(root):
        raise ValueError('skill must stay inside its package')
    text = source.read_text(encoding='utf-8')
    if text.startswith('---\n'):
        text = text.split('\n---\n', 1)[1].lstrip()
    body = (f"Skill: {routes['plugin']}:{skill}\nSkill directory: {source.parent}\n"
            'Resolve relative references in that directory. Load supporting references only when needed.\n\n' + text)
    digest = hashlib.sha256(body.encode()).hexdigest()
    identity = [session, event.get('cwd', ''), event.get('agent_id', ''), routes['plugin'], skill]
    key = hashlib.sha256(json.dumps(identity).encode()).hexdigest()
    data = os.environ.get('PLUGIN_DATA') or os.environ.get('CLAUDE_PLUGIN_DATA')
    if not data:
        raise ValueError('plugin data directory is unavailable; context hook skipped')
    directory = Path(data) / 'skill-context'
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    path = directory / (key + '.json')
    with state_lock(path):
        state = read_state(path)
        before = dict(state)
        if name == 'PreCompact':
            state['emitted'] = ''
            context = ''
        else:
            if name == 'SessionStart':
                if event.get('source') in {'startup', 'clear', 'fork'}:
                    state = {}
                elif event.get('source') in {'compact', 'resume'}:
                    state['emitted'] = ''
            else:
                signals = select_signals(event, state)
                if signals is not None:
                    state['active'] = bool(selectors & signals)
            context = body if state.get('active') and state.get('emitted') != digest else ''
            if context:
                state['emitted'] = digest
        if state != before:
            save_state(path, state)
        return context


def main():
    event = json.load(sys.stdin)
    if not isinstance(event, dict) or not event.get('session_id'):
        return
    if event.get('hook_event_name') not in {'UserPromptSubmit', 'PreToolUse', 'SessionStart', 'PreCompact'}:
        return
    root = Path(os.environ.get('VIBE_CONTEXT_PLUGIN_ROOT', Path(__file__).resolve().parents[1])).resolve()
    routes = json.loads((root / 'hooks/routes.json').read_text(encoding='utf-8'))
    skills = sys.argv[1:] or list(routes['skills'])
    contexts = []
    for skill in skills:
        context = skill_context(event, root, routes, skill)
        if context:
            contexts.append(context)
    if contexts:
        print(json.dumps({'hookSpecificOutput': {'hookEventName': event['hook_event_name'],
                                               'additionalContext': '\n\n'.join(contexts)}}), flush=True)


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, IndexError, TypeError) as error:
        # These hooks supply context only. A loader problem must not reject work.
        print(f'vibe-coding context hook skipped: {error}', file=sys.stderr)
