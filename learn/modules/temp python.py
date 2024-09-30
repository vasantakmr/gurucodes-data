import os 
import json

data ={
  "python-nihar": {
    "title": "Python",
    "description": "like never before :)",
    "slug": "python-nihar",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
      {
        "name": "Introduction to Python",
        "slug": "introduction-to-python",
      },
      {
        "name": "Input - Output",
        "slug": "python-input-output",
      },
      {
        "name": "Variables and Datatypes",
        "slug": "variables-datatypes",
      },
      {
        "name": "Python Syntax",
        "slug": "syntax",
      },
      {
        "name": "Python Strings",
        "slug": "strings",
      },
      {
        "name": "Type Conversion",
        "slug": "type-conversion",
      },
      {
        "name": "Arithmetic Operators",
        "slug": "arithmetic-operators",
      },
      {
        "name": "Relational Operators",
        "slug": "relational-operators",
      },
      {
        "name": "Logical Operators",
        "slug": "logical-operators",
      },
      {
        "name": "Conditional Statements",
        "slug": "conditional-statements",
      },
      {
        "name": "Loops",
        "slug": "loops",
      },
      {
        "name": "Lists",
        "slug": "lists",
      },
      {
        "name": "Tuples",
        "slug": "tuples",
      },
      {
        "name": "Dictionaries",
        "slug": "dictionaries",
      },
      {
        "name": "Sets",
        "slug": "sets",
      },
      {
        "name": "Functions",
        "slug": "functions",
      },
      {
        "name": "Built-in Functions",
        "slug": "built-in-functions",
      },
      {
        "name": "Object Oriented Programming",
        "slug": "oop",
      },
    ],
  },
  "python-introduction-to-python": {
    "title": "Introduction to Python",
    "description": "A beginner's guide to understanding Python and its foundational concepts.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-introduction-to-python",
    "chapters": [
      {
        "name": "Basic Introduction",
        "slug": "basic-introduction"
      },
      {
        "name": "History of Python",
        "slug": "history-of-python"
      },
      {
        "name": "Python vs Other Programming Languages",
        "slug": "python-vs-other"
      },
    ]
  },
  "python-input-output": {
    "title": "Input - Output",
    "description": "lets print and read stuff :)",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-input-output",
    "chapters": [
      {
        "name": "Introduction",
        "slug": "introduction"
      },
      {
        "name": "Examples",
        "slug": "examples"
      },
    ]
  },
  "python-variables-datatypes": {
    "title": "Variables and Datatypes",
    "description": "Learn about Python variables and data types, a crucial part of programming.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-variables-datatypes",
    "chapters": [
      {
        "name": "variables",
        "slug": "variables"
      },
      {
        "name": "Data Types",
        "slug": "datatypes"
      },
    ]
  },
  "python-syntax": {
    "title": "Python Syntax",
    "description": "An overview of Python syntax and how to write your first programs.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-syntax",
    "chapters": [
      {
        "name": "Syntax Rules and Order of Instructions",
        "slug": "basic-syntax"
      },
      {
        "name": "BODMAS Rule",
        "slug": "bodmas"
      },
    ]
  },
  "python-strings": {
    "title": "Python Strings",
    "description": "Explore Python strings and how to manipulate text in your programs.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-strings",
    "chapters": [
      {
        "name": "Introduction to Strings",
        "slug": "intro-to-strings"
      },
      {
        "name": "String Operations",
        "slug": "string-operations"
      },
    ]
  },
  "python-type-conversion": {
    "title": "Type Conversion",
    "description": "Learn how to convert between different data types in Python.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-type-conversion",
    "chapters": [
      {
        "name": "Introduction to Type Conversion",
        "slug": "intro-to-type-conversion"
      },
      {
        "name": "Common Type Conversion Functions",
        "slug": "common-type-conversion-functions"
      },
    ]
  },
  "python-arithmetic-operators": {
    "title": "Arithmetic Operators",
    "description": "Understand how arithmetic operators work in Python for basic mathematical operations.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-arithmetic-operators",
    "chapters": [
      {
        "name": "Introduction to Arithmetic Operators",
        "slug": "introduction-to-arithmetic-operators"
      },
      {
        "name": "Operator Precedence",
        "slug": "operator-precedence"
      },
    ]
  },
  "python-relational-operators": {
    "title": "Relational Operators",
    "description": "Explore relational operators in Python, used for comparing values.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-relational-operators",
    "chapters": [
      {
        "name": "Introduction to Relational Operators",
        "slug": "introduction-to-relational-operators"
      },
      {
        "name": "Examples",
        "slug": "examples"
      },
    ]
  },
  "python-logical-operators": {
    "title": "Logical Operators",
    "description": "Learn about logical operators in Python and how to implement logical conditions.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-logical-operators",
    "chapters": [
      {
        "name": "Introduction to Logical Operators",
        "slug": "introduction-to-logical-operators"
      },
      {
        "name": "Combining Logical Operators",
        "slug": "combining-logical-operators"
      },
      {
        "name": "Examples",
        "slug": "examples"
      },
    ]
  },
  "python-conditional-statements": {
    "title": "Conditional Statements",
    "description": "Master Python's conditional statements, including if, else, and elif.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-conditional-statements",
    "chapters": [
      {
        "name": "Introduction to Conditional Statements",
        "slug": "introduction-to-conditional-statements"
      },
      {
        "name": "if Conditional Statement",
        "slug": "if-conditional-statement"
      },
      {
        "name": "if - else Conditional Statement",
        "slug": "if-else-conditional-statement"
      },
      {
        "name": "elif Conditional Statement",
        "slug": "elif-conditional-statement"
      },
      {
        "name": "Nested Conditional Statements",
        "slug": "nested-conditional-statements"
      },
      {
        "name": "Examples",
        "slug": "examples"
      },
    ]
  },
  "python-loops": {
    "title": "Loops",
    "description": "Master loops in Python, including 'for' and 'while' loops.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-loops",
    "chapters": [
      {
        "name": "Introduction to Loops",
        "slug": "introduction-to-loops"
      },
      {
        "name": "While Loop",
        "slug": "while-loop"
      },
      {
        "name": "For Loop",
        "slug": "for-loop"
      },
      {
        "name": "Nested Loops",
        "slug": "nested-loops"
      },
      {
        "name": "Control Flow Statements",
        "slug": "control-flow-statements"
      },
    ]
  },
  "python-lists": {
    "title": "Lists",
    "description": "Learn how to create, manipulate, and work with lists in Python.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-lists",
    "chapters": [
      {
        "name": "Introduction to Lists",
        "slug": "introduction-to-lists"
      },
      {
        "name": "List Operations",
        "slug": "list-operations"
      },
    ]
  },
  "python-tuples": {
    "title": "Tuples",
    "description": "Explore tuples in Python, an immutable data type often used for grouping data.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-tuples",
    "chapters": [
      {
        "name": "Introduction to Tuples",
        "slug": "introduction-to-tuples"
      },
      {
        "name": "Tuple Operations",
        "slug": "tuple-operations"
      },
    ]
  },
  "python-dictionaries": {
    "title": "Dictionaries",
    "description": "Learn about Python dictionaries, a powerful data structure for storing key-value pairs.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-dictionaries",
    "chapters": [
      {
        "name": "Introduction to Dictionaries",
        "slug": "introduction-to-dictionaries"
      },
      {
        "name": "Dictionary Opeartions",
        "slug": "dictionary-operations"
      },
      {
        "name": "*args **kwargs",
        "slug": "args-kwargs"
      },
    ]
  },
  "python-sets": {
    "title": "Sets",
    "description": "Understand how to work with sets in Python, a collection type that ensures unique elements.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-sets",
    "chapters": [
      {
        "name": "Introduction to Sets",
        "slug": "introduction-to-sets"
      },
      {
        "name": "Set Operations",
        "slug": "set-operations"
      },
    ]
  },
  "python-functions": {
    "title": "Functions",
    "description": "Understand how to define and call functions in Python to create reusable code.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-functions",
    "chapters": [
      {
        "name": "Introduction to Functions",
        "slug": "introduction-to-functions"
      },
      {
        "name": "Returning Values",
        "slug": "returning-values"
      },
      {
        "name": "Function Scope and Lifetime",
        "slug": "function-scope-and-lifetime"
      },
      {
        "name": "Recursive Functions",
        "slug": "recursive-functions"
      },
      {
        "name": "Lambda Functions",
        "slug": "lambda-functions"
      },
    ]
  },
  "python-built-in-functions": {
    "title": "Built-in Functions",
    "description": "Learn about Python’s built-in functions, which provide powerful capabilities right out of the box.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-built-in-functions",
    "chapters": [
      {
        "name": "Mathemetical Functions",
        "slug": "mathematical-functions"
      },
      {
        "name": "Data Type Conversions",
        "slug": "data-type-conversions"
      },
      {
        "name": "Sequence Operations",
        "slug": "sequence-operations"
      },
      {
        "name": "Miscellaneous",
        "slug": "miscellaneous"
      }
    ]
  },
  "python-oop": {
    "title": "Object Oriented Programming",
    "description": "Dive into Python’s object-oriented programming paradigm to learn about classes, objects, inheritance, and more.",
    "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
    "slug": "python-oop",
    "chapters": [
      {
        "name": "Introduction to Object Oriented Programming",
        "slug": "introduction-to-oop"
      },
      {
        "name": "Attributes and Methods",
        "slug": "attributes-and-methods"
      },
      {
        "name": "Inheritance",
        "slug": "inheritance"
      },
      {
        "name": "Encapsulation",
        "slug": "encapsulation"
      },
      {
        "name": "Polymorphism",
        "slug": "polymorphism"
      },
      {
        "name": "Abstraction",
        "slug": "abstraction"
      },
      {
        "name": "Examples",
        "slug": "examples"
      },
    ]
  },
}
  
def create_folders_and_files(data):
    for folder_name, folder_data in data.items():
        # Create the folder based on the key
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created.")
       
        # Iterate through chapters and create files
        chapters = folder_data.get("chapters", [])
        for chapter in chapters:
            file_name = f"{chapter['slug']}.md"
            file_path = os.path.join(folder_name, file_name)
           
            # Create and write to the file with the required format
            with open(file_path, "w") as file:
                file_content = f"---\ntitle: \"{chapter['name']}\"\n---\n"  # Frontmatter format
                file.write(file_content)
                print(f"File '{file_name}' created in folder '{folder_name}'.")

# Call the function to execute the folder and file creation
create_folders_and_files(data)
