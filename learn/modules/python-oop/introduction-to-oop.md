---
title: "Introduction to Object Oriented Programming"
---

Object-Oriented Programming (OOP) is a programming paradigm centered around objects and classes. Python supports OOP, enabling you to create classes that define properties (attributes) and behaviors (methods) that can be instantiated as objects. OOP promotes code reusability, modularity, and a clear organizational structure.

---

## Classes and Objects

### Defining a Class

A class is a blueprint for creating objects. It encapsulates data and methods that operate on that data. 

**Syntax:**
```python
class ClassName:
    def __init__(self, parameters):
        # Constructor method to initialize attributes
        self.attribute = value

    def method_name(self):
        # Method definition
        pass
```

**Example:**
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Buddy", 3)
dog1.bark()  # Output: Buddy says woof!
```

### Creating an Object

An object is an instance of a class. You create an object by calling the class name followed by parentheses.

**Example:**
```python
dog1 = Dog("Buddy", 3)
print(dog1.name)  # Output: Buddy
```

---