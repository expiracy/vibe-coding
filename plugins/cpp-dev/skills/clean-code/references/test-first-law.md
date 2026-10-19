---
title: "Keep Test-First Changes Small"
impact: MEDIUM
impactDescription: "The three laws of TDD limit each step: make a production change in response to a failing test, write only enough new test to expose a failure, and implement only enough to pass"
tags: clean-code, test
---

## Keep Test-First Changes Small

The three laws of TDD limit each step: make a production change in response to a failing test, write only enough new test to expose a failure, and implement only enough to pass. Use small steps to connect a requested behavior to an observable check.

Observe the intended failure, preserve earlier passing behavior, and refactor while checks pass. A broken harness is not a behavioral failure. Describe actual execution results rather than presenting an unrun example as a verified test-first cycle.

Reference: [Clean Code, Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
