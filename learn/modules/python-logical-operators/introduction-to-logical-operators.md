---
title: "Introduction to Logical Operators"
---

**Logical operators** in Python are used to combine conditional statements. They evaluate expressions and return a Boolean value (`True` or `False`) based on the logic of the expression.

Python provides three logical operators:

1. **`and`**: Returns `True` if both conditions are true.
2. **`or`**: Returns `True` if at least one of the conditions is true.
3. **`not`**: Inverts the Boolean value of the condition. If the condition is `True`, it becomes `False` and vice versa.

Logical operators are essential when working with decision-making structures like `if`, `elif`, and `else`.

---

## 1. Logical AND (`and`)

The `and` operator returns `True` if **both** operands are true. If one or both operands are false, it returns `False`.

### Example:
```python
x = True
y = True
result = x and y
print(f"x and y: {result}")
```

**Output:**
```
x and y: True
```

### Real-world Example:
Dodagatta Nihar wants to check if both his laptop and phone are charged:
```python
laptop_charged = True
phone_charged = True
ready_for_meeting = laptop_charged and phone_charged
print(f"Is Dodagatta Nihar ready for the meeting? {ready_for_meeting}")
```

**Output:**
```
Is Dodagatta Nihar ready for the meeting? True
```

---

## 2. Logical OR (`or`)

The `or` operator returns `True` if **at least one** of the operands is true. If both operands are false, it returns `False`.

### Example:
```python
x = False
y = True
result = x or y
print(f"x or y: {result}")
```

**Output:**
```
x or y: True
```

### Real-world Example:
Harsha wants to check if he has either a pen or a pencil to take notes:
```python
has_pen = False
has_pencil = True
can_take_notes = has_pen or has_pencil
print(f"Can Harsha take notes? {can_take_notes}")
```

**Output:**
```
Can Harsha take notes? True
```

---

## 3. Logical NOT (`not`)

The `not` operator inverts the Boolean value of an operand. If the operand is `True`, it returns `False`, and if the operand is `False`, it returns `True`.

### Example:
```python
x = True
result = not x
print(f"not x: {result}")
```

**Output:**
```
not x: False
```

### Real-world Example:
Vasanta Kumar checks if he does **not** have any pending tasks:
```python
has_pending_tasks = True
no_tasks = not has_pending_tasks
print(f"Does Vasanta Kumar have no tasks left? {no_tasks}")
```

**Output:**
```
Does Vasanta Kumar have no tasks left? False
```

---