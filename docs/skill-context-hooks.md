# Skill context hooks

Each plugin bundles a Python loader and host-specific hook configuration. The
loader emits only its own relevant `SKILL.md` bodies, with the installed skill
directory so relative references can be resolved. Skill references, templates
and assets stay on demand. Global `AGENTS.md` continues to load through the host.

## Loading policy

| Work | Main skill bodies |
|---|---|
| C++ task or source read/edit | `cpp-dev:clean-code`, `cpp-dev:cpp-guidelines` |
| Java task or source read/edit | `java-dev:clean-code` |
| Behavior implementation or bug fixing | `dev-workflow:canon-tdd`, `dev-workflow:test-strategy` |
| Test planning or coverage questions | `dev-workflow:test-strategy` |
| Refactoring with behavior preserved | `dev-workflow:test-strategy` |
| Architecture or dependency decisions | `dev-architecture:clean-architecture` |
| Human-facing prose, README or documentation work | `doc-tools:text-writing` |
| Software diagrams or identified TikZ source | `doc-tools:uml-diagrams` |

Pure formatting and explicit workflow opt-outs suppress automatic TDD/test
strategy loading. Source language guidance still applies. Generated/vendor
paths, test fixtures and instruction files such as `SKILL.md` and `AGENTS.md`
do not automatically trigger prose editing guidance. `.h` alone does not imply
C++: a C++ task, neighboring C++ file or nearby CMake CXX declaration supplies
that context. Arbitrary projects can still use explicit skill invocation.

## Events and deduplication

- `UserPromptSubmit` recognizes task/language hints before the model starts work.
- `PreToolUse` recognizes structured read/edit/write paths, patch target headers
  and file arguments in simple shell read commands. It supplies a fallback when
  prompt hints were insufficient; it never executes the tool input itself.
- `PreCompact` invalidates emission markers while retaining active skill choices.
- `SessionStart` after compaction/resume restores the most recently active main
  bodies once. New/cleared/forked sessions start with fresh hook state.

The plugin data directory stores small JSON cache entries keyed by conversation,
working directory, skill and available agent identity. Transcript filenames are
not part of the key because they may be omitted or rotated during compaction. A body is emitted
once until compaction/resume or a change to the body/installed source path. Parallel
calls coordinate with a lock and atomic cache replacement. Prompts and source
contents are not written to the cache; only routing hints and body hashes are.

Deduplication applies to these hook emissions. A host's native skill loader or an
explicit/manual file read can still load the same content independently. Hooks
add context; they cannot pin it permanently or remove earlier context. Automatic
routing uses conservative hints, so unusual phrasing and unknown editing tools
may require explicit skill invocation. Shell/Python programs that generate edits
and every possible MCP payload cannot be classified reliably by filename.

Pre-tool context is consumed on a subsequent model request: the pending tool call
has already been prepared. Prompt-time loading and early source-read hooks are
therefore preferred. These advisory hooks do not block edits, rewrite tool input,
execute tests, or claim that a pending edit already followed newly supplied rules.

Agent IDs are included when the host supplies them. A host that shares both the
session identity across agents without providing an agent ID cannot
support fully independent per-agent deduplication through this payload alone.

## Setup

Install Python 3.9+ with a `python3` command, update the installed plugins and
restart the client. Packages are self-contained: the repository's `tools/`
directory is for development only and is not needed by installed plugins.

- **Claude Code:** plugin `hooks/hooks.json` is discovered automatically. Inspect
  `/hooks` to confirm the enabled plugin hooks; honor any local/managed restrictions.
- **Codex:** the portable OpenAI extension (or compatibility manifest) selects
  `hooks/codex.json`. Open `/hooks` and review/trust the new hook definitions.
  Installation alone does not grant hook trust. If hooks were explicitly disabled,
  enable them in the client's configuration before relying on context injection.

Other hosts can adapt the event envelope and provide a writable plugin-data
location; skill instructions themselves remain provider-neutral. A host without
these adapters can continue to discover and load the packaged skills normally.

The loader uses `PLUGIN_DATA` or `CLAUDE_PLUGIN_DATA` for its cache. Missing data
storage, malformed inputs or a loader failure are reported on stderr and do not
reject the operation. A cache failure skips injection to avoid repeating full
bodies without reliable deduplication.

## Maintain and verify

`tools/skill-context/loader.py` is the canonical loader. After editing it or the
profiles/configuration in `tools/skill-context/sync.py`, refresh the bundled
copies and run the tests:

```sh
python3 tools/skill-context/sync.py
python3 tools/skill-context/sync.py --check
python3 -m unittest discover -s tests -v
```

Bump each affected plugin's version in all three manifests when releasing changes.
The tests run the real loader in separate processes with temporary plugin data;
they do not call model APIs or touch user conversations. Validate native plugin
manifests as well. End-to-end hook delivery also depends on the host's trust,
configuration and execution environment.

Official host contracts: [Codex hooks](https://learn.chatgpt.com/docs/hooks),
[OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins),
and [Claude Code hooks](https://code.claude.com/docs/en/hooks).
