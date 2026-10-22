---
title: Design Failure Paths First
impact: HIGH
impactDescription: prevents missing error handling cases
tags: err, try-catch, tdd, boundaries
---

## Design Failure Paths First

Start by defining the caller-visible failure behavior, then organize success and reporting around that contract. Preserve the project's existing error policy. Do not prescribe exceptions for a project with a different failure contract.

**Benefits:**
- Forces you to consider error cases first
- Makes partial-success and failure expectations explicit
- Failure scenarios become observable requirements

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [err-write-try-catch-first](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/err-write-try-catch-first.md).
