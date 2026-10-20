---
title: Use DTOs for Data Transfer
impact: MEDIUM
impactDescription: prevents sensitive data exposure at boundaries
tags: obj, dto, transfer, boundary
---

## Use DTOs for Data Transfer

Data Transfer Objects (DTOs) are pure data structures for transferring data between layers or systems. They should have no behavior beyond accessors. Use them at system boundaries.

**Incorrect (domain object used for transfer):**

```java
// Domain object with behavior used for API response
public class User {
    private String name;
    private String hashedPassword;
    private CreditCard creditCard;

    public void authenticate(String password) { /* ... */ }
    public void chargeCard(Money amount) { /* ... */ }

    // Serialized directly - exposes sensitive data and internal structure
}
```

**Correct (separate DTO for transfer):**

```java
// Domain object with behavior (internal)
public class User {
    private String name;
    private HashedPassword password;
    private CreditCard creditCard;

    public void authenticate(String password) { /* ... */ }
    public void chargeCard(Money amount) { /* ... */ }

    public UserDTO toDTO() {
        return new UserDTO(name, creditCard.getMaskedNumber());
    }
}

// DTO for API response (external)
public final class UserDTO {
    private final String name;
    private final String maskedCardNumber;

    public UserDTO(String name, String maskedCardNumber) {
        this.name = name;
        this.maskedCardNumber = maskedCardNumber;
    }

    public String getName() { return name; }
    public String getMaskedCardNumber() { return maskedCardNumber; }
}

// Active Record is a different persistence pattern, not the DTO above.
public class UserRecord {
    public String name;
    public String email;

    public void save() { /* SQL insert/update */ }
    public static UserRecord findById(Long id) { throw new UnsupportedOperationException("supply the project persistence implementation"); }
}
```

**Use DTOs when:**
- Transferring data across system boundaries (API, database, message queue)
- Hiding internal structure from external consumers
- Transforming data format between layers

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-dto](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-dto.md).
