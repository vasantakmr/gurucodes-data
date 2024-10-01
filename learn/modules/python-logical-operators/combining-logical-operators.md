---
title: "Combining Logical Operators"
---

You can combine multiple logical operators to evaluate more complex conditions.

### Example:
```python
x = 10
y = 5
z = 15
result = (x > y) and (z > x)
print(f"Is x greater than y and z greater than x? {result}")
```

**Output:**
```
Is x greater than y and z greater than x? True
```

### Real-world Example:
Praveen checks if both his project is completed and he has enough time for review:
```python
project_completed = True
time_for_review = False
can_proceed = project_completed and time_for_review
print(f"Can Praveen proceed with submission? {can_proceed}")
```

**Output:**
```
Can Praveen proceed with submission? False
```

---