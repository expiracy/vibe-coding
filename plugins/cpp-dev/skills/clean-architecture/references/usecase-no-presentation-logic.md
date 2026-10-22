---
title: Use Cases Must Not Contain Presentation Logic
impact: HIGH
impactDescription: enables multiple UI implementations from same use case
tags: usecase, presentation, formatting, separation
---

## Use Cases Must Not Contain Presentation Logic

Return application data from the use case. Keep locale, labels, markup and view-specific visibility in the presenter unless formatting is itself the requested business capability.

Currency display, locale and escaping rules belong to an explicit presentation contract.

Reference: [Clean Architecture - Presenters](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch23.xhtml)

Upstream rule: [usecase-no-presentation-logic](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-no-presentation-logic.md).
