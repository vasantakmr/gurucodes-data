---
title: "Operator Precedence"
---

## BODMAS

Python follows the **BODMAS** rule (Brackets, Orders, Division/Multiplication, Addition/Subtraction) to determine the order in which operators are evaluated in an expression.

### Example:
```python
result = 10 + 2 * 5 - 3
print(result)
```

**Output:**
```
17
```

In this case, the multiplication (`2 * 5 = 10`) is performed before the addition and subtraction, so the result is `17`.

### Real-world Example:
Praveen is calculating a complex expression:
```python
result = (5 + 2) ** 2 - 8 // 3
print(result)
```

**Output:**
```
45
```

Here:
1. Brackets are evaluated first: `(5 + 2) = 7`
2. Exponentiation: `7 ** 2 = 49`
3. Floor division: `8 // 3 = 2`
4. Subtraction: `49 - 2 = 47`

---

## Few more examples

### Example 1: Using Multiple Operators
```python
a = 15
b = 6
c = a + b * 2 - (a // b)
print(f"Result of complex operation: {c}")
```

**Output:**
```
Result of complex operation: 22
```

### Example 2: Real-world Scenario
```python
# Vasanta Kumar is calculating his earnings after a raise
initial_salary = 50000
raise_percentage = 10
new_salary = initial_salary + (initial_salary * raise_percentage / 100)
print(f"Vasanta Kumar's new salary is: {new_salary}")
```

**Output:**
```
Vasanta Kumar's new salary is: 55000.0
```

---
