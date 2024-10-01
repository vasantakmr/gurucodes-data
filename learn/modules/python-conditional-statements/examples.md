---
title: "Examples"
---

## `if`, `elif`, `else` with Multiple Conditions

Python allows combining multiple conditions using **logical operators** (`and`, `or`, `not`) to form complex conditional statements.

### Example:
```python
x = 10
y = 5
if x > 5 and y < 10:
    print("x is greater than 5 and y is less than 10")
```

**Output:**
```
x is greater than 5 and y is less than 10
```

### Real-world Example:
Dodagatta Nihar checks if both his laptop is charged and the internet is working before starting a meeting:
```python
laptop_charged = True
internet_working = False

if laptop_charged and internet_working:
    print("Dodagatta Nihar can start the meeting.")
else:
    print("Dodagatta Nihar cannot start the meeting.")
```

**Output:**
```
Dodagatta Nihar cannot start the meeting.
```

---

## Few more examples

### Example 1: Checking Grades
Dodagatta Nihar checks the grade based on his marks:
```python
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
else:
    print("Grade: C")
```

**Output:**
```
Grade: B
```

### Example 2: Nested Condition for Vacation Plans
Vasanta Kumar checks both his vacation days and budget to plan his trip:
```python
vacation_days = 5
budget = 15000

if vacation_days >= 7:
    if budget >= 20000:
        print("Vasanta Kumar will go on an international trip.")
    else:
        print("Vasanta Kumar will go on a domestic trip.")
else:
    print("Vasanta Kumar will go on a short weekend getaway.")
```

**Output:**
```
Vasanta Kumar will go on a short weekend getaway.
```

### Example 3: Using `elif` and `else`
Harsha checks his work progress:
```python
tasks_completed = 8

if tasks_completed == 10:
    print("Harsha has completed all tasks.")
elif tasks_completed >= 5:
    print("Harsha has completed more than half of the tasks.")
else:
    print("Harsha needs to complete more tasks.")
```

**Output:**
```
Harsha has completed more than half of the tasks.
```

---
