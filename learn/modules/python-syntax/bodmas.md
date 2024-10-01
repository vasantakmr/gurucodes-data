---
title: "BODMAS Rule"
---

Python follows the **BODMAS** (Brackets, Orders, Division/Multiplication, Addition/Subtraction) rule to evaluate mathematical expressions. This rule defines the order in which operations should be performed in an arithmetic expression.

- **B**: Brackets `()` (Parentheses)
- **O**: Orders (Exponentiation, `**`)
- **D**: Division `/`, Floor Division `//`
- **M**: Multiplication `*`, Modulus `%`
- **A**: Addition `+`
- **S**: Subtraction `-`

### BODMAS in Action:
1. **Brackets**: Operations inside parentheses are performed first.
2. **Orders**: Exponents (powers and roots) are evaluated next.
3. **Division and Multiplication**: Performed from left to right.
4. **Addition and Subtraction**: Performed last, from left to right.

---

## Example of BODMAS Rule in Python

### Example 1: Simple Arithmetic Expression
```python
result = 10 + 2 * 5
print(result)
```
**Output:**
```
20
```
Here, multiplication (`2 * 5 = 10`) is performed before addition (`10 + 10 = 20`), following BODMAS.

### Example 2: Using Brackets
```python
result = (10 + 2) * 5
print(result)
```
**Output:**
```
60
```
In this case, parentheses force the addition (`10 + 2 = 12`) to happen first, followed by multiplication (`12 * 5 = 60`).

### Example 3: Mixed Operations
```python
result = 100 - 5**2 + (10 / 2)
print(result)
```
**Output:**
```
78.0
```
- **Exponent**: `5**2 = 25`
- **Division**: `10 / 2 = 5.0`
- **Subtraction and Addition**: `100 - 25 + 5 = 80`

### Example 4: More Complex Expression
```python
result = 20 + 3 * (2**3 - 1) / 2
print(result)
```
**Output:**
```
32.0
```
Here’s how the expression is evaluated step by step:
- **Exponent**: `2**3 = 8`
- **Parentheses**: `8 - 1 = 7`
- **Multiplication and Division**: `3 * 7 / 2 = 10.5`
- **Addition**: `20 + 10.5 = 32.5`

---
