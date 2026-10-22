---
title: Use Verb Phrases for Method Names
impact: MEDIUM-HIGH
impactDescription: makes domain meaning easier to identify
tags: name, method, verb, action
---

## Use Verb Phrases for Method Names

Method names should be verbs or verb phrases. Methods do things, so their names should say what they do.

Use consistent operation and predicate names within the existing interface.

Follow the C++ project's established naming conventions. Query names such as
`size()` or `name()` can be idiomatic; the goal is to make an operation's meaning
clear, not to mandate accessor prefixes.

Reference: [Clean Code, Chapter 2: Meaningful Names](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [name-method-verb](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/name-method-verb.md).
