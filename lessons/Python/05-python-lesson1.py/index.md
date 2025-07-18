---
layout: default
title: DevSecOps lessons
---

# Python Lesson 1 - Complete Guide

## Table of Contents
1. [Introduction to Python](#introduction-to-python)
2. [Python History](#python-history)
3. [PyCharm Setup](#pycharm-setup)
4. [Interpreter vs Compiler](#interpreter-vs-compiler)
5. [Running Python Code](#running-python-code)
6. [File Extensions](#file-extensions)
7. [Data Types in Python](#data-types-in-python)
8. [Variables and Memory Management](#variables-and-memory-management)
9. [Variable Naming Conventions](#variable-naming-conventions)
10. [Casting (Type Conversion)](#casting-type-conversion)
11. [Truthy and Falsy Values](#truthy-and-falsy-values)
12. [Print Function](#print-function)
13. [Input Function](#input-function)
14. [String Operations](#string-operations)
15. [F-Strings](#f-strings)
16. [Garbage Collection](#garbage-collection)

---

## Introduction to Python

Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used in web development, data science, automation, and DevOps.

**Key Features:**
- Easy to learn and use
- Interpreted language
- Dynamic typing
- Extensive standard library
- Cross-platform compatibility

---

## Python History

- **Created by:** Guido van Rossum
- **First release:** 1991
- **Named after:** Monty Python's Flying Circus
- **Philosophy:** "There should be one obvious way to do it"
- **Current major versions:** Python 3.x (Python 2.x is deprecated)

---

## PyCharm Setup

### How to Create a New Project in PyCharm

1. **Open PyCharm**
2. **Create New Project:**
   - Click "New Project" on the welcome screen
   - OR File → New Project
3. **Configure Project:**
   - Choose project location
   - Select Python interpreter
   - Choose project type (Pure Python for beginners)
4. **Click "Create"**
5. **Create Python file:**
   - Right-click on project folder
   - New → Python File
   - Name your file (e.g., `main.py`)

---

## Interpreter vs Compiler

### Interpreter
- **Python uses an interpreter**
- Executes code line by line
- No separate compilation step
- Slower execution but faster development cycle
- Errors are found at runtime

### Compiler
- Translates entire source code to machine code before execution
- Creates executable files
- Faster execution but slower development cycle
- Errors are found at compile time
- Examples: C, C++, Rust

---

## Running Python Code

### From Terminal/Command Line

```bash
# Navigate to your file location
cd /path/to/your/file

# Run Python file
python filename.py
# OR
python3 filename.py

# Interactive Python shell
python
# OR
python3
```

### From PyCharm
- Click the green play button
- OR press `Ctrl + Shift + F10`
- OR right-click and select "Run"

---

## File Extensions

- **`.py`** - Standard Python source file
- **`.pyw`** - Python script for Windows (runs without console)
- **`.pyc`** - Compiled Python bytecode
- **`.pyo`** - Optimized bytecode (older Python versions)

---

## Data Types in Python

### Numbers

#### Integer (int)
```python
age = 25
year = 2025
negative_number = -10
```

#### Float
```python
price = 19.99
temperature = -2.5
scientific = 1.5e2  # 150.0
```

#### Complex
```python
complex_num = 3 + 4j
another_complex = complex(2, 3)  # 2 + 3j
```

### Strings (str)

#### Different Ways to Create Strings
```python
# Single quotes
name = 'John'
sentence = 'He said "Hello"'

# Double quotes
message = "Welcome to Python"
quote = "She said 'Hi'"

# Triple quotes (multiline)
paragraph = '''This is a 
multiline string
that spans multiple lines'''

# Triple double quotes
text = """Another way to create
multiline strings"""
```

### Boolean (bool)
```python
is_student = True
is_graduated = False
```

### Checking Data Types
```python
print(type(25))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type('hello'))   # <class 'str'>
print(type(True))      # <class 'bool'>
```

---

## Variables and Memory Management

### Variable Declaration and Assignment
```python
# Simple assignment
x = 10
name = "Alice"

# Multiple assignment
x, y, z = 1, 2, 3

# Same value to multiple variables
a = b = c = 0
```

### Stack vs Heap Memory

#### Stack Memory
- Stores variable names and references
- Fast access
- Limited size
- Automatic memory management

#### Heap Memory
- Stores actual object data
- Slower access than stack
- Large memory space
- Managed by Python's garbage collector

```
Stack          Heap
┌─────────┐   ┌─────────────┐
│ x   ────┼──→│ 10          │
├─────────┤   ├─────────────┤
│ name ───┼──→│ "Alice"     │
├─────────┤   ├─────────────┤
│ y   ────┼──→│ [1, 2, 3]   │
└─────────┘   └─────────────┘
```

---

## Variable Naming Conventions

### Allowed Variable Names
```python
# Valid names
age = 25
first_name = "John"
_private = "hidden"
number2 = 42
camelCase = "valid but not recommended"
```

### Not Allowed Variable Names
```python
# Invalid names (will cause errors)
# 2age = 25        # Can't start with number
# first-name = ""  # Can't use hyphens
# class = "test"   # Can't use reserved keywords
# first name = ""  # Can't use spaces
```

### Snake Case Convention (Recommended)
```python
# Python convention - use snake_case
user_name = "john_doe"
birth_year = 1990
is_active = True
max_retry_count = 3
```

### Reserved Keywords (Cannot Use)
```python
# These are reserved and cannot be used as variable names:
# False, True, None, and, or, not, if, else, elif, while, for, 
# def, class, import, from, as, try, except, finally, with, etc.
```

---

## Casting (Type Conversion)

### Integer Casting
```python
a = int(1)        # 1
b = int(3.9)      # 3 (truncates decimal)
c = int('3')      # 3
d = int(True)     # 1
e = int(False)    # 0
```

### Float Casting
```python
f = float(5)      # 5.0
g = float('3.14') # 3.14
h = float(True)   # 1.0
```

### String Casting
```python
i = str(123)      # '123'
j = str(3.14)     # '3.14'
k = str(True)     # 'True'
```

### Boolean Casting
```python
l = bool(1)       # True
m = bool(0)       # False
n = bool('')      # False
o = bool('hello') # True
```

---

## Truthy and Falsy Values

### Falsy Values (evaluate to False)
```python
bool(False)    # False
bool(0)        # False
bool(0.0)      # False
bool('')       # False (empty string)
bool([])       # False (empty list)
bool({})       # False (empty dict)
bool(None)     # False
```

### Truthy Values (evaluate to True)
```python
bool(True)     # True
bool(1)        # True
bool(-1)       # True
bool(0.1)      # True
bool('hello')  # True
bool(' ')      # True (space is not empty)
bool([1])      # True (non-empty list)
```

---

## Print Function

### Basic Print
```python
print("Hello World")
print('Single quotes work too')
```

### Print with Variables
```python
name = "Alice"
age = 25
print(name, age)  # Alice 25
```

### Print with Separator (sep)
```python
print("apple", "banana", "cherry", sep="|")
# Output: apple|banana|cherry

print("2025", "07", "19", sep="-")
# Output: 2025-07-19
```

### Print with End Parameter
```python
print("Hello", end=" ")
print("World")
# Output: Hello World (on same line)

print("Loading", end="...")
print("Done")
# Output: Loading...Done
```

### Combining sep and end
```python
name = 'Ross'
sentence = 'We were on a break'
print(name, sentence, 9 + 18, sep='|', end='CC hothaifa\n')
print('Hunter x Hunter')
# Output: Ross|We were on a break|27CC hothaifa
#         Hunter x Hunter
```

---

## Input Function

### Basic Input
```python
name = input("Enter your name: ")
print("Hello", name)
```

### Input with Casting
```python
# Get integer input
age = int(input("Enter your age: "))
print("You are", age, "years old")

# Get float input
price = float(input("Enter price: "))
print("Price is $", price)
```

### Input without Prompt
```python
birth_year = int(input())  # User types without prompt
```

### Custom Prompts
```python
print('Please enter your birth year: ', end='')
birth_year = int(input())
```

---

## String Operations

### String Concatenation
```python
# Using + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# Multiple concatenation
email = "john" + "@" + "company.com"
print(email)  # john@company.com
```

### String Repetition
```python
# Using * operator
dashes = "-" * 50
print(dashes)  # --------------------------------------------------

stars = "*" * 10
print(stars)   # **********

# Useful for formatting
print("=" * 30)
print("    WELCOME TO PYTHON")
print("=" * 30)
```

---

## F-Strings

### Basic F-String Usage
```python
name = "Alice"
age = 25
message = f"Hi {name}, you are {age} years old"
print(message)  # Hi Alice, you are 25 years old
```

### F-Strings with Expressions
```python
birth_year = 1998
current_year = 2025
print(f"You are {current_year - birth_year} years old")
# You are 27 years old
```

### F-Strings with Multiple Variables
```python
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
print(f"Hi {name}, your age is {2025 - birth_year}")
```

---

## Garbage Collection

### What is Garbage Collection?
- Automatic memory management in Python
- Removes objects that are no longer referenced
- Prevents memory leaks
- Runs automatically in the background

### How it Works
```python
# When variables go out of scope or are reassigned,
# Python's garbage collector frees up memory

x = [1, 2, 3]  # List created in memory
x = [4, 5, 6]  # Previous list becomes eligible for garbage collection
x = None       # Current list also becomes eligible for garbage collection
```

### Memory Management Example
```python
# Reference counting
a = [1, 2, 3]  # Reference count = 1
b = a          # Reference count = 2
del a          # Reference count = 1
b = None       # Reference count = 0, object can be garbage collected
```

---

## Practice Examples

### Complete Example Program
```python
# Get user information
print("=== Python Lesson 1 Demo ===")
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

# Calculate age
current_year = 2025
age = current_year - birth_year

# Display results
print("=" * 40)
print(f"Hello {name}!")
print(f"You are {age} years old")
print("=" * 40)

# Boolean operations
is_adult = age >= 18
print(f"Are you an adult? {is_adult}")

# String operations
stars = "*" * age
print(f"Here are {age} stars for you: {stars}")
```

### Data Type Examples
```python
# Different data types
age = 25                    # int
height = 5.9               # float
name = "John Doe"          # str
is_student = True          # bool
complex_num = 3 + 4j       # complex

# Print types
print(f"age: {age}, type: {type(age)}")
print(f"height: {height}, type: {type(height)}")
print(f"name: {name}, type: {type(name)}")
print(f"is_student: {is_student}, type: {type(is_student)}")
print(f"complex_num: {complex_num}, type: {type(complex_num)}")
```
