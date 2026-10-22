---
title: Use DTOs for Data Transfer
impact: MEDIUM
impactDescription: prevents sensitive data exposure at boundaries
tags: obj, dto, transfer, boundary
---

## Use DTOs for Data Transfer

Data Transfer Objects (DTOs) are pure data structures for transferring data between layers or systems. They should have no behavior beyond accessors. Use them at system boundaries.

**Use DTOs when:**
- Transferring data across system boundaries (API, database, message queue)
- Hiding internal structure from external consumers
- Transforming data format between layers

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-dto](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-dto.md).
