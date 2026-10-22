---
title: Service Boundaries Do Not Replace Internal Design
impact: MEDIUM-HIGH
impactDescription: microservices don't replace architecture, they require it
tags: bound, services, microservices, internal
---

## Service Boundaries Do Not Replace Internal Design

A network boundary does not fix internal coupling. Each C++ service still needs coherent policy and adapter responsibilities; a small service may need only a few functions.

Use a local module unless independent deployment/scale/ownership justifies a service. Remote calls introduce timeouts, compatibility and partial failures absent from an ordinary function call.

Reference: [Clean Architecture - Services: Great and Small](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch27.xhtml)

Upstream rule: [bound-service-internal-architecture](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/bound-service-internal-architecture.md).
