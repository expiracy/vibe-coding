---
title: "Use Clear Data Transfer Records"
impact: MEDIUM
impactDescription: "Use a simple record when the purpose is to carry data across an application boundary"
tags: clean-code, obj
---

## Use Clear Data Transfer Records

Use a simple record when the purpose is to carry data across an application boundary. Keep its fields and validation expectations clear, and translate external representations where they enter the application.

Do not turn a transfer record into a hidden business service. Introduce a separate domain abstraction when behavior or invariants require one, rather than assuming every data structure needs a behavior-rich wrapper.

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/).
