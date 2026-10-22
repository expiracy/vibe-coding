---
title: Each Use Case Has One Reason to Change
impact: HIGH
impactDescription: isolates change impact, enables parallel development
tags: usecase, single-responsibility, cohesion, srp
---

## Each Use Case Has One Reason to Change

Give each application workflow a coherent reason to change. Split unrelated workflows where their policies or dependencies differ; a function can be a use case.

**Incorrect:**

```cpp
struct Orders {
    void place(int);
    void refund(int);
    void print_monthly_report();
};
```

**Better for this contract:**

```cpp
struct PlaceOrder { void execute(int product_id); };
struct RefundOrder { void execute(int order_id); };
struct MonthlyReport { void execute(); };
```

Splitting every method into a class is not required. Keep operations together when they form one cohesive contract and change for the same reason.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Use Cases](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [usecase-single-responsibility](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-single-responsibility.md).
