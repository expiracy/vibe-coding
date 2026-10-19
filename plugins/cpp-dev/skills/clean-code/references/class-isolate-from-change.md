---
title: "Isolate Volatile Dependencies"
impact: MEDIUM
impactDescription: "Keep application decisions independent of changing infrastructure details"
tags: clean-code, class
---

## Isolate Volatile Dependencies

Keep application decisions independent of changing infrastructure details. Supply the operation or dependency that policy needs instead of making it select an external implementation internally.

Choose the smallest useful seam for the current requirement. Validate outcomes rather than merely checking interactions with the seam, unless those interactions are themselves the required behavior.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
