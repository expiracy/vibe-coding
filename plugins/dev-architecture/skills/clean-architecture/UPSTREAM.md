# Source and adaptation

Adapted directly from [pproenca/dot-skills](https://github.com/pproenca/dot-skills),
path `skills/.experimental/clean-architecture`, revision `cf93c57cac89d6fc3e4194686000411567f5caf3`,
upstream skill version 1.0.6. This source is under upstream's `.experimental` tree.
All 42 rule files and eight categories are retained, with the original MIT licence.
Downloaded reference files were checked against their Git blob hashes at this
revision. Each rule links to its immutable upstream original.

The main skill is a concise router. The original index is a reference; additional
C++20 and Java 11 examples illustrate the same small workflow. Other upstream
examples remain contextual excerpts, including application/framework types.
They are not complete applications or dependency installation instructions.

Bounded corrections:

- Use cases contain application-specific business rules; entities contain reusable
  domain rules. The dependency example moves persistence orchestration out of the
  entity to agree with the collection's entity guidance.
- A local database transaction does not roll back a remote payment. The revised
  example records a pending order and outbox message in the same local transaction;
  remote processing requires idempotency, recovery and reconciliation.
- Domain isolation does not ban every supporting library. Testing guidance does
  not ban pure constructors or static functions or require an interface per class.
- Mappers, models and service layers are justified by actual boundaries, not quotas.
- Unsupported numerical effectiveness claims are removed. Example success and
  compilation do not establish production correctness or model effectiveness.

Principles are attributed upstream to Robert C. Martin's *Clean Architecture*.
Primary clarification: [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).
This adaptation is independent of the book author and upstream maintainers.
