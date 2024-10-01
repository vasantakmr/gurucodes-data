---
title: "Polymorphism"
---

Polymorphism allows methods to do different things based on the object it is acting upon. It enables objects of different classes to be treated as objects of a common superclass.

### Method Overriding

Derived classes can override methods from the base class.

**Example:**
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()
```

**Output:**
```
Dog barks
Cat meows
```

---