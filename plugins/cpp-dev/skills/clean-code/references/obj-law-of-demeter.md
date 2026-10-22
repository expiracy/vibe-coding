---
title: Follow the Law of Demeter
impact: MEDIUM-HIGH
impactDescription: prevents hidden dependencies between modules
tags: obj, demeter, coupling, encapsulation
---

## Follow the Law of Demeter

A method should only call methods on: its own object, objects passed as parameters, objects it creates, or its direct component objects. Avoid chained method calls on returned objects.

Navigation through explicit data records and fluent APIs is not the same as
reaching into an object's private collaborators. Do not add forwarding wrappers
merely to reduce the number of dots in an expression.

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-law-of-demeter](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-law-of-demeter.md).
