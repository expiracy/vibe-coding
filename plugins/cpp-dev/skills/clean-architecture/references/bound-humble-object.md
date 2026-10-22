---
title: Use Humble Objects at Architectural Boundaries
impact: MEDIUM-HIGH
impactDescription: maximizes testable code, isolates hard-to-test parts
tags: bound, humble-object, testing, boundaries
---

## Use Humble Objects at Architectural Boundaries

Keep the hard-to-test device/UI/network edge small. Extract deterministic decisions into ordinary C++ operations; still test the real edge for its own contract.

A direct logic test establishes only the tested decision. Rendering, threading and device behavior need their own integration or UI checks.

Reference: [Clean Architecture - Humble Object Pattern](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch23.xhtml)

Upstream rule: [bound-humble-object](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/bound-humble-object.md).
