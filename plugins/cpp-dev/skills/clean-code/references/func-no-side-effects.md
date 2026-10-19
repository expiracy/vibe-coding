---
title: "Avoid Surprising Side Effects"
impact: HIGH
impactDescription: "Make significant effects visible in the operation's name and contract"
tags: clean-code, func
---

## Avoid Surprising Side Effects

Make significant effects visible in the operation's name and contract. A calculation or query should not unexpectedly change configuration, send a message, or alter unrelated state.

Necessary effects can be appropriate; keep them deliberate and easy for callers to identify. Refactoring should preserve required effects and their ordering, rather than removing them to make a function look pure.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
