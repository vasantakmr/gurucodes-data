---
title: "Abstraction"
---

Abstraction hides the complex implementation details and shows only the essential features of the object. In Python, abstraction is implemented using abstract classes and methods.

### Abstract Classes

An abstract class cannot be instantiated and typically contains one or more abstract methods that must be implemented by derived classes.

**Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(rect.area())  # Output: 50
```

---