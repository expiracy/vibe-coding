# Trustworthy test results

## Use an independent expectation

Derive expected results from the agreed behavior, a manually checked example or
an independent trusted implementation. Avoid copying the production algorithm
into the test, calculating expected output by calling the same helper, or
replacing expected values with observed values after a failure.

Property tests need properties that express the contract. A round-trip check can
miss a bug shared by the encoder and decoder; combine it with independently known
representations when interoperability matters. A sort test checking only order
can miss dropped or duplicated elements; also check that the required elements
and multiplicities survive.

Exercise behavior through stable interfaces. Use precise assertions for the
relevant fields, error details and side effects. Test names and failures should
identify the scenario, expected outcome and actual result without another run.
Multiple assertions can establish one coherent outcome. Snapshot tests need a
reviewed, meaningful baseline; bulk snapshot acceptance is not verification.

## Keep execution honest

- Establish a relevant baseline and distinguish pre-existing failures from new
  regressions. Keep fixtures isolated from other tests and external state.
- Run the test command; discovery, compilation or runner success alone does not
  prove that the intended tests ran. Check collected/executed cases and exit codes.
- A timeout or unavailable database is an environment or execution result, not a
  passing behavior check. A skipped integration case leaves its claim open.
- Checks must remain active in the build mode used. In C++, ordinary `assert`
  checks can disappear under `NDEBUG`; in Java, language assertions require
  enabling. Use the project's test assertions or always-active checks as appropriate.
- Diagnose flaky failures. Re-running until green is not evidence of a stable fix;
  retain the failure, identify the cause and report any remaining uncertainty.
- Use the existing build, test runner and diagnostics. Add a framework, mutation
  campaign, fuzz harness or benchmark only when the task's risk and scope justify it.

## Report what the checks establish

Report the commands actually executed and their outcomes, which important
behaviors/boundaries they exercise, and any skipped or unavailable checks. Keep
anticipated results and proposed commands distinct from observed execution.
Passing tests support the exercised claims; they do not establish exhaustive
correctness, production readiness or vendor behavior outside the tested scope.

Further reading: Titus Winters' [Test Failures Should Be Actionable](https://testing.googleblog.com/2024/05/test-failures-should-be-actionable.html)
explains why precise assertions and useful failure information matter.
