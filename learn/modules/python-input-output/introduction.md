---
title: "Input - Output"
---

Input and output (I/O) operations are essential for interacting with users or external files in Python. They allow you to retrieve data (input) from the user or another source and display (output) information in various formats.

Python provides built-in functions to handle both input and output efficiently:

- **Input Function**: `input()` to capture user input.
- **Output Functions**: `print()` to display output on the console.

---

## Python Input

The `input()` function in Python is used to take input from the user. It always returns the user input as a **string**, even if the user provides numerical input. If a different data type (e.g., integer, float) is required, explicit conversion is necessary.

### Syntax:
```python
variable = input(prompt)
```
- **prompt**: A message shown to the user, explaining what input is expected. This is optional, but useful to guide the user.

### Example 1: Simple User Input
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

**Output:**
```
Enter your name: Nihar
Hello, Nihar!
```

In this example, the `input()` function takes a string input from the user and stores it in the `name` variable. Then, the `print()` function displays a message that includes the user's input.

### Example 2: Input as an Integer
```python
age = int(input("Enter your age: "))
print("You will be " + str(age + 1) + " next year.")
```

**Output:**
```
Enter your age: 25
You will be 26 next year.
```

Here, the user input is taken as a string by `input()`, but it is immediately converted into an integer using `int()`. The result is manipulated mathematically and converted back to a string using `str()` for output.

### Example 3: Input as a Float
```python
price = float(input("Enter the price of the item: "))
print("The price with tax is:", price * 1.15)
```

**Output:**
```
Enter the price of the item: 100
The price with tax is: 115.0
```

In this case, the input is converted to a float using `float()`, and the result is used in a mathematical operation.

---

## Python Output

The `print()` function is used to display output on the screen. It can print various types of data, including strings, numbers, lists, dictionaries, and more. By default, `print()` adds a newline at the end of the output, but this behavior can be modified.

### Syntax:
```python
print(value1, value2, ..., sep=' ', end='\n')
```

- **value1, value2, ...**: The values to be printed. Multiple values can be printed, separated by commas.
- **sep**: Optional. Specifies the separator between multiple values. Default is a space (`' '`).
- **end**: Optional. Specifies the string to be appended at the end of the output. Default is a newline (`'\n'`).

### Example 1: Simple Output
```python
print("Hello, World!")
```

**Output:**
```
Hello, World!
```

This basic example prints a simple string.

### Example 2: Printing Multiple Values
```python
x = 10
y = 20
print("x =", x, ", y =", y)
```

**Output:**
```
x = 10 , y = 20
```

Here, the values of variables `x` and `y` are printed along with explanatory text.

### Example 3: Changing the Separator
```python
print("Apple", "Banana", "Cherry", sep=" - ")
```

**Output:**
```
Apple - Banana - Cherry
```

The `sep` parameter changes the default space separator to a hyphen.

### Example 4: Customizing the End of the Print
```python
print("Hello", end=" ")
print("World!")
```

**Output:**
```
Hello World!
```

By using the `end` parameter, the default newline is replaced with a space.
