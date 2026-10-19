---
title: "Separate Commands from Queries"
impact: MEDIUM
impactDescription: "Keep ordinary queries free of surprising mutation and name commands to reveal their effects"
tags: clean-code, func
---

## Separate Commands from Queries

Keep ordinary queries free of surprising mutation and name commands to reveal their effects. A command may return an outcome or extracted value when that result naturally belongs to the operation.

Do not split an operation that must remain indivisible just to enforce a rule about return values. Preserve the contract of combined operations such as consuming an item and returning it, or recording an insertion and reporting its outcome.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
