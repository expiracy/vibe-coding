---
title: "Provide Context with Errors"
impact: HIGH
impactDescription: "An error should identify the attempted operation and enough safe context to diagnose the failure"
tags: clean-code, err
---

## Provide Context with Errors

An error should identify the attempted operation and enough safe context to diagnose the failure. Preserve its original cause and useful category rather than replacing it with a vague message.

Do not include credentials, secrets, or unnecessary personal data in diagnostics. Adding context does not replace handling the failure or preserving the operation's contract.

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/).
