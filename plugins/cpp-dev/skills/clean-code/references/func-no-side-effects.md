---
title: Avoid Side Effects
impact: HIGH
impactDescription: prevents hidden temporal couplings
tags: func, side-effects, purity, predictability
---

## Avoid Side Effects

Side effects are lies. Your function promises to do one thing, but it also does other hidden things. Avoid unexpected changes to class variables, globals, or passed arguments.

If you must have a temporal coupling, make it explicit in the function name: `checkPasswordAndInitializeSession`.

**When side effects are expected:**
- I/O operations (file writes, network calls, database mutations) inherently have side effects — the principle here is about *hidden* side effects, not avoiding all mutation. A function named `saveUser()` clearly signals side effects.
- Event handlers, middleware, and lifecycle hooks are designed to produce side effects. Name them to make the effect obvious.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-no-side-effects](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-no-side-effects.md).
