---
title: Abstract Logging Behind Domain Interfaces
impact: MEDIUM
impactDescription: prevents logging framework coupling, enables structured logging
tags: frame, logging, abstraction, cross-cutting
---

## Abstract Logging Behind Domain Interfaces

Keep vendor logging types out of policy headers. If an application needs observable audit/diagnostic behavior, define that contract where consumed; do not add a logger to every entity.

**Incorrect:**

```cpp
namespace vendor { void log_order_created(int); }
void order_created(int id) { vendor::log_order_created(id); }
```

**Better for this contract:**

```cpp
struct OrderEvents { virtual ~OrderEvents() = default; virtual void created(int id) = 0; };
void order_created(OrderEvents& events, int id) { events.created(id); }
namespace vendor { void log_order_created(int); }
struct LogEvents final : OrderEvents { void created(int id) override { vendor::log_order_created(id); } };
```

Diagnostic logging is not a durable audit trail. Define failure, sensitive-data handling and durability separately when the product requires auditing.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Frameworks are Details](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [frame-logging-abstraction](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/frame-logging-abstraction.md).
