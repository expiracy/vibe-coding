---
title: "Define Errors by Caller Needs"
impact: HIGH
impactDescription: "Classify failures by what the caller can do about them"
tags: clean-code, err
---

## Define Errors by Caller Needs

Classify failures by what the caller can do about them. Translate dependency-specific details at an appropriate boundary while retaining their useful causes.

Do not flatten failures with different recovery actions into one undifferentiated message, or create a new hierarchy when the existing contract already fits. Retry only when the operation's contract permits it.

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/).
