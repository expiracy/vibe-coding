---
title: "Avoid Duplicated Knowledge"
impact: CRITICAL
impactDescription: "Give a business rule or policy one authoritative representation when its uses must change together"
tags: clean-code, func
---

## Avoid Duplicated Knowledge

Give a business rule or policy one authoritative representation when its uses must change together. Distinguish repeated knowledge from code that merely looks similar.

Extract a shared concept only when the relationship is real. Combining unrelated cases behind flags or a speculative abstraction can make future changes harder than a small amount of local repetition.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
