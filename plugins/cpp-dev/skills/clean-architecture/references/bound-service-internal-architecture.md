---
title: Service Boundaries Do Not Replace Internal Design
impact: MEDIUM-HIGH
impactDescription: microservices don't replace architecture, they require it
tags: bound, services, microservices, internal
---

## Service Boundaries Do Not Replace Internal Design

A network boundary does not fix internal coupling. Each C++ service still needs coherent policy and adapter responsibilities; a small service may need only a few functions.

**Incorrect:**

```cpp
struct HttpRequest { int quantity; };
struct RemoteSqlClient { void insert(int); };
void handler(RemoteSqlClient& sql, const HttpRequest& request) { sql.insert(request.quantity); }
```

**Better for this contract:**

```cpp
#include <stdexcept>
struct Orders { virtual ~Orders() = default; virtual void save(int quantity) = 0; };
void place(Orders& orders, int quantity) {
    if (quantity < 1) throw std::invalid_argument("invalid quantity");
    orders.save(quantity);
}
struct HttpRequest { int quantity; };
void handler(Orders& orders, const HttpRequest& request) { place(orders, request.quantity); }
```

Use a local module unless independent deployment/scale/ownership justifies a service. Remote calls introduce timeouts, compatibility and partial failures absent from an ordinary function call.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Services: Great and Small](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch27.xhtml)

Upstream rule: [bound-service-internal-architecture](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/bound-service-internal-architecture.md).
