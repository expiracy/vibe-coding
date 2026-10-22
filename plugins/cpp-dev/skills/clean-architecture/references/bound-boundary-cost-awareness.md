---
title: Weigh Boundary Cost Against Ignorance Cost
impact: MEDIUM-HIGH
impactDescription: optimizes architectural investment, prevents both over and under engineering
tags: bound, cost, tradeoffs, pragmatism
---

## Weigh Boundary Cost Against Ignorance Cost

Add a boundary when isolating actual volatility, ownership or difficult external behavior justifies its mapping, maintenance and runtime/build costs. Simple stable code can stay simple.

**Incorrect:**

```cpp
struct AddInput { int a; int b; };
struct Adder { virtual ~Adder() = default; virtual int add(AddInput) = 0; };
struct AdditionUseCase { Adder& adder; int execute(AddInput input) { return adder.add(input); } };
```

**Better for this contract:**

```cpp
// For this bounded teaching domain, direct calculation is adequate.
int total_small_counts(unsigned char a, unsigned char b) { return int(a) + int(b); }
// Introduce a seam separately for a real external dependency or changing policy.
```

Assess independent change, meaningful ownership, real external dependencies and testing difficulty. A small team or a stable component is evidence, not an automatic veto or mandate.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - The Cost of Boundaries](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch25.xhtml)

Upstream rule: [bound-boundary-cost-awareness](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/bound-boundary-cost-awareness.md).
