---
title: "Introduction to Relational Operators"
---

**Relational operators** (also known as comparison operators) are used in Python to compare two values. The result of a relational operation is a Boolean value: either `True` or `False`.

The six relational operators in Python are:

1. **Equal to (`==`)**
2. **Not equal to (`!=`)**
3. **Greater than (`>`)**
4. **Less than (`<`)**
5. **Greater than or equal to (`>=`)**
6. **Less than or equal to (`<=`)**

These operators are frequently used in conditional statements and loops.

---

## 1. Equal to (`==`)

The `==` operator checks if two values are equal. If they are, it returns `True`, otherwise it returns `False`.

### Example:
```python
x = 10
y = 10
result = x == y
print(f"Is {x} equal to {y}? {result}")
```

**Output:**
```
Is 10 equal to 10? True
```

### Real-world Example:
Dodagatta Nihar checks if his age is the same as Harsha’s:
```python
age_nihar = 30
age_harsha = 30
same_age = age_nihar == age_harsha
print(f"Do Dodagatta Nihar and Harsha have the same age? {same_age}")
```

**Output:**
```
Do Dodagatta Nihar and Harsha have the same age? True
```

---

## 2. Not equal to (`!=`)

The `!=` operator checks if two values are not equal. If they are not equal, it returns `True`, otherwise it returns `False`.

### Example:
```python
x = 10
y = 5
result = x != y
print(f"Is {x} not equal to {y}? {result}")
```

**Output:**
```
Is 10 not equal to 5? True
```

### Real-world Example:
Vasanta Kumar checks if the price of two items is different:
```python
item1_price = 150
item2_price = 200
different_price = item1_price != item2_price
print(f"Are the prices of the two items different? {different_price}")
```

**Output:**
```
Are the prices of the two items different? True
```

---

## 3. Greater than (`>`)

The `>` operator checks if the left operand is greater than the right operand. If it is, the result is `True`, otherwise it’s `False`.

### Example:
```python
x = 20
y = 15
result = x > y
print(f"Is {x} greater than {y}? {result}")
```

**Output:**
```
Is 20 greater than 15? True
```

### Real-world Example:
Harsha checks if his score is higher than Praveen’s:
```python
score_harsha = 95
score_praveen = 89
higher_score = score_harsha > score_praveen
print(f"Does Harsha have a higher score than Praveen? {higher_score}")
```

**Output:**
```
Does Harsha have a higher score than Praveen? True
```

---

## 4. Less than (`<`)

The `<` operator checks if the left operand is less than the right operand. If it is, it returns `True`, otherwise it returns `False`.

### Example:
```python
x = 8
y = 12
result = x < y
print(f"Is {x} less than {y}? {result}")
```

**Output:**
```
Is 8 less than 12? True
```

### Real-world Example:
Dodagatta Nihar checks if the temperature today is lower than yesterday:
```python
temp_today = 28
temp_yesterday = 32
cooler_today = temp_today < temp_yesterday
print(f"Is today cooler than yesterday? {cooler_today}")
```

**Output:**
```
Is today cooler than yesterday? True
```

---

## 5. Greater than or equal to (`>=`)

The `>=` operator checks if the left operand is greater than or equal to the right operand. If it is, it returns `True`, otherwise it returns `False`.

### Example:
```python
x = 25
y = 25
result = x >= y
print(f"Is {x} greater than or equal to {y}? {result}")
```

**Output:**
```
Is 25 greater than or equal to 25? True
```

### Real-world Example:
Praveen checks if the number of books he has is enough to give each of his 5 friends:
```python
total_books = 5
friends = 5
enough_books = total_books >= friends
print(f"Does Praveen have enough books for his friends? {enough_books}")
```

**Output:**
```
Does Praveen have enough books for his friends? True
```

---

## 6. Less than or equal to (`<=`)

The `<=` operator checks if the left operand is less than or equal to the right operand. If it is, it returns `True`, otherwise it returns `False`.

### Example:
```python
x = 15
y = 20
result = x <= y
print(f"Is {x} less than or equal to {y}? {result}")
```

**Output:**
```
Is 15 less than or equal to 20? True
```

### Real-world Example:
Vasanta Kumar checks if the number of pages he has read is less than or equal to the total number of pages in the book:
```python
pages_read = 150
total_pages = 300
on_track = pages_read <= total_pages
print(f"Has Vasanta Kumar read less than or equal to the total number of pages? {on_track}")
```

**Output:**
```
Has Vasanta Kumar read less than or equal to the total number of pages? True
```

---