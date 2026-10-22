---
title: Design for Testability From the Start
impact: LOW-MEDIUM
impactDescription: enables comprehensive testing without test-induced damage
tags: test, testability, design, interfaces
---

## Design for Testability From the Start

Make uncertain external inputs, including time when relevant, controllable. Deterministic functions, value constructors and pure static operations can be tested directly without new interfaces.

Choose the clock according to the real contract: wall time and elapsed monotonic time are different. Test the relevant before/at/after boundaries.

Reference: [Growing Object-Oriented Software, Guided by Tests](http://www.growing-object-oriented-software.com/)

Upstream rule: [test-testable-design](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/test-testable-design.md).
