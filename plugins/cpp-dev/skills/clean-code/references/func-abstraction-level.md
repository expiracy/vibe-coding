---
title: "Keep a Consistent Level of Abstraction"
impact: CRITICAL
impactDescription: "Let a high-level operation read as a short account of what it does"
tags: clean-code, func
---

## Keep a Consistent Level of Abstraction

Let a high-level operation read as a short account of what it does. Move implementation mechanics into a helper when they obscure that account and the helper expresses a meaningful concept.

Keep closely related simple details local when extraction would add indirection without improving understanding. Abstraction levels are a readability guide, not a ban on useful inline detail.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
