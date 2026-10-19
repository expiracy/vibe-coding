---
title: "Make Absence Explicit"
impact: HIGH
impactDescription: "Distinguish an expected missing value, an empty collection, and a failed operation in the public contract"
tags: clean-code, err
---

## Make Absence Explicit

Distinguish an expected missing value, an empty collection, and a failed operation in the public contract. Callers should not need to guess which meaning an ambiguous result carries.

Use the project's established representation for each outcome. An empty collection can mean there are no results; it must not conceal an operational failure. Do not introduce a fake object merely to hide an error.

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/).
