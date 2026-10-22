---
title: Use Mappers to Translate Between Layers
impact: MEDIUM
impactDescription: decouples domain from persistence and presentation models
tags: adapt, mapper, translation, layers
---

## Use Mappers to Translate Between Layers

Map at boundaries where representations differ in meaning, access or change reasons. Use explicit output fields to make disclosure review possible; do not duplicate identical models mechanically.

Test the actual serializer to establish the external representation. An allowlist mapper can still leak a sensitive field if its classification is wrong.

Reference: [Data Mapper Pattern](https://martinfowler.com/eaaCatalog/dataMapper.html)

Upstream rule: [adapt-mapper-translation](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/adapt-mapper-translation.md).
