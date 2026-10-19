---
title: "Use Build-Operate-Check"
impact: MEDIUM
impactDescription: "Arrange a readable test around constructing the relevant scenario, invoking the behavior, and checking the observable result"
tags: clean-code, test
---

## Use Build-Operate-Check

Arrange a readable test around constructing the relevant scenario, invoking the behavior, and checking the observable result. Keep those phases easy to distinguish.

Use the existing framework and helpers where they clarify the case. Do not introduce a custom test language or assertion machinery when ordinary checks already tell the story.

Reference: [Clean Code, Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
