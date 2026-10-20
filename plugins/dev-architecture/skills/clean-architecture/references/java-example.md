# Java boundary example

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

Read the other language's [equivalent example](cpp-example.md)
only when comparing implementations. These examples use exceptions and simple
ports for clarity; preserve your project's language version and error policy.

### `domain/Order.java`

```java
package domain;

public final class Order {
    private final int quantity;
    private final long unitPrice;
    public Order(int quantity, long unitPrice) {
        // Illustrative catalog/order limits keep multiplication in range.
        if (quantity < 1 || quantity > 1_000_000 || unitPrice < 0 || unitPrice > 1_000_000_000L)
            throw new IllegalArgumentException("invalid order quantity or price");
        this.quantity = quantity;
        this.unitPrice = unitPrice;
    }
    public long total() { return unitPrice * quantity; }
}
```

### `application/Checkout.java`

```java
package application;

import domain.Order;

public final class Checkout {
    public interface CustomerDirectory { boolean verified(String customerId); }
    public interface ProductCatalog { long unitPrice(String productId); }
    public interface OrderStore { String save(String customerId, Order order); }
    public static final class Request {
        public final String customerId;
        public final String productId;
        public final int quantity;
        public Request(String customerId, String productId, int quantity) {
            this.customerId = customerId;
            this.productId = productId;
            this.quantity = quantity;
        }
    }
    public static final class Receipt {
        public final String orderId;
        public final long total;
        public Receipt(String orderId, long total) { this.orderId = orderId; this.total = total; }
    }
    private final CustomerDirectory customers;
    private final ProductCatalog catalog;
    private final OrderStore orders;
    public Checkout(CustomerDirectory customers, ProductCatalog catalog, OrderStore orders) {
        this.customers = customers;
        this.catalog = catalog;
        this.orders = orders;
    }
    public Receipt execute(Request request) {
        // This application's online channel requires a verified customer.
        if (!customers.verified(request.customerId))
            throw new IllegalStateException("customer must be verified for online checkout");
        Order order = new Order(request.quantity, catalog.unitPrice(request.productId));
        return new Receipt(orders.save(request.customerId, order), order.total());
    }
}
```

### `adapters/Memory.java`

```java
package adapters;

import application.Checkout;
import domain.Order;

public final class Memory {
    private Memory() {}
    public static final class Customers implements Checkout.CustomerDirectory {
        public boolean isVerified = true;
        @Override public boolean verified(String id) { return "customer-1".equals(id) && isVerified; }
    }
    public static final class Catalog implements Checkout.ProductCatalog {
        public long price = 1250;
        @Override public long unitPrice(String id) {
            if (!"product-1".equals(id)) throw new IllegalArgumentException("unknown product");
            return price;
        }
    }
    public static final class Orders implements Checkout.OrderStore {
        public int saves;
        public boolean failBeforeSave;
        public long savedTotal;
        @Override public String save(String customerId, Order order) {
            if (failBeforeSave) throw new IllegalStateException("store unavailable before save");
            saves++;
            savedTotal = order.total();
            return "order-1";
        }
    }
}
```

### `Main.java`

```java
import adapters.Memory;
import application.Checkout;

public final class Main {
    private Main() {}
    private static void check(boolean condition) {
        if (!condition) throw new IllegalStateException("example check failed");
    }
    private static void expectFailure(Runnable action) {
        boolean failed = false;
        try { action.run(); } catch (RuntimeException ex) { failed = true; }
        check(failed);
    }
    public static void main(String[] args) {
        Memory.Customers customers = new Memory.Customers();
        Memory.Catalog catalog = new Memory.Catalog();
        Memory.Orders orders = new Memory.Orders();
        Checkout checkout = new Checkout(customers, catalog, orders);
        Checkout.Request request = new Checkout.Request("customer-1", "product-1", 2);
        Checkout.Receipt receipt = checkout.execute(request);
        check(receipt.orderId.equals("order-1") && receipt.total == 2500);
        check(orders.saves == 1 && orders.savedTotal == 2500);
        customers.isVerified = false;
        expectFailure(() -> checkout.execute(request));
        check(orders.saves == 1);
        customers.isVerified = true;
        expectFailure(() -> checkout.execute(new Checkout.Request("customer-1", "product-1", 0)));
        check(orders.saves == 1);
        catalog.price = -1;
        expectFailure(() -> checkout.execute(request));
        check(orders.saves == 1);
        catalog.price = 1250;
        orders.failBeforeSave = true;
        expectFailure(() -> checkout.execute(request));
        check(orders.saves == 1);
        System.out.println("PASS: checkout success and four failure cases");
    }
}
```

## Run and interpret the checks

Save the files at the paths above inside a scratch folder. With a compatible
compiler installed, run from that folder:

```sh
javac --release 11 -Xlint:all -Werror -d build domain/Order.java application/Checkout.java adapters/Memory.java Main.java
java -cp build Main
```

The checks exercise success, an unverified customer, invalid quantity, invalid
price and a store that fails before saving. They verify the receipt/total and
that rejected operations do not add saved orders in these test doubles. They do
not prove real storage atomicity, concurrent authorization, vendor integration,
retries or payment behavior. No payment is performed here. Production adapters
need separate contract/integration checks; see the
[transaction reference](usecase-transaction-boundary.md) for external effects.
