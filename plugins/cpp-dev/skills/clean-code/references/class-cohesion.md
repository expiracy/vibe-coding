---
title: Maintain Class Cohesion
impact: MEDIUM
impactDescription: enables extracting focused subclasses
tags: class, cohesion, variables, methods
---

## Maintain Class Cohesion

Classes should have a small number of instance variables. Each method should manipulate one or more of those variables. Methods should support a coherent concept; touching more fields does not make unrelated responsibilities cohesive.

**When cohesion breaks down:** If a subset of methods only uses a subset of variables, extract those methods and variables into a separate class.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [class-cohesion](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/class-cohesion.md).
