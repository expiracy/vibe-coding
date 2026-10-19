---
title: "Keep Tests Readable"
impact: MEDIUM
impactDescription: "Treat tests as maintained code"
tags: clean-code, test
---

## Keep Tests Readable

Treat tests as maintained code. Make the relevant inputs, action, expected behavior, and failure context clear. Use modest helpers without hiding the scenario behind fixture machinery.

Prefer observable results and state over private implementation details. Check required external interactions when they are part of the behavior, and keep unrelated scenarios independently understandable.

Reference: [Clean Code, Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
