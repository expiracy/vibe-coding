---
title: "Make Warning Comments Actionable"
impact: MEDIUM
impactDescription: "Document a non-obvious consequence at the operation that causes it"
tags: clean-code, cmt
---

## Make Warning Comments Actionable

Document a non-obvious consequence at the operation that causes it. State the triggering condition, the consequence, and what a caller needs to do.

A warning such as "this operation permanently removes the selected records" is more useful than "be careful". Prefer an interface that prevents misuse when practical; a comment does not replace necessary checks. Do not invent timings or resource-cost claims.

Reference: [Clean Code, Chapter 4: Comments](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
