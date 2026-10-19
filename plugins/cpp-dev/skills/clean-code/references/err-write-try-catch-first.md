---
title: "Design Failure Paths First"
impact: HIGH
impactDescription: "Define what callers should observe when an operation cannot complete before concentrating only on success"
tags: clean-code, err
---

## Design Failure Paths First

Define what callers should observe when an operation cannot complete before concentrating only on success. Identify the relevant failure cases and the state that must remain valid.

Test meaningful failure behavior alongside success. Distinguish a partial result from a completed operation, and make recovery or retry conditions explicit rather than hiding them in the happy path.

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/).
