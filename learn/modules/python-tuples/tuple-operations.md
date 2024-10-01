---
title: "Tuple Operations"
---

## 1. Creating a Tuple

Tuples are created using parentheses `()` with items separated by commas.

### Syntax:
```python
my_tuple = (item1, item2, item3, ...)
```

### Example:
```python
fruits = ("apple", "banana", "cherry")
print(fruits)
```

**Output:**
```
('apple', 'banana', 'cherry')
```

### Real-world Example:
Dodagatta Nihar creates a tuple of his favorite colors:
```python
favorite_colors = ("blue", "green", "red")
print(favorite_colors)
```

**Output:**
```
('blue', 'green', 'red')
```

---

## 2. Accessing Tuple Items

You can access items in a tuple by their index, with the index starting from 0.

### Syntax:
```python
item = my_tuple[index]
```

### Example:
```python
fruits = ("apple", "banana", "cherry")
print(fruits[1])
```

**Output:**
```
banana
```

### Real-world Example:
Harsha accesses his second favorite city from a tuple:
```python
favorite_cities = ("New York", "London", "Tokyo")
print(favorite_cities[1])
```

**Output:**
```
London
```

---

## 3. Tuple Unpacking

Tuple unpacking allows you to assign the elements of a tuple to multiple variables.

### Syntax:
```python
var1, var2, var3 = my_tuple
```

### Example:
```python
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)
```

**Output:**
```
10 20 30
```

### Real-world Example:
Vasanta Kumar unpacks a tuple of his top 3 favorite movies:
```python
top_movies = ("Inception", "The Matrix", "Interstellar")
movie1, movie2, movie3 = top_movies
print(movie1)
print(movie2)
print(movie3)
```

**Output:**
```
Inception
The Matrix
Interstellar
```

---

## 4. Immutable Nature of Tuples

Since tuples are immutable, you cannot change, add, or remove elements once they are created.

### Example:
```python
fruits = ("apple", "banana", "cherry")
# Attempting to change an element will raise an error
# fruits[1] = "blueberry"  # This will raise a TypeError
```

### Real-world Example:
Praveen realizes that tuples are immutable while trying to update his tuple of favorite songs:
```python
favorite_songs = ("Song A", "Song B", "Song C")
# Attempting to update the tuple will raise an error
# favorite_songs[1] = "Song D"  # This will raise a TypeError
```

---

## 5. Tuple Methods

Tuples have only two built-in methods:

- **`count(value)`**: Returns the number of times a specified value appears in the tuple.
- **`index(value)`**: Returns the index of the first occurrence of a specified value.

### Example:
```python
numbers = (1, 2, 3, 2, 1)
print(numbers.count(1))  # Output: 2
print(numbers.index(3))  # Output: 2
```

### Real-world Example:
Dodagatta Nihar uses tuple methods to analyze his favorite numbers:
```python
favorite_numbers = (7, 8, 9, 7, 5)
print(favorite_numbers.count(7))  # Output: 2
print(favorite_numbers.index(9))  # Output: 2
```

**Output:**
```
2
2
```

---

## 6. Nested Tuples

Tuples can contain other tuples, allowing for nested structures.

### Example:
```python
nested_tuple = ((1, 2, 3), (4, 5, 6))
print(nested_tuple)
```

**Output:**
```
((1, 2, 3), (4, 5, 6))
```

### Real-world Example:
Harsha organizes his daily schedule into nested tuples:
```python
daily_schedule = (("Morning", "Breakfast"), ("Afternoon", "Work"), ("Evening", "Relax"))
for period, activity in daily_schedule:
    print(f"During the {period}, Harsha will {activity}.")
```

**Output:**
```
During the Morning, Harsha will Breakfast.
During the Afternoon, Harsha will Work.
During the Evening, Harsha will Relax.
```

---

## 7. Tuple Concatenation and Repetition

Tuples can be concatenated and repeated using the `+` and `*` operators.

### Example:
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
repeated_tuple = tuple1 * 2
print(concatenated_tuple)
print(repeated_tuple)
```

**Output:**
```
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 1, 2, 3)
```

### Real-world Example:
Vasanta Kumar combines and repeats tuples of his favorite items:
```python
fruits = ("apple", "banana")
vegetables = ("carrot", "broccoli")
combined = fruits + vegetables
repeated_fruits = fruits * 3
print(combined)
print(repeated_fruits)
```

**Output:**
```
('apple', 'banana', 'carrot', 'broccoli')
('apple', 'banana', 'apple', 'banana', 'apple', 'banana')
```

---

## Few more examples

### Example 1: Creating and Accessing a Tuple
```python
colors = ("red", "green", "blue")
print(colors[0])
```

**Output:**
```
red
```

### Example 2: Tuple Unpacking
```python
person = ("John", 25, "Engineer")
name, age, profession = person
print(name)
print(age)
print(profession)
```

**Output:**
```
John
25
Engineer
```

### Example 3: Tuple Methods
```python
numbers = (4, 5, 6, 4, 6, 4)
print(numbers.count(4))
print(numbers.index(6))
```

**Output:**
```
3
4
```

---
