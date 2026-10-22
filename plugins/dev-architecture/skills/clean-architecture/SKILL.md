---
name: clean-architecture
description: Design or review module boundaries, dependency direction, entities, use cases and infrastructure isolation using Clean Architecture. Use for architecture decisions and incremental boundary refactoring; ordinary naming or function cleanup belongs to Clean Code.
license: MIT
metadata:
  version: "1.0.1"
---

# Clean Architecture

Protect business policy from delivery mechanisms and infrastructure. Adapt the
[upstream 42-rule collection](UPSTREAM.md) to the existing system; use the
[rule index](references/architecture-index.md) to load only relevant references.

## Apply at the smallest useful scope

- Identify the policy that needs protection, actual change pressure and existing
  dependency direction. Simple CRUD, scripts and stable framework-oriented code
  may need no additional layers. Do not reorganize a repository for folder names.
- Source dependencies point toward policy. Inner code defines the contracts it
  needs; outer adapters implement them. Runtime calls can travel outward through
  those contracts. Interfaces are useful at real seams, not mandatory per class.
- Entities or domain functions protect reusable rules and invariants. Use cases
  own application-specific rules and orchestration. Both can contain business
  rules; distinguish their scope rather than pushing everything into entities.
- Translate transport, vendor and persistence formats at the affected boundaries.
  Keep models shaped for their consumers; duplicate models only when distinct
  meanings or change reasons justify the mapping.
- Compose concrete infrastructure at startup or another outer composition point.
  Preserve public APIs, observable behavior, project conventions and error policy
  unless the requested architecture change requires an agreed contract change.
- State consistency and failure behavior explicitly. Local transactions cannot
  undo remote payments or messages. Use the existing recovery approach and test
  partial failures; see [transaction boundaries](references/usecase-transaction-boundary.md).

## Choose supporting detail

- Start with [dependency direction](references/dep-inward-only.md) or
  [boundary costs](references/bound-boundary-cost-awareness.md) for placement decisions.
- Use the [C++20 example](references/cpp-example.md) or
  [Java 11 example](references/java-example.md) for policy, ports, adapters and wiring.
  The two examples express the same architecture. Their limits, data and error
  mechanisms are illustrations, not application requirements.
- The remaining indexed rules retain upstream examples in several languages.
  These are contextual excerpts; adapt them to the actual stack rather than
  copying a framework or installing a dependency to match an example.

## Verify the affected boundary

Test domain invariants and application decisions directly. Check adapter mapping
and real integration contracts separately. Use dependency/build checks where
available, and integration tests for transaction behavior and composition. A fake
adapter cannot establish vendor behavior or durability.

For a review, report the policy, offending dependency and smallest useful fix.
For implementation, migrate one boundary at a time and run meaningful project
checks. Explain any deliberate choice to retain a simpler design and report
checks that actually ran.
