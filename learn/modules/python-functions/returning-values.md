---
title: "Returning Values"
---

Functions can return values using the `return` keyword. If no return statement is present, the function returns `None` by default.

### Syntax:
```python
def function_name(parameters):
    # Function body
    return value
```

### Example:
```python
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)
```

**Output:**
```
20
```

### Real-world Example:
Dodagatta Nihar creates a function to calculate the factorial of a number:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```

**Output:**
```
120
```

---