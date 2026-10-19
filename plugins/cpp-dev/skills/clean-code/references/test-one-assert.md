---
title: "Test One Concept at a Time"
impact: MEDIUM
impactDescription: "Focus a test on one coherent behavior"
tags: clean-code, test
---

## Test One Concept at a Time

Focus a test on one coherent behavior. Several assertions can describe the result of that behavior; an arbitrary one-assertion limit can duplicate setup and fragment the explanation.

Split unrelated expectations into separate scenarios. For an expensive or irreversible operation, a controlled integration scenario may check several related outcomes without repeating the external effect.

Reference: [Clean Code, Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
