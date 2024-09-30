---
title: "Introduction to Arithmetic Operators"
---

## Introduction

**Arithmetic operators** in Python are used to perform mathematical operations such as addition, subtraction, multiplication, and division. Python supports the following arithmetic operators:

1. **Addition (`+`)**
2. **Subtraction (`-`)**
3. **Multiplication (`*`)**
4. **Division (`/`)**
5. **Floor Division (`//`)**
6. **Modulus (`%`)**
7. **Exponentiation (`**`)**

Each operator performs a specific mathematical operation and is often used in expressions.

---

## 1. Addition (`+`)

The `+` operator adds two numbers.

### Example:
```python
x = 10
y = 5
result = x + y
print(f"Sum of {x} and {y}: {result}")
```

**Output:**
```
Sum of 10 and 5: 15
```

In this example, `10 + 5` results in `15`.

### Real-world Example:
Dodagatta Nihar wants to combine the scores from two games:
```python
game1_score = 85
game2_score = 92
total_score = game1_score + game2_score
print(f"Total score: {total_score}")
```

**Output:**
```
Total score: 177
```

---

## 2. Subtraction (`-`)

The `-` operator subtracts one number from another.

### Example:
```python
x = 20
y = 8
result = x - y
print(f"Difference between {x} and {y}: {result}")
```

**Output:**
```
Difference between 20 and 8: 12
```

### Real-world Example:
Harsha is calculating how many more points he needs to reach his goal:
```python
goal = 100
current_points = 78
points_needed = goal - current_points
print(f"Harsha needs {points_needed} more points to reach his goal.")
```

**Output:**
```
Harsha needs 22 more points to reach his goal.
```

---

## 3. Multiplication (`*`)

The `*` operator multiplies two numbers.

### Example:
```python
x = 7
y = 6
result = x * y
print(f"Product of {x} and {y}: {result}")
```

**Output:**
```
Product of 7 and 6: 42
```

### Real-world Example:
Vasanta Kumar wants to calculate the total cost of 5 books, each priced at 200:
```python
book_price = 200
number_of_books = 5
total_cost = book_price * number_of_books
print(f"Total cost of books: {total_cost}")
```

**Output:**
```
Total cost of books: 1000
```

---

## 4. Division (`/`)

The `/` operator divides one number by another and returns a floating-point result.

### Example:
```python
x = 20
y = 4
result = x / y
print(f"Division of {x} by {y}: {result}")
```

**Output:**
```
Division of 20 by 4: 5.0
```

### Real-world Example:
Praveen divides his total earnings of 5000 between himself and 4 friends:
```python
total_earnings = 5000
number_of_friends = 4
share_per_person = total_earnings / number_of_friends
print(f"Each person gets: {share_per_person}")
```

**Output:**
```
Each person gets: 1250.0
```

---

## 5. Floor Division (`//`)

The `//` operator divides one number by another and returns the integer (whole number) part of the division, effectively rounding down.

### Example:
```python
x = 17
y = 3
result = x // y
print(f"Floor division of {x} by {y}: {result}")
```

**Output:**
```
Floor division of 17 by 3: 5
```

### Real-world Example:
Dodagatta Nihar wants to distribute 25 apples evenly among 4 people, and he needs to know how many each will get:
```python
total_apples = 25
people = 4
apples_per_person = total_apples // people
print(f"Each person gets {apples_per_person} apples.")
```

**Output:**
```
Each person gets 6 apples.
```

---

## 6. Modulus (`%`)

The `%` operator returns the remainder of the division of one number by another.

### Example:
```python
x = 20
y = 6
result = x % y
print(f"Remainder of {x} divided by {y}: {result}")
```

**Output:**
```
Remainder of 20 divided by 6: 2
```

### Real-world Example:
Harsha is distributing candy and needs to know how many are left after giving an equal number to his 5 friends:
```python
total_candies = 23
friends = 5
leftover_candies = total_candies % friends
print(f"Harsha has {leftover_candies} candies left over.")
```

**Output:**
```
Harsha has 3 candies left over.
```

---

## 7. Exponentiation (`**`)

The `**` operator raises one number to the power of another.

### Example:
```python
x = 3
y = 4
result = x ** y
print(f"{x} raised to the power of {y}: {result}")
```

**Output:**
```
3 raised to the power of 4: 81
```

### Real-world Example:
Vasanta Kumar wants to calculate the square of 7:
```python
number = 7
square = number ** 2
print(f"The square of {number} is {square}.")
```

**Output:**
```
The square of 7 is 49.
```

---