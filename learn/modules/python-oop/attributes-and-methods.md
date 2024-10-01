---
title: "Attributes and Methods"
---

### Instance Attributes

Attributes are variables that belong to an object. They are defined within the `__init__` method.

**Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Harsha", 25)
print(person1.name)  # Output: Harsha
```

### Methods

Methods are functions defined within a class. They operate on the attributes of the class.

**Example:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Vasanta Kumar", 30)
person1.greet()  # Output: Hello, my name is Vasanta Kumar and I am 30 years old.
```

---