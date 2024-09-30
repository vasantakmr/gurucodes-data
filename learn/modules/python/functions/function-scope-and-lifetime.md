---
title: "Function Scope and Lifetime"
---

## Function Scope and Lifetime

Variables defined inside a function are local to that function and cannot be accessed outside it. This scope ensures that function variables do not interfere with variables in other parts of the code.

### Example:
```python
def local_variable_example():
    x = 10  # Local variable
    print(x)

local_variable_example()
print(x)  # Raises NameError
```

**Output:**
```
10
```

**Error:**
```
NameError: name 'x' is not defined
```

### Real-world Example:
Harsha defines a function that uses local variables:
```python
def calculate_sum():
    a = 5
    b = 7
    total = a + b
    return total

print(calculate_sum())
```

**Output:**
```
12
```

---