# Native hook verification — 2026-10-22

Verified against Codex CLI 0.160.0 and Claude Code 2.1.282 using disposable local
fixtures. The model-backed runs used the actual clients, installed plugins,
normal hook dispatch and recorded hook outputs. No application/project code was
changed by the verification runs.

## Enabled configuration

Codex's `hooks/list` reports 20 intended context hooks, all enabled and trusted,
with no warnings or errors. The five plugin packages are enabled in both clients:

| Plugin | Version |
|---|---|
| cpp-dev | 2.2.1 |
| java-dev | 1.1.1 |
| dev-architecture | 1.1.1 |
| dev-workflow | 1.2.1 |
| doc-tools | 1.2.1 |

This Codex installation discovered the skills but zero bundled hooks. The
compatibility installer registered the same reviewed loaders as supported user
hooks. Trust was granted through Codex's normal `/hooks` review; no repository
trust or global hook-trust bypass was granted. Claude discovered its packaged
hooks directly. An expired Claude login initially prevented model calls; the
live checks completed after the user refreshed authentication.

## Live-client observations

| Scenario | Codex | Claude |
|---|---|---|
| C++ source read plus two separate comment edits | Each C++ main body injected once; no repeat-edit injection | Each C++ main body injected once; no repeat-edit injection |
| Java source read, two edits, then two further edits | Java body once; follow-up edits injected nothing | Java body once; follow-up edits injected nothing |
| Test-planning request | Test strategy once; no TDD body | Test strategy once; no TDD body |
| Implementation-intent routing probe | TDD once; previously loaded test strategy not repeated | TDD once; previously loaded test strategy not repeated |
| Dependency-direction routing probe | Architecture body once | Architecture body once |
| README read and two edits, followed by two more edits | Writing body once; follow-up edits injected nothing | Writing body once; follow-up edits injected nothing |
| Diagram creation and repeated label edits | Diagram body once; no repeat injection | Diagram body once; no repeat injection |
| Compaction and continuation | PreCompact invalidated markers; SessionStart restored active C++ bodies once before the next model request | Real `/compact` restored the active diagram body once; two subsequent Edit calls injected nothing |

The routing probes requested a short response without changing files; they check
activation rather than the quality of an implementation or design. Native tool
records confirm the read/edit operations and expected fixture contents. The tests
did not invoke Skill or read SKILL.md themselves, so those actions cannot explain
the observed hook-body delivery.

Codex compaction is not necessarily an immediate restoration at the end of the
compact operation: the SessionStart compact hook runs before continuation. An
initial harness that waited for restoration without starting a continuation was
insufficient; the follow-up test observed the actual next-request behavior.

## Fixes made during verification

- Added an idempotent Codex compatibility installer that preserves other user
  hooks, supplies concrete installed paths/data directories, and removes its own
  fallback entries when native discovery provides all four required events.
- Removed `additionalContextLimit` from Codex PreCompact handlers. That event
  cannot emit additional context and the setting produced native warnings.
- Classified partial `.tex` edits using the replacement fragment plus a bounded
  prefix of the existing file, preserving diagram routing when editing a label.

## Regression checks and limits

`python3 -m unittest discover -s tests -v` passes 39 tests. These cover routing,
body/reference separation, repeated edits, session/agent isolation where IDs are
available, parallel calls, body changes, resume/clear/compaction, malformed cache
recovery, failure without blocking work, quoted installation paths, adapter
commands, and preservation/idempotency of compatibility registration. Native
plugin/marketplace validation and bundle synchronization checks also passed.

Header-language inference, cache corruption, parallel races and synthetic body
updates are isolated process/filesystem tests; they are not all separate live
model scenarios. Passing this finite set does not establish every phrasing,
editor integration, future client version or production workload.

Deduplication covers hook emissions. Native skill discovery and explicit file
reads remain separate mechanisms. Re-run compatibility setup after plugin
updates/enables/disables, and review any changed definitions through `/hooks`.
See [setup and limitations](skill-context-hooks.md).
