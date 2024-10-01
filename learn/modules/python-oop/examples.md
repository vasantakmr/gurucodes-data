---
title: "Examples"
---

### Example 1: Class and Object
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car: {self.make} {self.model}")

car1 = Car("Toyota", "Corolla")
car1.display_info()  # Output: Car: Toyota Corolla
```

### Example 2: Inheritance and Method Overriding
```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

penguin = Penguin()
penguin.fly()  # Output: Penguin cannot fly
```

### Example 3: Encapsulation
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(500)
account.deposit(200)
print(account.get_balance())  # Output: 700
```

### Example 4: Polymorphism
```python
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Rectangle(5, 10), Square(4)]
for shape in shapes:
    print(shape.area())
```

**Output:**
```
50
16
```

---
