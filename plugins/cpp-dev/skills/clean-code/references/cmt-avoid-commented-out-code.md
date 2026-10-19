---
title: "Delete Obsolete Commented-Out Code"
impact: HIGH
impactDescription: "Remove abandoned executable code from maintained source once its purpose is understood"
tags: clean-code, cmt
---

## Delete Obsolete Commented-Out Code

Remove abandoned executable code from maintained source once its purpose is understood. Version control preserves committed history; inactive alternatives obscure the current implementation.

Distinguish obsolete code from a useful usage example, required compatibility path, or meaningful rationale. Preserve required notices, and represent a still-supported alternative through the project's actual configuration mechanism.

Reference: [Clean Code, Chapter 4: Comments](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
