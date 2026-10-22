---
title: Organize Classes for Change
impact: MEDIUM
impactDescription: minimizes modification risk when requirements change
tags: class, ocp, change, design
---

## Organize Classes for Change

Classes should be organized so that change is minimally invasive. Following the Open-Closed Principle (OCP): classes should be open for extension but closed for modification.

Choose extension points from a real extension requirement. A small closed set of
alternatives may be clearer as explicit cases; do not add a hierarchy merely to
satisfy the principle.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [class-organize-for-change](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/class-organize-for-change.md).
