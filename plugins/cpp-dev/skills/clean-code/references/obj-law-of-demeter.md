---
title: "Respect Useful Object Boundaries"
impact: MEDIUM-HIGH
impactDescription: "Ask an object to perform a meaningful operation instead of making every caller navigate its changing internals"
tags: clean-code, obj
---

## Respect Useful Object Boundaries

Ask an object to perform a meaningful operation instead of making every caller navigate its changing internals. Place a domain rule with the concept responsible for it.

Counting dots is not a design test: a plain data record or a fluent interface may legitimately expose several steps. Do not add chains of forwarding methods that merely conceal the same dependency.

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/).
