---
title: "Set Operations"
---

## 1. Creating a Set

Sets are created using curly braces `{}` or the `set()` constructor.

### Syntax:
```python
my_set = {item1, item2, item3, ...}
# or
my_set = set([item1, item2, item3, ...])
```

### Example:
```python
fruits = {"apple", "banana", "cherry"}
print(fruits)
```

**Output:**
```
{'apple', 'banana', 'cherry'}
```

### Real-world Example:
Dodagatta Nihar creates a set of his favorite hobbies:
```python
hobbies = {"reading", "cycling", "painting"}
print(hobbies)
```

**Output:**
```
{'painting', 'reading', 'cycling'}
```

---

## 2. Accessing Set Items

Sets do not support indexing or slicing, so you cannot access items by position. However, you can check for membership using the `in` keyword and iterate through a set.

### Syntax:
```python
item in my_set
```

### Example:
```python
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)
```

**Output:**
```
True
```

### Real-world Example:
Harsha checks if a specific color is in his set of favorite colors:
```python
favorite_colors = {"blue", "green", "red"}
print("blue" in favorite_colors)
```

**Output:**
```
True
```

---

## 3. Adding and Removing Items

You can add items to a set using the `add()` method and remove items using the `remove()` or `discard()` methods. The `remove()` method raises an error if the item is not found, while `discard()` does not.

### Adding Items:
```python
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)
```

**Output:**
```
{'apple', 'banana', 'cherry'}
```

### Removing Items:
```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
```

**Output:**
```
{'apple', 'cherry'}
```

### Using `discard()`:
```python
fruits = {"apple", "banana", "cherry"}
fruits.discard("orange")  # No error even if "orange" is not in the set
print(fruits)
```

**Output:**
```
{'apple', 'banana', 'cherry'}
```

### Real-world Example:
Vasanta Kumar adds and removes items from a set of his favorite movies:
```python
movies = {"Inception", "Interstellar", "The Matrix"}
movies.add("Tenet")
movies.remove("The Matrix")
print(movies)
```

**Output:**
```
{'Inception', 'Tenet', 'Interstellar'}
```

---

## 4. Set Operations

Sets support several mathematical operations, such as union, intersection, difference, and symmetric difference.

### Union:
Combines all unique elements from both sets.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)
```

**Output:**
```
{1, 2, 3, 4, 5}
```

### Intersection:
Returns elements that are present in both sets.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)
```

**Output:**
```
{3}
```

### Difference:
Returns elements that are in the first set but not in the second set.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print(difference_set)
```

**Output:**
```
{1, 2}
```

### Symmetric Difference:
Returns elements that are in either of the sets, but not in both.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)
```

**Output:**
```
{1, 2, 4, 5}
```

### Real-world Example:
Praveen performs set operations with his collection of books:
```python
collection1 = {"Book A", "Book B", "Book C"}
collection2 = {"Book C", "Book D", "Book E"}

# Union
all_books = collection1 | collection2
print("All Books:", all_books)

# Intersection
common_books = collection1 & collection2
print("Common Books:", common_books)

# Difference
unique_books = collection1 - collection2
print("Unique to Collection 1:", unique_books)

# Symmetric Difference
exclusive_books = collection1 ^ collection2
print("Exclusive Books:", exclusive_books)
```

**Output:**
```
All Books: {'Book A', 'Book B', 'Book D', 'Book E', 'Book C'}
Common Books: {'Book C'}
Unique to Collection 1: {'Book A', 'Book B'}
Exclusive Books: {'Book A', 'Book B', 'Book D', 'Book E'}
```

---

## 5. Set Methods

Sets have several useful methods for modifying and querying their contents, such as `copy()`, `clear()`, and `pop()`.

### Using `copy()`:
Returns a shallow copy of the set.
```python
fruits = {"apple", "banana", "cherry"}
fruits_copy = fruits.copy()
print(fruits_copy)
```

**Output:**
```
{'apple', 'banana', 'cherry'}
```

### Using `clear()`:
Removes all elements from the set.
```python
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
```

**Output:**
```
set()
```

### Using `pop()`:
Removes and returns a random element from the set. Raises a `KeyError` if the set is empty.
```python
fruits = {"apple", "banana", "cherry"}
popped_item = fruits.pop()
print(f"Removed item: {popped_item}")
print(fruits)
```

**Output:**
```
Removed item: apple
{'banana', 'cherry'}
```

### Real-world Example:
Harsha uses set methods to manage his collection of tech gadgets:
```python
gadgets = {"Smartphone", "Laptop", "Tablet"}
gadgets_copy = gadgets.copy()
gadgets.clear()
print("Original Gadgets:", gadgets_copy)
print("Cleared Gadgets:", gadgets)
```

**Output:**
```
Original Gadgets: {'Smartphone', 'Laptop', 'Tablet'}
Cleared Gadgets: set()
```

---

## Few more examples

### Example 1: Creating and Accessing a Set
```python
numbers = {1, 2, 3, 4, 5}
print(numbers)
print(3 in numbers)
```

**Output:**
```
{1, 2, 3, 4, 5}
True
```

### Example 2: Adding and Removing Items
```python
numbers = {1, 2, 3}
numbers.add(4)
numbers.remove(2)
print(numbers)
```

**Output:**
```
{1, 3, 4}
```

### Example 3: Set Operations
```python
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)
```

**Output:**
```
Union: {1, 2, 3, 4, 5}
Intersection: {3}
Difference: {1, 2}
Symmetric Difference: {1, 2, 4, 5}
```

---
