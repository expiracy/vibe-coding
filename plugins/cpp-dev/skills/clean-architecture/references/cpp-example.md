# C++ boundary example

A small online checkout illustrates the dependency rule. This teaching example
uses one product and quantity, integer cents and explicit upper limits to keep
arithmetic in range. A real order needs its own pricing, quantity, currency,
identity, authorization and consistency contracts.

- **Domain:** quantity/price invariants and total calculation.
- **Application:** this channel requires a verified customer; the use case looks
  up the trusted catalog price and saves through application-owned ports.
- **Adapters:** in-memory implementations for an executable illustration.
- **Composition:** `main` wires adapters into the use case. No inner code imports
  the adapter or entry point. Directory names illustrate the dependency graph;
  they are not a required project layout.

This C++20 example uses exceptions and simple ports for clarity; preserve your
project's declared language version and error policy. Include guards, naming and
layout follow local conventions; the dependency direction is the teaching point.

### `domain/order.hpp`

```cpp
#pragma once
#include <cstdint>
#include <stdexcept>

namespace domain {
using Cents = std::int64_t;
class Order {
public:
    Order(int quantity, Cents unitPrice) : quantity_(quantity), unitPrice_(unitPrice) {
        // Illustrative catalog/order limits keep multiplication in range.
        if (quantity < 1 || quantity > 1000000 || unitPrice < 0 || unitPrice > 1000000000)
            throw std::invalid_argument("invalid order quantity or price");
    }
    Cents total() const { return unitPrice_ * quantity_; }
private:
    int quantity_;
    Cents unitPrice_;
};
}
```

### `application/checkout.hpp`

```cpp
#pragma once
#include "domain/order.hpp"
#include <string>

namespace application {
struct CustomerDirectory {
    virtual ~CustomerDirectory() = default;
    virtual bool verified(const std::string& customerId) const = 0;
};
struct ProductCatalog {
    virtual ~ProductCatalog() = default;
    virtual domain::Cents unitPrice(const std::string& productId) const = 0;
};
struct OrderStore {
    virtual ~OrderStore() = default;
    virtual std::string save(const std::string& customerId, const domain::Order& order) = 0;
};
struct CheckoutRequest { std::string customerId; std::string productId; int quantity; };
struct Receipt { std::string orderId; domain::Cents total; };

class Checkout {
public:
    Checkout(const CustomerDirectory& customers, const ProductCatalog& catalog, OrderStore& orders)
        : customers_(customers), catalog_(catalog), orders_(orders) {}
    Receipt execute(const CheckoutRequest& request) {
        // This application's online channel requires a verified customer.
        if (!customers_.verified(request.customerId))
            throw std::runtime_error("customer must be verified for online checkout");
        const domain::Order order(request.quantity, catalog_.unitPrice(request.productId));
        return {orders_.save(request.customerId, order), order.total()};
    }
private:
    const CustomerDirectory& customers_;
    const ProductCatalog& catalog_;
    OrderStore& orders_;
};
}
```

### `adapters/memory.hpp`

```cpp
#pragma once
#include "application/checkout.hpp"

namespace adapters {
class Customers final : public application::CustomerDirectory {
public:
    bool isVerified = true;
    bool verified(const std::string& id) const override { return id == "customer-1" && isVerified; }
};
class Catalog final : public application::ProductCatalog {
public:
    domain::Cents price = 1250;
    domain::Cents unitPrice(const std::string& id) const override {
        if (id != "product-1") throw std::runtime_error("unknown product");
        return price;
    }
};
class Orders final : public application::OrderStore {
public:
    int saves = 0;
    bool failBeforeSave = false;
    domain::Cents savedTotal = 0;
    std::string save(const std::string&, const domain::Order& order) override {
        if (failBeforeSave) throw std::runtime_error("store unavailable before save");
        ++saves;
        savedTotal = order.total();
        return "order-1";
    }
};
}
```

### `main.cpp`

```cpp
#include "adapters/memory.hpp"
#include <iostream>

void check(bool condition) {
    if (!condition) throw std::runtime_error("example check failed");
}
template<class Action> void expectFailure(Action action) {
    bool failed = false;
    try { action(); } catch (const std::exception&) { failed = true; }
    check(failed);
}
int main() {
    adapters::Customers customers;
    adapters::Catalog catalog;
    adapters::Orders orders;
    application::Checkout checkout(customers, catalog, orders);
    const application::CheckoutRequest request{"customer-1", "product-1", 2};
    const auto receipt = checkout.execute(request);
    check(receipt.orderId == "order-1" && receipt.total == 2500);
    check(orders.saves == 1 && orders.savedTotal == 2500);
    customers.isVerified = false;
    expectFailure([&] { checkout.execute(request); });
    check(orders.saves == 1);
    customers.isVerified = true;
    expectFailure([&] { checkout.execute({"customer-1", "product-1", 0}); });
    check(orders.saves == 1);
    catalog.price = -1;
    expectFailure([&] { checkout.execute(request); });
    check(orders.saves == 1);
    catalog.price = 1250;
    orders.failBeforeSave = true;
    expectFailure([&] { checkout.execute(request); });
    check(orders.saves == 1);
    std::cout << "PASS: checkout success and four failure cases\n";
}
```

## Run and interpret the checks

Save the files at the paths above inside a scratch folder. With a compatible
compiler installed, run from that folder:

```sh
c++ -std=c++20 -Wall -Wextra -Werror -I . main.cpp -o checkout
./checkout
```

The checks exercise success, an unverified customer, invalid quantity, invalid
price and a store that fails before saving. They verify the receipt/total and
that rejected operations do not add saved orders in these test doubles. They do
not prove real storage atomicity, concurrent authorization, vendor integration,
retries or payment behavior. No payment is performed here. Production adapters
need separate contract/integration checks; see the
[transaction reference](usecase-transaction-boundary.md) for external effects.
