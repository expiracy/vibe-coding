---
title: Understand Data/Object Anti-Symmetry
impact: MEDIUM-HIGH
impactDescription: clarifies data and behavior boundaries
tags: obj, asymmetry, procedural, polymorphism
---

## Understand Data/Object Anti-Symmetry

Objects and data structures are opposites. Objects hide data and expose behavior; data structures expose data and have no behavior. Choose based on what kind of changes you anticipate.

**Incorrect (wrong approach for frequent type additions):**

```cpp
#include <stdexcept>

namespace example {
struct Shape { enum class Kind { circle, rectangle }; Kind kind; double a; double b; };
double area(const Shape& shape) {
    switch (shape.kind) {
    case Shape::Kind::circle: return 3.141592653589793 * shape.a * shape.a;
    case Shape::Kind::rectangle: return shape.a * shape.b;
    }
    throw std::invalid_argument("unknown shape");
}
}
```

**Correct (polymorphic approach for frequent type additions):**

```cpp

namespace example {
struct Shape {
    virtual double area() const = 0;
    virtual ~Shape() = default;
};
struct Circle : Shape {
    double radius;
    explicit Circle(double r) : radius(r) {}
    double area() const override { return 3.141592653589793 * radius * radius; }
};
struct Rectangle : Shape {
    double width;
    double height;
    Rectangle(double w, double h) : width(w), height(h) {}
    double area() const override { return width * height; }
};
double area(const Shape& shape) { return shape.area(); }
}
```

**Choose based on anticipated changes:**
- Adding new functions often? Use data structures (procedural)
- Adding new types often? Use objects (polymorphic)

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-data-object-asymmetry](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-data-object-asymmetry.md).
