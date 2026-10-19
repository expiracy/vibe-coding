---
title: "Avoid Fragile Horizontal Alignment"
impact: MEDIUM
impactDescription: "Use ordinary consistent spacing rather than padding unrelated declarations or expressions into columns"
tags: clean-code, fmt
---

## Avoid Fragile Horizontal Alignment

Use ordinary consistent spacing rather than padding unrelated declarations or expressions into columns. Alignment that requires distant edits after a rename makes maintenance noisier.

Preserve an established formatter or a genuinely useful tabular representation. Do not turn a focused behavior change into a repository-wide formatting rewrite.

Reference: [Clean Code, Chapter 5: Formatting](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
