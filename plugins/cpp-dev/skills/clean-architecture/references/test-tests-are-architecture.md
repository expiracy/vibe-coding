---
title: Tests Are Part of the System Architecture
impact: LOW-MEDIUM
impactDescription: enables fast feedback, documents behavior
tags: test, architecture, design, first-class
---

## Tests Are Part of the System Architecture

Test stable observable contracts and isolate only the external behavior the check does not intend to exercise. Keep infrastructure integration tests as distinct evidence.

Use the existing test framework in a real project. Stable public behavior is the target; fixtures need not mirror every production directory or private class.

Reference: [Clean Architecture - The Test Boundary](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch28.xhtml)

Upstream rule: [test-tests-are-architecture](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/test-tests-are-architecture.md).
