---
title: "Nested Loops"
---

You can have loops inside loops, known as **nested loops**. A `for` or `while` loop can contain another loop inside it.

### Example:
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
```

**Output:**
```
i = 1, j = 1
i = 1, j = 2
i = 1, j = 3
i = 2, j = 1
i = 2, j = 2
i = 2, j = 3
i = 3, j = 1
i = 3, j = 2
i = 3, j = 3
```

### Real-world Example:
Vasanta Kumar wants to combine different types of beverages with different types of snacks:
```python
beverages = ["Tea", "Coffee"]
snacks = ["Cookies", "Cake"]

for beverage in beverages:
    for snack in snacks:
        print(f"Vasanta Kumar can have {beverage} with {snack}.")
```

**Output:**
```
Vasanta Kumar can have Tea with Cookies.
Vasanta Kumar can have Tea with Cake.
Vasanta Kumar can have Coffee with Cookies.
Vasanta Kumar can have Coffee with Cake.
```

---