# Select a test boundary from the risk

Test labels vary by project. Say what runs together, what is real and what is
substituted. A unit need not be one class; related in-process objects can be
cheaper and more useful to test together than through extensive mocking.

| Risk or claim | Useful evidence | What this alone does not establish |
|---|---|---|
| Calculation, parsing rule or domain invariant | Direct input/output tests with known expected results and boundary cases | Correct endpoint wiring or persistence |
| Application decision or workflow | Exercise the public operation with controlled external dependencies; assert results and required effects | Actual vendor/database behavior |
| DTO or protocol mapping | Round-trip or fixture tests through the real serializer/parser, including invalid inputs and missing fields | A deployed peer accepts that representation |
| Database mapping, constraint, query or migration | Integration checks with the relevant engine/version/configuration and real schema | Behavior under every production load or failure |
| Consumer/provider compatibility | Verify the consumer's expectations against the actual provider implementation or an executable provider-verified contract | Provider availability or an entire user journey |
| Startup, dependency composition or packaging | Start the built application through its real entry point in a controlled environment | Every business rule and error path |
| Critical user journey across components | A focused end-to-end check through the relevant deployed/tested components | Detailed coverage of all edge cases |

Choose the least expensive boundary that makes the important defect observable.
Complement it with another level when that level answers a different question.
For example, an in-process handler can test validation and error mapping while a
small startup check verifies that the route is actually registered. Avoid
repeating every validation case through a browser merely to cover the same rule.

## Work from the change

- A price-calculation change needs known totals, limits and rounding rules. Add a
  database or browser check only if storage, representation or wiring is affected.
- A SQL query change needs representative rows, constraints, ordering and the
  actual dialect. A repository fake cannot detect a wrong join or SQL syntax.
- A retry change needs success, retryable/non-retryable failure, exhaustion and
  the observable effects of another attempt. Check uncertain outcomes separately
  if an earlier request may have succeeded remotely.
- A refactor needs evidence that required results, errors, mutation, ordering and
  external effects survive. Characterization tests can capture established
  behavior; intentional behavior changes need an explicit new expectation.

Read existing tests before planning new ones. Coverage numbers help locate code
that ran, but do not establish that the right outcomes were asserted. No universal
unit/integration/E2E percentage or coverage target applies to every project.

For a larger task, a compact plan can map each outcome or risk to its chosen
boundary, real dependencies, existing/new check and execution status. Keep
unimplemented scenarios as notes when following Canon TDD. Do not create tests
for an internal helper solely because the helper exists.

Further reading: Ham Vocke's [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
discusses test granularity, contracts and avoiding duplicated coverage. This
reference is original guidance informed by that discussion, not a copied rule pack.
