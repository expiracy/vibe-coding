---
title: Avoid Returning and Passing Null
impact: HIGH
impactDescription: makes expected absence explicit to callers
tags: err, null, optional, null-object
---

## Avoid Returning and Passing Null

Returning null creates work for callers and invites errors. One missing null check leads to NullPointerException. Throw exceptions, return empty collections, or use the Special Case / Null Object pattern.

**Incorrect (returning null):**

```java
public List<Employee> getEmployees() {
    if (thereAreNoEmployees) {
        return null;  // Caller must check for null
    }
    return employees;
}

// Every caller must do this
List<Employee> employees = getEmployees();
if (employees != null) {  // Easy to forget
    for (Employee e : employees) {
        pay(e);
    }
}

// Passing null
public double calculatePay(Employee employee, Money bonus) {
    // What if bonus is null?
}
calculatePay(employee, null);  // What does null mean?
```

**Correct (the outcome is explicit to callers):**

```java
// Return empty collection instead of null
public List<Employee> getEmployees() {
    if (thereAreNoEmployees) {
        return Collections.emptyList();
    }
    return employees;
}

// Clean caller code
for (Employee e : getEmployees()) {
    pay(e);
}

// Use Optional for truly optional values
public Optional<Employee> findById(Long id) {
    return Optional.ofNullable(employeeMap.get(id));
}

// Use Special Case object
public interface BillingPlan {
    Money getRate();
}

public class NullBillingPlan implements BillingPlan {
    public Money getRate() {
        return Money.ZERO;
    }
}

// Explicit parameters instead of null
public double calculatePay(Employee employee, Money bonus) { /* ... */ }
public double calculatePayWithoutBonus(Employee employee) { /* ... */ }
```

**When null/nullable is acceptable:**
- Expected absence can be a legitimate part of a documented API. Keep the project's representation and distinguish an empty result from an operational failure.
- Interop with APIs or frameworks that require null (e.g., JDBC, some serialization libraries).

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [err-avoid-null](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/err-avoid-null.md).
