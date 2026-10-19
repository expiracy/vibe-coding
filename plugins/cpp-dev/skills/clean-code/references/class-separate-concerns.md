---
title: "Separate Construction from Use"
impact: MEDIUM
impactDescription: "Choose and assemble configurable external dependencies at an application boundary, then supply them to the behavior that uses them"
tags: clean-code, class
---

## Separate Construction from Use

Choose and assemble configurable external dependencies at an application boundary, then supply them to the behavior that uses them. The main operation should not repeatedly decide which infrastructure to construct.

Keep ordinary local values near their use. Moving all construction into a framework or factory adds complexity unless configuration, substitution, or a real separate responsibility calls for it.

Reference: [Clean Code, Chapter 11: Systems](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
