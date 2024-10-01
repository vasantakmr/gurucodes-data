---
title: "Recursive Functions"
---

A recursive function is one that calls itself. Recursion is useful for solving problems that can be broken down into smaller, similar problems.

### Example:
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
```

**Output:**
```
8
```

### Real-world Example:
Vasanta Kumar uses recursion to compute the greatest common divisor (GCD):
```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(48, 18))
```

**Output:**
```
6
```

---