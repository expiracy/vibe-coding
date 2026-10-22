---
name: clean-architecture
description: >-
  Design and review C++20 architecture, public headers, component dependencies,
  domain policy, use cases and adapters. Use when creating, editing or reviewing
  C++ headers, or changing C++ module boundaries and dependency direction.
license: MIT
metadata:
  version: "2.1.0"
  cpp-baseline: "20"
---

# Clean Architecture for C++

Protect policy from infrastructure at the smallest useful scope. Header edits
need a boundary check, not mandatory layers.

- Point dependencies toward policy; consumers own contracts. Functions, templates
  and runtime interfaces are options, not required layers.
- Keep domain invariants and application rules separate. Translate vendor, storage
  and transport formats at real boundaries; wire concrete adapters at the edge.
- Keep headers self-contained and check public types, includes and build links.
  Forward declarations alone do not reverse dependencies.
- Preserve APIs, ABI, behavior and error policy. Use C++20 within project constraints.
  Define failure guarantees; local rollback cannot undo remote effects.

Read [header guidance](references/cpp-headers.md) or the [42-rule index](references/architecture-index.md)
only as needed. Migrate one boundary
at a time. Run relevant header/build/behavior checks and real adapter checks for
integration claims; report actual results. [Source notes](UPSTREAM.md).
