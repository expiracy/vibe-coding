---
title: Web Framework Concerns Stay in Interface Layer
impact: MEDIUM
impactDescription: enables delivery mechanism substitution
tags: frame, web, http, interface
---

## Web Framework Concerns Stay in Interface Layer

Keep HTTP status, request/session objects and routing out of application contracts. An HTTP adapter, CLI or queue consumer should be able to invoke the same relevant policy.

Preserve the actual authentication, transport and error contracts when adapting an existing endpoint.

Reference: [Clean Architecture - The Web is a Detail](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch31.xhtml)

Upstream rule: [frame-web-in-infrastructure](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/frame-web-in-infrastructure.md).
