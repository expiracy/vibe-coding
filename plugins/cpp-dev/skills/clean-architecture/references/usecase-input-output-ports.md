---
title: Define Input and Output Ports for Use Cases
impact: HIGH
impactDescription: decouples use cases from delivery mechanism
tags: usecase, ports, input, output, boundaries
---

## Define Input and Output Ports for Use Cases

Express the use case entry point and result using application-owned data. Keep parsing, HTTP status and serialization in delivery adapters.

Use a direct function, callable or class method as appropriate. Explicit data contracts do not imply a separate abstract input interface for every use case.

Reference: [Clean Architecture - Input/Output Ports](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [usecase-input-output-ports](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-input-output-ports.md).
