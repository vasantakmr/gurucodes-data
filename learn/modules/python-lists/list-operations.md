---
title: "List Operations"
---

## 1. Creating a List

Lists are created using square brackets `[]`, with items separated by commas.

### Syntax:
```python
my_list = [item1, item2, item3, ...]
```

### Example:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

**Output:**
```
['apple', 'banana', 'cherry']
```

### Real-world Example:
Dodagatta Nihar creates a list of his favorite books:
```python
favorite_books = ["The Alchemist", "1984", "To Kill a Mockingbird"]
print(favorite_books)
```

**Output:**
```
['The Alchemist', '1984', 'To Kill a Mockingbird']
```

---

## 2. Accessing List Items

You can access list items by their index, with the index starting from 0.

### Syntax:
```python
item = my_list[index]
```

### Example:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
```

**Output:**
```
banana
```

### Real-world Example:
Harsha accesses his second favorite movie from a list:
```python
favorite_movies = ["Inception", "The Matrix", "Interstellar"]
print(favorite_movies[1])
```

**Output:**
```
The Matrix
```

---

## 3. Modifying List Items

Lists are mutable, so you can change items by accessing them with their index.

### Syntax:
```python
my_list[index] = new_value
```

### Example:
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)
```

**Output:**
```
['apple', 'blueberry', 'cherry']
```

### Real-world Example:
Vasanta Kumar updates his list of top 3 destinations:
```python
top_destinations = ["Paris", "London", "New York"]
top_destinations[2] = "Tokyo"
print(top_destinations)
```

**Output:**
```
['Paris', 'London', 'Tokyo']
```

---

## 4. Adding Items to a List

You can add items using the `append()`, `extend()`, and `insert()` methods.

### Using `append()`:
Adds an item to the end of the list.
```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)
```

**Output:**
```
['apple', 'banana', 'cherry']
```

### Using `extend()`:
Adds all items from another list to the end of the current list.
```python
fruits = ["apple", "banana"]
more_fruits = ["cherry", "date"]
fruits.extend(more_fruits)
print(fruits)
```

**Output:**
```
['apple', 'banana', 'cherry', 'date']
```

### Using `insert()`:
Inserts an item at a specified index.
```python
fruits = ["apple", "banana"]
fruits.insert(1, "blueberry")
print(fruits)
```

**Output:**
```
['apple', 'blueberry', 'banana']
```

### Real-world Example:
Praveen adds more tasks to his to-do list:
```python
tasks = ["Complete assignment", "Read a book"]
tasks.append("Go for a walk")
print(tasks)
```

**Output:**
```
['Complete assignment', 'Read a book', 'Go for a walk']
```

---

## 5. Removing Items from a List

You can remove items using the `remove()`, `pop()`, and `del` methods.

### Using `remove()`:
Removes the first occurrence of a specified value.
```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
```

**Output:**
```
['apple', 'cherry']
```

### Using `pop()`:
Removes and returns the item at a specified index. If no index is provided, it removes the last item.
```python
fruits = ["apple", "banana", "cherry"]
removed_item = fruits.pop(1)
print(fruits)
print(f"Removed item: {removed_item}")
```

**Output:**
```
['apple', 'cherry']
Removed item: banana
```

### Using `del`:
Deletes an item at a specified index or the entire list.
```python
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)
```

**Output:**
```
['apple', 'cherry']
```

### Real-world Example:
Dodagatta Nihar removes a book from his reading list:
```python
reading_list = ["Book A", "Book B", "Book C"]
reading_list.remove("Book B")
print(reading_list)
```

**Output:**
```
['Book A', 'Book C']
```

---

## 6. Looping Through a List

You can loop through a list using a `for` loop to access each item.

### Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

### Real-world Example:
Harsha prints out each item on his shopping list:
```python
shopping_list = ["milk", "bread", "eggs"]
for item in shopping_list:
    print(f"Harsha needs to buy: {item}")
```

**Output:**
```
Harsha needs to buy: milk
Harsha needs to buy: bread
Harsha needs to buy: eggs
```

---

## 7. List Slicing

List slicing allows you to extract a portion of a list.

### Syntax:
```python
sub_list = my_list[start:end]
```

### Example:
```python
fruits = ["apple", "banana", "cherry", "date"]
sliced_fruits = fruits[1:3]
print(sliced_fruits)
```

**Output:**
```
['banana', 'cherry']
```

### Real-world Example:
Vasanta Kumar views a subset of his favorite movies:
```python
favorite_movies = ["Movie A", "Movie B", "Movie C", "Movie D"]
selected_movies = favorite_movies[1:3]
print(selected_movies)
```

**Output:**
```
['Movie B', 'Movie C']
```

---

## 8. List Comprehensions

List comprehensions provide a concise way to create lists. They consist of an expression followed by a `for` clause and zero or more `if` clauses.

### Syntax:
```python
new_list = [expression for item in iterable if condition]
```

### Example:
```python
squares = [x**2 for x in range(10)]
print(squares)
```

**Output:**
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Real-world Example:
Harsha creates a list of squares for numbers from 1 to 5:
```python
squares = [x**2 for x in range(1, 6)]
print(squares)
```

**Output:**
```
[1, 4, 9, 16, 25]
```

---

## Few more examples

### Example 1: Creating and Modifying a List
```python
colors = ["red", "green", "blue"]
colors.append("yellow")
colors[1] = "purple"
print(colors)
```

**Output:**
```
['red', 'purple', 'blue', 'yellow']
```

### Example 2: Removing and Looping Through a List
```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
cherry
```

### Example 3: Using List Comprehension
```python
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [x * 2 for x in numbers]
print(doubled_numbers)
```

**Output:**
```
[2, 4, 6, 8, 10]
```

---
