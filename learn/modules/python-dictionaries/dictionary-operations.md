---
title: "Dictionary Opeartions"
---

## 1. Creating a Dictionary

Dictionaries are created using curly braces `{}` with key-value pairs separated by colons `:` and items separated by commas.

### Syntax:
```python
my_dict = {key1: value1, key2: value2, key3: value3, ...}
```

### Example:
```python
person = {"name": "John", "age": 30, "city": "New York"}
print(person)
```

**Output:**
```
{'name': 'John', 'age': 30, 'city': 'New York'}
```

### Real-world Example:
Dodagatta Nihar creates a dictionary to store information about his favorite books:
```python
favorite_books = {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988}
print(favorite_books)
```

**Output:**
```
{'title': 'The Alchemist', 'author': 'Paulo Coelho', 'year': 1988}
```

---

## 2. Accessing Dictionary Values

You can access the value associated with a specific key by using square brackets `[]` or the `get()` method.

### Syntax:
```python
value = my_dict[key]
```

### Example:
```python
person = {"name": "John", "age": 30, "city": "New York"}
print(person["age"])
```

**Output:**
```
30
```

### Real-world Example:
Harsha accesses the year of publication for a book:
```python
book_info = {"title": "1984", "author": "George Orwell", "year": 1949}
print(book_info["year"])
```

**Output:**
```
1949
```

---

## 3. Adding and Updating Items

You can add new key-value pairs or update existing ones using square brackets `[]`.

### Syntax:
```python
my_dict[key] = value
```

### Example:
```python
person = {"name": "John", "age": 30}
person["city"] = "New York"  # Adding a new key-value pair
person["age"] = 31           # Updating an existing value
print(person)
```

**Output:**
```
{'name': 'John', 'age': 31, 'city': 'New York'}
```

### Real-world Example:
Vasanta Kumar updates his contact information:
```python
contact_info = {"email": "vasanta@example.com", "phone": "123-456-7890"}
contact_info["phone"] = "987-654-3210"  # Updating phone number
contact_info["address"] = "123 Elm St"  # Adding address
print(contact_info)
```

**Output:**
```
{'email': 'vasanta@example.com', 'phone': '987-654-3210', 'address': '123 Elm St'}
```

---

## 4. Removing Items

You can remove items using the `del` statement, the `pop()` method, or the `popitem()` method.

### Using `del`:
Removes a key-value pair by key.
```python
person = {"name": "John", "age": 30, "city": "New York"}
del person["city"]
print(person)
```

**Output:**
```
{'name': 'John', 'age': 30}
```

### Using `pop()`:
Removes and returns the value for the specified key.
```python
person = {"name": "John", "age": 30, "city": "New York"}
age = person.pop("age")
print(person)
print(f"Removed age: {age}")
```

**Output:**
```
{'name': 'John', 'city': 'New York'}
Removed age: 30
```

### Using `popitem()`:
Removes and returns the last key-value pair as a tuple.
```python
person = {"name": "John", "age": 30, "city": "New York"}
last_item = person.popitem()
print(person)
print(f"Removed item: {last_item}")
```

**Output:**
```
{'name': 'John', 'age': 30}
Removed item: ('city', 'New York')
```

### Real-world Example:
Praveen removes an entry from his inventory:
```python
inventory = {"item1": 50, "item2": 100, "item3": 200}
removed_item = inventory.pop("item2")
print(inventory)
print(f"Removed item2 quantity: {removed_item}")
```

**Output:**
```
{'item1': 50, 'item3': 200}
Removed item2 quantity: 100
```

---

## 5. Looping Through a Dictionary

You can loop through dictionaries using loops to access keys, values, or key-value pairs.

### Looping through keys:
```python
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key)
```

**Output:**
```
name
age
city
```

### Looping through values:
```python
person = {"name": "John", "age": 30, "city": "New York"}
for value in person.values():
    print(value)
```

**Output:**
```
John
30
New York
```

### Looping through key-value pairs:
```python
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
```

**Output:**
```
name: John
age: 30
city: New York
```

### Real-world Example:
Dodagatta Nihar prints details of his favorite authors:
```python
authors = {"Paulo Coelho": "The Alchemist", "George Orwell": "1984", "J.K. Rowling": "Harry Potter"}
for author, book in authors.items():
    print(f"Author: {author}, Book: {book}")
```

**Output:**
```
Author: Paulo Coelho, Book: The Alchemist
Author: George Orwell, Book: 1984
Author: J.K. Rowling, Book: Harry Potter
```

---

## 6. Dictionary Methods

Dictionaries have several built-in methods, including `copy()`, `clear()`, `get()`, and `update()`.

### Using `copy()`:
Returns a shallow copy of the dictionary.
```python
person = {"name": "John", "age": 30}
copy_person = person.copy()
print(copy_person)
```

**Output:**
```
{'name': 'John', 'age': 30}
```

### Using `clear()`:
Removes all items from the dictionary.
```python
person = {"name": "John", "age": 30}
person.clear()
print(person)
```

**Output:**
```
{}
```

### Using `get()`:
Returns the value for the specified key if it exists, or a default value if it doesn’t.
```python
person = {"name": "John", "age": 30}
print(person.get("name"))
print(person.get("city", "Unknown"))
```

**Output:**
```
John
Unknown
```

### Using `update()`:
Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
```python
person = {"name": "John", "age": 30}
person.update({"city": "New York", "job": "Engineer"})
print(person)
```

**Output:**
```
{'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
```

### Real-world Example:
Harsha updates his contact details:
```python
contact_info = {"email": "harsha@example.com", "phone": "123-456-7890"}
contact_info.update({"phone": "098-765-4321", "address": "456 Elm St"})
print(contact_info)
```

**Output:**
```
{'email': 'harsha@example.com', 'phone': '098-765-4321', 'address': '456 Elm St'}
```

---

## Few more examples

### Example 1: Creating and Accessing a Dictionary
```python
student = {"name": "Alice", "age": 22, "major": "Computer Science"}
print(student["name"])
```

**Output:**
```
Alice
```

### Example 2: Adding and Removing Items
```python
student = {"name": "Alice", "age": 22}
student["graduated"] = True
del student["age"]
print(student)
```

**Output:**
```
{'name': 'Alice', 'gradu

ated': True}
```

### Example 3: Looping Through a Dictionary
```python
student = {"name": "Alice", "age": 22, "major": "Computer Science"}
for key, value in student.items():
    print(f"{key}: {value}")
```

**Output:**
```
name: Alice
age: 22
major: Computer Science
```

---