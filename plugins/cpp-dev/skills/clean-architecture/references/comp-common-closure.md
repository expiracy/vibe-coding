---
title: Group Classes That Change Together
impact: HIGH
impactDescription: localizes change impact, reduces deployment risk
tags: comp, common-closure, cohesion, change
---

## Group Classes That Change Together

Group code that changes for the same business reason. Include the relevant header, implementation and tests in one cohesive capability rather than organizing every file solely by technical kind.

Delivery and persistence adapters can remain separate when they have distinct change reasons. Cohesion is a tradeoff, not a ban on layers.

Reference: [Clean Architecture - Common Closure Principle](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch13.xhtml)

Upstream rule: [comp-common-closure](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/comp-common-closure.md).
