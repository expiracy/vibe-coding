---
title: Separate Commands from Queries
impact: MEDIUM
impactDescription: eliminates ambiguous function behavior
tags: func, cqs, command, query, separation
---

## Separate Commands from Queries

Separate queries from unrelated state changes, and make a command's effects and
result clear in its contract.

The separation makes ordinary single-threaded usage easier to read. A command
may return its natural result; do not split checking and updating when the
operation must remain atomic.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-command-query-separation](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-command-query-separation.md).
