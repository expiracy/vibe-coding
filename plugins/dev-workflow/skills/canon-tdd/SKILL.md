---
name: canon-tdd
description: Use when implementing features, fixing bugs, or changing behavior with automated tests, especially when the user requests TDD, Canon TDD, or Kent Beck's approach. Does not apply to prose edits or changes without executable behavior.
---

# Canon TDD

Develop one behavior at a time, using a test to guide each change.

Based on Kent Beck's [Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd), published 11 December 2023. The loop below paraphrases his method; the execution checks add practical verification guidance.

## The loop

1. **List scenarios.** Make a short checklist of desired outcomes, boundaries, error cases, and existing behavior that must survive. Describe behavior, not planned classes or helpers. Extend the list as you learn.
2. **Choose one.** Turn exactly one pending scenario into a runnable automated test with setup, an invocation, and meaningful assertions. Let the test shape the interface. Keep other scenarios as notes, not runnable tests.
3. **Make it pass.** Change the implementation just enough to satisfy that test and preserve earlier passing tests. Keep assertions honest; do not replace expected results with observed output to get green. Mark the scenario complete after verification.
4. **Optionally refactor.** Once green, improve the design where useful. Keep behavior unchanged and rerun tests. Avoid premature abstractions or unrelated cleanup.
5. **Repeat.** Choose the next pending scenario. Finish when the agreed behavior is covered and the list has no unresolved items.

## Execution checks

Before the loop, read relevant code and tests. Run the project's test command to establish a baseline. Preserve unrelated work and record pre-existing failures separately.

For each new behavior:

- **Red:** Run the new test before changing production behavior. Read the actual failure. It must expose the missing behavior; a broken import, unavailable runner, or unrelated exception is a setup problem. An absent API may require a minimal declaration to obtain an executable behavioral failure.
- **Green:** Implement, run the focused test, then the relevant regression suite. Inspect exit codes and assertions. All previously passing relevant tests must stay green before proceeding.
- **Refactor:** If you refactor, rerun those checks before starting another scenario.

If a new test already passes, inspect why. A valid test of existing behavior can remain as coverage; mark that scenario covered and choose a missing behavior. Do not deliberately break correct code to manufacture red.

If execution tools are unavailable, give the user the test command and continue from their actual output. If tests cannot run, resolve the environment within the task's authorization or report the blocker; do not claim red, green, or a verified TDD result.

For bugs, reproduce the failure in a test. Passing characterization tests can establish a baseline for untested code. If you implement first, acknowledge it and recover red by safely undoing only your own change. Preserve existing code.

## Keep progress small

Example scenario list for a retry function:

```text
[ ] returns a successful result
[ ] retries a transient failure
[ ] stops at the attempt limit
```

Start with one runnable test. Choose the next after green; parameterized batches of pending scenarios count as multiple tests.

At handoff, report covered scenarios, executed test commands and results, and unresolved items. State deferred scope explicitly; keep pending scenarios visible.
