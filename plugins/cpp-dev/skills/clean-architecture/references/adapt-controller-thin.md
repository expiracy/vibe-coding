---
title: Keep Controllers Thin
impact: MEDIUM
impactDescription: simplifies testing, isolates HTTP concerns
tags: adapt, controller, thin, http
---

## Keep Controllers Thin

A delivery adapter parses transport input, invokes an application operation and maps its result/error. Reusable and application business decisions stay outside the transport handler.

Give authentication, parsing failures and HTTP error translation explicit contracts too.

Reference: [Clean Architecture - Controllers](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch22.xhtml)

Upstream rule: [adapt-controller-thin](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/adapt-controller-thin.md).
