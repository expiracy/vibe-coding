---
title: Define Exceptions by Caller Needs
impact: HIGH
impactDescription: makes success and failure contracts understandable
tags: err, wrapper, classification, design
---

## Define Exceptions by Caller Needs

Define exception classes based on how they are caught, not on their source or type. Often a single exception class is sufficient for a particular area of code. Wrap third-party API exceptions.

**Benefits of wrapping:**
- Minimizes dependencies on third-party APIs
- Easier to mock for testing
- Easier to switch implementations later
- Single exception type per area simplifies catching

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [err-define-by-caller-needs](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/err-define-by-caller-needs.md).
