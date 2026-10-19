---
title: "Expose Meaningful Operations"
impact: MEDIUM-HIGH
impactDescription: "Hide representation behind operations when that protects an actual invariant or lets the representation change independently"
tags: clean-code, obj
---

## Expose Meaningful Operations

Hide representation behind operations when that protects an actual invariant or lets the representation change independently. Design an interface around what callers need to do.

Mechanical accessors for every field do not necessarily provide an abstraction. Plain records are appropriate when their purpose is to transfer independent data without enforcing behavior.

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/).
