---
title: Encapsulate Business Invariants Within Entities
impact: CRITICAL
impactDescription: prevents invalid state, centralizes validation
tags: entity, invariants, validation, encapsulation
---

## Encapsulate Business Invariants Within Entities

Protect meaningful invariants at the domain operation that can violate them. Preserve the project error policy; exceptions here illustrate rejected operations.

**Incorrect:**

```cpp
struct Account { int balance; };
void withdraw(Account& account, int amount) { account.balance -= amount; }
```

**Better for this contract:**

```cpp
#include <stdexcept>
class Account {
    int balance_;
public:
    explicit Account(int balance) : balance_(balance) {
        if (balance < 0) throw std::invalid_argument("negative balance");
    }
    void withdraw(int amount) {
        if (amount < 0 || amount > balance_) throw std::invalid_argument("invalid withdrawal");
        balance_ -= amount;
    }
    int balance() const { return balance_; }
};
```

The example checks the complete subtraction domain. Different currency, overdraft or concurrency rules need their own contracts; encapsulation alone does not supply them.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Domain-Driven Design - Aggregates](https://martinfowler.com/bliki/DDD_Aggregate.html)

Upstream rule: [entity-encapsulate-invariants](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/entity-encapsulate-invariants.md).
