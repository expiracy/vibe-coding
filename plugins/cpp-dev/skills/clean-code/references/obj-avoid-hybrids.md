---
title: "Keep Data and Behavior Responsibilities Clear"
impact: MEDIUM-HIGH
impactDescription: "Make it clear whether a type is a plain record or an abstraction responsible for enforcing a rule"
tags: clean-code, obj
---

## Keep Data and Behavior Responsibilities Clear

Make it clear whether a type is a plain record or an abstraction responsible for enforcing a rule. Avoid a design that appears to protect an invariant while callers can bypass it through exposed internal state.

Public data plus harmless convenience operations can be appropriate for a value or transfer record. Do not add a layer of mechanical accessors merely to make the type look encapsulated.

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/).
