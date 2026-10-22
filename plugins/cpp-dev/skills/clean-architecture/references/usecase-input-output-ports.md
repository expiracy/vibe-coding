---
title: Define Input and Output Ports for Use Cases
impact: HIGH
impactDescription: decouples use cases from delivery mechanism
tags: usecase, ports, input, output, boundaries
---

## Define Input and Output Ports for Use Cases

Express the use case entry point and result using application-owned data. Keep parsing, HTTP status and serialization in delivery adapters.

**Incorrect:**

```cpp
namespace http { struct Request { int quantity; }; struct Response { int status; }; }
http::Response checkout(const http::Request& request) { return {request.quantity > 0 ? 200 : 400}; }
```

**Better for this contract:**

```cpp
struct CheckoutRequest { int product_id; int quantity; };
struct CheckoutResult { int order_id; };
CheckoutResult checkout(const CheckoutRequest& request);
namespace cli {
CheckoutResult run(int product_id, int quantity) { return checkout({product_id, quantity}); }
}
```

Use a direct function, callable or class method as appropriate. Explicit data contracts do not imply a separate abstract input interface for every use case.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Input/Output Ports](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [usecase-input-output-ports](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-input-output-ports.md).
