# Source and C++ adaptation

Adapted directly from [pproenca/dot-skills](https://github.com/pproenca/dot-skills),
path `skills/.experimental/clean-architecture`, revision `cf93c57cac89d6fc3e4194686000411567f5caf3`,
upstream skill version 1.0.6. All 42 rule identifiers and eight categories remain,
with the original MIT licence. Original downloads were checked against Git blob
hashes before adaptation. Each rule links to its immutable upstream original.

This version replaces multilingual examples with C++20 illustrations, C++ component
layouts or CMake excerpts. The Java comparison is removed. The checkout example
is executable; individual rule examples are independent compile-only excerpts,
sometimes declaring fictional external APIs. Compilation does not establish real
integration behavior, production correctness or effectiveness across models.

A focused header reference covers public contracts, includes and build dependencies.
The main file stays concise; detailed references load on demand. Language/library
policy remains in cpp-guidelines, and code readability remains in clean-code.

Corrections retained or clarified:

- Use cases own application rules; entities/domain functions own reusable invariants.
  Class hierarchies and an interface per operation are unnecessary.
- Local rollback cannot undo remote effects. An order/outbox contract needs actual
  transaction, idempotency and recovery verification in the real adapter/worker.
- Stable libraries, values and deterministic functions need no wrappers merely for
  isolation. Construction or function parameters can expose dependencies.
- Separate models/mappers where meaning, security or change reasons differ. Entities
  are not universally forbidden from crossing an internal boundary.
- Boundary cost, dependency metrics and test pyramids guide judgment, not layers,
  quotas or fixed ratios. Folders alone cannot enforce architecture.
- Durability, vendor replacement and disclosure need appropriate integration checks;
  fakes and syntax checks cannot establish these guarantees.

Principles are attributed upstream to Robert C. Martin's Clean Architecture.
Primary clarification: [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).
This adaptation is independent of the book author and upstream maintainers.
