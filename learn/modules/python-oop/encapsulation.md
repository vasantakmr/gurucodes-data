---
title: "Encapsulation"
---

Encapsulation refers to bundling data (attributes) and methods that operate on the data into a single unit, i.e., a class. It also involves restricting direct access to some attributes.

### Private Attributes

Private attributes are not accessible from outside the class. They are indicated by a double underscore prefix.

**Example:**
```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

acc = Account(1000)
print(acc.get_balance())  # Output: 1000
print(acc.__balance)     # AttributeError: 'Account' object has no attribute '__balance'
```

---