---
title: Keep ORM Usage in Infrastructure Layer
impact: MEDIUM
impactDescription: isolates persistence complexity, enables ORM switching
tags: frame, orm, infrastructure, persistence
---

## Keep ORM Usage in Infrastructure Layer

Keep ORM queries, sessions and persistence mappings in the storage adapter. The application names the data capability it needs without accepting an ORM session.

**Incorrect:**

```cpp
namespace orm { struct Session { int query_credit(int); }; }
int customer_credit(orm::Session& session, int id) { return session.query_credit(id); }
```

**Better for this contract:**

```cpp
struct Customers { virtual ~Customers() = default; virtual int credit(int id) = 0; };
namespace orm { struct Session { int query_credit(int); }; }
struct SqlCustomers final : Customers {
    orm::Session& session;
    explicit SqlCustomers(orm::Session& value) : session(value) {}
    int credit(int id) override { return session.query_credit(id); }
};
int customer_credit(Customers& customers, int id) { return customers.credit(id); }
```

The session API is fictional. Test actual mappings, nullability, transaction scope and connection behavior against the chosen storage implementation.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)

Upstream rule: [frame-orm-in-infrastructure](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/frame-orm-in-infrastructure.md).
