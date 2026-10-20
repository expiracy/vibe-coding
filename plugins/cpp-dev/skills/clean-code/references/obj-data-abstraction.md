---
title: Hide Data Behind Abstractions
impact: MEDIUM-HIGH
impactDescription: enables implementation changes without ripple effects
tags: obj, abstraction, encapsulation, data-hiding
---

## Hide Data Behind Abstractions

Objects hide their data behind abstractions and expose functions that operate on that data. Data structures expose their data and have no meaningful functions. Do not mix these concepts.

**Incorrect (exposing implementation):**

```cpp
#include <cmath>

namespace example {
struct Point { double x; double y; };
double distanceFromOrigin(const Point& point) { return std::hypot(point.x, point.y); }
}
```

**Correct (hiding behind abstraction — immutable):**

```cpp
#include <cmath>

namespace example {
class Point {
    double x_;
    double y_;
    Point(double x, double y) : x_(x), y_(y) {}
public:
    static Point fromCartesian(double x, double y) { return Point(x, y); }
    static Point fromPolar(double r, double theta) { return Point(r * std::cos(theta), r * std::sin(theta)); }
    double getX() const { return x_; }
    double getY() const { return y_; }
    double getR() const { return std::hypot(x_, y_); }
};
double distanceFromOrigin(const Point& point) { return point.getR(); }
}
```

**Key insight:** The abstraction is not just about using getters/setters. It is about hiding the form of the data and exposing operations that work with the abstract concept. A clear value and mutability contract can simplify reasoning. A factory or the absence of setters does not by itself guarantee correct behavior or thread safety.

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-data-abstraction](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-data-abstraction.md).
