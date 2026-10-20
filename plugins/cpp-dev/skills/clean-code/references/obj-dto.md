---
title: Use DTOs for Data Transfer
impact: MEDIUM
impactDescription: prevents sensitive data exposure at boundaries
tags: obj, dto, transfer, boundary
---

## Use DTOs for Data Transfer

Data Transfer Objects (DTOs) are pure data structures for transferring data between layers or systems. They should have no behavior beyond accessors. Use them at system boundaries.

**Incorrect (domain object used for transfer):**

```cpp
#include <string>
#include <vector>

namespace example {
struct User {
    std::string name;
    std::string hashedPassword;
    std::string cardNumber;
};
// Directly exposing this object also exposes internal authentication data.
std::vector<std::string> responseFields(const User& user) {
    return {user.name, user.hashedPassword, user.cardNumber};
}
}
```

**Correct (separate DTO for transfer):**

```cpp
#include <string>

namespace example {
struct UserDTO { std::string name; std::string maskedCardNumber; };
class User {
    std::string name_;
    std::string hashedPassword_;
    std::string maskedCardNumber_;
public:
    User(std::string name, std::string passwordHash, std::string maskedCard)
        : name_(name), hashedPassword_(passwordHash), maskedCardNumber_(maskedCard) {}
    UserDTO toDTO() const { return {name_, maskedCardNumber_}; }
};
}
```

**Use DTOs when:**
- Transferring data across system boundaries (API, database, message queue)
- Hiding internal structure from external consumers
- Transforming data format between layers

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-dto](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-dto.md).
