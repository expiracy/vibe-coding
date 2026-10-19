---
title: "Make Functions Do One Thing"
impact: CRITICAL
impactDescription: "Group work around one coherent responsibility"
tags: clean-code, func
---

## Make Functions Do One Thing

Group work around one coherent responsibility. Separate independent reasons for change, such as calculating a total and choosing how to deliver a receipt.

An orchestration function can coordinate several named operations at one level of abstraction. Do not confuse that coordination with several unrelated responsibilities.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
