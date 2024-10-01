---
title: "Inheritance"
---

Inheritance allows one class to inherit the attributes and methods of another class. This promotes code reuse.

### Syntax:
```python
class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass
```

**Example:**
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

cat1 = Cat()
cat1.speak()  # Output: Animal speaks
cat1.meow()   # Output: Cat meows
```

---