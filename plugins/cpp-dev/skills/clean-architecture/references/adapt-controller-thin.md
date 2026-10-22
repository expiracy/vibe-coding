---
title: Keep Controllers Thin
impact: MEDIUM
impactDescription: simplifies testing, isolates HTTP concerns
tags: adapt, controller, thin, http
---

## Keep Controllers Thin

A delivery adapter parses transport input, invokes an application operation and maps its result/error. Reusable and application business decisions stay outside the transport handler.

**Incorrect:**

```cpp
struct HttpRequest { int quantity; };
struct HttpResponse { int status; };
HttpResponse handle(const HttpRequest& request) {
    // Only the HTTP path enforces this rule.
    return {request.quantity <= 100 ? 200 : 400};
}
```

**Better for this contract:**

```cpp
struct OrderRequest { int quantity; };
bool accepted(const OrderRequest& request) { return request.quantity > 0 && request.quantity <= 100; }
struct HttpRequest { int quantity; };
struct HttpResponse { int status; };
HttpResponse handle(const HttpRequest& request) { return {accepted({request.quantity}) ? 200 : 400}; }
```

The quantity limit is illustrative policy. Authentication, parsing failure and complete HTTP error translation need explicit contracts too.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Controllers](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch22.xhtml)

Upstream rule: [adapt-controller-thin](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/adapt-controller-thin.md).
