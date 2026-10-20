# Boundaries, test doubles and partial failures

## Decide what must be real

Use a stub, fake or mock to control a dependency when the claim concerns the
caller's decision. Prefer a small fixture or a real in-process collaborator when
that makes the contract clearer. Verify a call or ordering only when the
interaction itself is a required outcome, such as an audit write or a single
permitted external request; avoid assertions about incidental helper calls.

A real adapter needs separate evidence for the behavior it translates: database
constraints and transactions, message formats, HTTP status/error mapping,
filesystem semantics, dependency wiring or a vendor protocol. Match the relevant
version, schema, flags and configuration. Use isolated test resources and the
project's established setup/cleanup approach. Do not assume a different database
engine, mock server or emulator reproduces the production contract.

A contract check is useful only for the contract exercised. A payload-schema
check does not establish business semantics, authorization, availability or
cross-service atomicity. A consumer expectation tested only against its own stub
has not been verified against the provider. Record the scope explicitly.

## Choose failure cases around observable state

Start with the actual operation and its promised consistency. Consider failures
before work starts, during a write, after a durable write, and after a remote
success whose response is lost. Select the cases that the change can affect;
there is no requirement to simulate every failure for every function.

For an order-plus-message workflow, distinct questions might be:

| Scenario | Required evidence, if this is the promised contract |
|---|---|
| Rejected input | Required error and no new durable order/message |
| Failure before a local transaction commits | Neither local write survives |
| Successful local transaction | The pending order and outbox record both persist |
| Worker redelivers a message | Stable operation identity and the required deduplication/idempotency behavior |
| Remote success with lost response | Recovery/reconciliation handles uncertainty without assuming the charge failed |

Test local atomicity against the database and transaction implementation that
provide it. Test worker retry/recovery separately. Rolling back a database cannot
undo an external payment or email. Exactly-once business effects require a real
end-to-end protocol; a mock call count or a passing retry loop does not prove them.

## Keep failures controlled and diagnosable

Control clocks, randomness, service outcomes and scheduling where they affect the
claim. Use deterministic synchronization for race-sensitive cases instead of
hoping sleeps produce a particular interleaving. Keep useful seeds and failing
inputs when randomized testing is appropriate.

Observe the final state, returned result and required effects. Inject a failure
at the relevant boundary instead of modifying unrelated production paths. A test
of a fake rollback proves the fake; inspect durable state through the real
transaction path for a persistence claim.

If the necessary test environment is unavailable, continue with useful narrower
checks and report the missing integration evidence. Resolve dependencies within
the task's authorization; do not silently use production services or create
external side effects to make a test pass.
