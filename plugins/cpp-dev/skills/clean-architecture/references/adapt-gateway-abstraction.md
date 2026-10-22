---
title: Gateways Hide External System Details
impact: MEDIUM
impactDescription: enables vendor switching, simplifies testing
tags: adapt, gateway, external, abstraction
---

## Gateways Hide External System Details

Expose the external capability the application actually needs through its own contract. Keep vendor request types and protocol details in the adapter.

Represent accepted, rejected and uncertain outcomes where the external capability can produce them. Remote refunds and local saves are not atomic; define idempotency, retention and recovery explicitly.

Reference: [Clean Architecture - Database Gateways](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch22.xhtml)

Upstream rule: [adapt-gateway-abstraction](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/adapt-gateway-abstraction.md).
