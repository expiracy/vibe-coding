---
title: Build Anti-Corruption Layers for External Systems
impact: MEDIUM
impactDescription: protects domain from external model pollution
tags: adapt, anti-corruption, external, isolation
---

## Build Anti-Corruption Layers for External Systems

Translate a vendor model into application concepts at the integration boundary. Reject unsupported values explicitly rather than scattering vendor status codes through domain code.

The vendor is fictional. Verify its real status semantics and schema with contract/integration tests; do not silently assume future statuses mean failure or success.

Reference: [Anti-Corruption Layer Pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer)

Upstream rule: [adapt-anti-corruption-layer](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/adapt-anti-corruption-layer.md).
