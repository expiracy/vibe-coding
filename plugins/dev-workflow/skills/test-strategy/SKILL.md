---
name: test-strategy
description: Choose appropriate tests and review coverage for changed behavior, integrations and failure modes. Use for test planning, deciding what to mock or run for real, and assessing whether checks support a correctness claim.
---

# Test Strategy

Choose checks from the behavior and risks of the change. Reuse the project's
frameworks and conventions. For a small change, a few planning notes can be
enough; a separate strategy document is needed only when requested or useful to
the project.

## Decide what evidence is needed

- Read the changed behavior, callers and existing tests. Identify observable
  outcomes, invariants, compatibility requirements and plausible failures. Reuse
  existing coverage before adding tests; prioritize consequences and uncertainty.
- For each important risk, choose the smallest test boundary that can expose it.
  Direct tests suit calculations and application decisions. Exercise the actual
  serializer or adapter for representation and integration claims; use real
  infrastructure where the claim depends on its behavior. A critical journey may
  need an end-to-end check. Do not impose test ratios or require every test level
  for every change.
- Make assertions about the agreed result, error or side effect. Use expectations
  independent of the implementation. Verify absence of effects when rejection or
  rollback requires it; retain meaningful regression coverage.
- Keep external behavior controllable where isolation helps. A fake proves how
  the caller handles that fake, not that the real dependency has the same contract.
  State which dependency, version and configuration each integration check covers.
- Select relevant boundary, empty, invalid and partial-failure cases. Add property,
  concurrency, fuzz, performance or native-code diagnostics when the actual risk
  warrants them. Preserve the project's error and consistency contracts.

## Load detail when needed

- [Test selection](references/test-selection.md): unit, integration, contract and
  end-to-end boundaries, plus examples of matching a risk to evidence.
- [Boundaries and failures](references/boundaries-and-failures.md): real services,
  persistence, retries, partial success and controllable test doubles.
- [Trustworthy results](references/trustworthy-results.md): independent oracles,
  determinism, useful assertions, execution and reporting.

## Execute and report proportionately

Run focused checks, then the relevant regression checks. Distinguish a behavior
failure from an unavailable dependency or broken runner. An unavailable integration
check leaves its claim unverified; passing fake-based tests do not replace it.
Report actual commands, outcomes and material gaps. Expand testing when a failure,
new change or unresolved risk justifies it, and stop when the relevant checks pass
and the agreed scope is covered.

This skill chooses verification coverage; Canon TDD guides implementation one
scenario at a time. When using TDD, keep the broader scenario list as notes and
implement only the next selected test before proceeding through its loop.
