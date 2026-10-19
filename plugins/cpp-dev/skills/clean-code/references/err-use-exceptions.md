---
title: "Separate Error Handling from the Happy Path"
impact: HIGH
impactDescription: "Keep the successful operation readable while preserving meaningful failures"
tags: clean-code, err
---

## Separate Error Handling from the Happy Path

Keep the successful operation readable while preserving meaningful failures. Separate recovery or translation from ordinary work where doing so clarifies the contract.

Use the project's existing failure convention. This principle does not mandate exceptions or permit silently swallowing an error. A failure must not look like a successful result.

Reference: [Clean Code, Chapter 3: Functions and Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/).
