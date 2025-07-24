# Python Strings and Lists

## Table of Contents
1. [Strings](#strings)
2. [String Methods](#string-methods)
3. [String Slicing](#string-slicing)
4. [String Concatenation](#string-concatenation)
5. [f-Strings (Formatted String Literals)](#f-strings-formatted-string-literals)
6. [Lists](#lists)
7. [List Methods](#list-methods)
8. [Join and Split Functions](#join-and-split-functions)

---

## Strings

Strings in Python are sequences of characters enclosed in quotes. They are immutable, meaning you cannot change them after creation.

### Creating Strings

```python
# Single quotes
single_quote = 'Hello World'

# Double quotes
double_quote = "Hello World"

# Triple quotes (for multiline strings)
multiline = """This is a
multiline string"""

# Empty string
empty = ""
```

### String Characteristics
- **Immutable**: Cannot be changed after creation
- **Indexed**: Each character has a position (starting from 0)
- **Iterable**: Can loop through each character

---

## String Methods

Python provides many built-in methods for string manipulation:

### Case Methods

```python
text = "Hello World"

# Convert to uppercase
print(text.upper())        # "HELLO WORLD"

# Convert to lowercase
print(text.lower())        # "hello world"

# Capitalize first letter
print(text.capitalize())   # "Hello world"

# Title case (capitalize each word)
print(text.title())        # "Hello World"

# Swap case
print(text.swapcase())     # "hELLO wORLD"
```

### Checking Methods

```python
text = "Hello123"

# Check if all characters are alphabetic
print(text.isalpha())      # False

# Check if all characters are digits
print(text.isdigit())      # False

# Check if all characters are alphanumeric
print(text.isalnum())      # True

# Check if string starts with specific text
print(text.startswith("Hello"))  # True

# Check if string ends with specific text
print(text.endswith("123"))      # True
```

### Search and Replace Methods

```python
text = "Hello World Hello"

# Find position of substring
print(text.find("World"))     # 6
print(text.find("xyz"))       # -1 (not found)

# Count occurrences of substring
print(text.count("Hello"))    # 2

# Replace substring
print(text.replace("Hello", "Hi"))  # "Hi World Hi"

# Replace only first occurrence
print(text.replace("Hello", "Hi", 1))  # "Hi World Hello"
```

### Whitespace Methods

```python
text = "  Hello World  "

# Remove whitespace from both ends
print(text.strip())       # "Hello World"

# Remove whitespace from left
print(text.lstrip())      # "Hello World  "

# Remove whitespace from right
print(text.rstrip())      # "  Hello World"

# Remove specific characters
print(text.strip(" H"))   # "ello World"
```

---

## String Slicing

String slicing allows you to extract parts of a string using the syntax `string[start:end:step]`.

### Basic Slicing

```python
index   012345678910
text = "Hello World"

# Get character at index 0
print(text[0])           # "H"

# Get substring from index 0 to 4 (exclusive)
print(text[0:5])         # "Hello"

# Get substring from index 6 to end
print(text[6:])          # "World"

# Get entire string
print(text[:])           # "Hello World"
```

### Negative Indexing

```python
text = "Hello World"
#      0123456789 10  (positive indices)
#     -11-10-9-8-7-6-5-4-3-2-1  (negative indices)

# Get last character
print(text[-1])          # "d"

# Get second to last character
print(text[-2])          # "l"

# Get last 5 characters
print(text[-5:])         # "World"

# Get all except last 2 characters
print(text[:-2])         # "Hello Wor"
```

### Step/Jump Slicing

```python
text = "Hello World"

# Get every second character
print(text[::2])         # "HloWrd"

# Get every second character starting from index 1
print(text[1::2])        # "el ol"

# Get substring with step
print(text[0:5:2])       # "Hlo"

# Reverse the string (negative step)
print(text[::-1])        # "dlroW olleH"

# Get every second character in reverse
print(text[::-2])        # "drWol"
```

### Advanced Slicing Examples

```python
text = "Python Programming"

# Get first 6 characters
print(text[:6])          # "Python"

# Get characters from index 7 to 12
print(text[7:13])        # "Progra"

# Get every third character
print(text[::3])         # "Ph ormn"

# Reverse and get every second character
print(text[::-2])        # "gimrgr hP"

# Get middle portion in reverse
print(text[5:10][::-1])  # " nohty" -> "yhtno "
```

---

## String Concatenation

There are several ways to combine strings in Python:

### Using + Operator

```python
first_name = "John"
last_name = "Doe"

# Simple concatenation
full_name = first_name + " " + last_name
print(full_name)  # "John Doe"

# Multiple concatenation
greeting = "Hello " + first_name + " " + last_name + "!"
print(greeting)   # "Hello John Doe!"
```

### Using += Operator

```python
message = "Hello"
message += " "
message += "World"
print(message)    # "Hello World"
```

### Using join() Method

```python
words = ["Hello", "World", "from", "Python"]
sentence = " ".join(words)
print(sentence)   # "Hello World from Python"

# Using different separator
csv_data = ",".join(["apple", "banana", "cherry"])
print(csv_data)   # "apple,banana,cherry"
```

---

## f-Strings (Formatted String Literals)

f-Strings provide a readable and efficient way to format strings (Python 3.6+):

### Basic f-String Usage

```python
name = "Alice"
age = 30

# Basic f-string
message = f"Hello, my name is {name} and I am {age} years old."
print(message)  # "Hello, my name is Alice and I am 30 years old."
```

### Expressions in f-Strings

```python
x = 10
y = 5

# Mathematical expressions
result = f"The result of {x} + {y} is {x + y}"
print(result)  # "The result of 10 + 5 is 15"

# Function calls
name = "john doe"
formatted = f"Name: {name.title()}"
print(formatted)  # "Name: John Doe"
```

### Formatting Numbers

```python
pi = 3.14159265359

# Decimal places
print(f"Pi rounded to 2 decimal places: {pi:.2f}")  # "Pi rounded to 2 decimal places: 3.14"

# Percentage
percentage = 0.875
print(f"Success rate: {percentage:.1%}")  # "Success rate: 87.5%"

# Thousands separator
big_number = 1234567
print(f"Number with commas: {big_number:,}")  # "Number with commas: 1,234,567"
```

### Advanced f-String Formatting

```python
# Width and alignment
name = "Python"
print(f"|{name:>10}|")    # "|    Python|" (right aligned)
print(f"|{name:<10}|")    # "|Python    |" (left aligned)
print(f"|{name:^10}|")    # "|  Python  |" (center aligned)

# Zero padding
number = 42
print(f"Number: {number:05}")  # "Number: 00042"

# Different number bases
num = 255
print(f"Decimal: {num}, Hex: {num:x}, Binary: {num:b}")
# "Decimal: 255, Hex: ff, Binary: 11111111"
```

---

## Lists

Lists are ordered, mutable collections that can store multiple items of different data types.

### Creating Lists

```python
# Empty list
empty_list = []

# List with initial values
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

# Using list() constructor
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(5))  # [0, 1, 2, 3, 4]
```

### List Indexing and Slicing

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing
print(fruits[0])     # "apple"
print(fruits[-1])    # "elderberry"

# Slicing
print(fruits[1:4])   # ["banana", "cherry", "date"]
print(fruits[:3])    # ["apple", "banana", "cherry"]
print(fruits[2:])    # ["cherry", "date", "elderberry"]
print(fruits[::2])   # ["apple", "cherry", "elderberry"]
print(fruits[::-1])  # ["elderberry", "date", "cherry", "banana", "apple"]
```

---

## List Methods

Python provides many built-in methods for list manipulation:

### Adding Elements

```python
fruits = ["apple", "banana"]

# Add single element to end
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]

# Add multiple elements to end
fruits.extend(["date", "elderberry"])
print(fruits)  # ["apple", "banana", "cherry", "date", "elderberry"]

# Insert element at specific position
fruits.insert(1, "apricot")
print(fruits)  # ["apple", "apricot", "banana", "cherry", "date", "elderberry"]
```

### Removing Elements

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# Remove first occurrence of value
fruits.remove("banana")
print(fruits)  # ["apple", "cherry", "banana", "date"]

# Remove and return element at index (default: last)
last_fruit = fruits.pop()
print(last_fruit)  # "date"
print(fruits)      # ["apple", "cherry", "banana"]

# Remove element at specific index
second_fruit = fruits.pop(1)
print(second_fruit)  # "cherry"
print(fruits)        # ["apple", "banana"]

# Remove all elements
fruits.clear()
print(fruits)  # []
```

### Finding and Counting

```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# Find index of first occurrence
index = numbers.index(2)
print(index)  # 1

# Find index starting from specific position
index = numbers.index(2, 2)  # Start searching from index 2
print(index)  # 3

# Count occurrences
count = numbers.count(2)
print(count)  # 3
```

### Sorting and Reversing

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# Sort in place (modifies original list)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# Sort in descending order
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# Reverse the list
numbers.reverse()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# Create sorted copy (doesn't modify original)
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
print(original)     # [3, 1, 4, 1, 5]
print(sorted_copy)  # [1, 1, 3, 4, 5]
```

### Copying Lists

```python
original = [1, 2, 3, 4, 5]

# Shallow copy
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# Modify original
original.append(6)
print(original)  # [1, 2, 3, 4, 5, 6]
print(copy1)     # [1, 2, 3, 4, 5]
```

---

## Join and Split Functions

These functions are essential for converting between strings and lists:

### split() Method

```python
# Basic splitting (default: whitespace)
text = "Hello World Python"
words = text.split()
print(words)  # ["Hello", "World", "Python"]

# Split by specific delimiter
csv_data = "apple,banana,cherry,date"
fruits = csv_data.split(",")
print(fruits)  # ["apple", "banana", "cherry", "date"]

# Limit number of splits
text = "one-two-three-four-five"
parts = text.split("-", 2)  # Split only twice
print(parts)  # ["one", "two", "three-four-five"]

# Split by newlines
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.split("\n")
print(lines)  # ["Line 1", "Line 2", "Line 3"]
```

### rsplit() Method (Right Split)

```python
# Split from the right
text = "www.example.com"
parts = text.rsplit(".", 1)  # Split only once from right
print(parts)  # ["www.example", "com"]
```

### splitlines() Method

```python
# Split by line breaks
text = "Line 1\nLine 2\r\nLine 3\rLine 4"
lines = text.splitlines()
print(lines)  # ["Line 1", "Line 2", "Line 3", "Line 4"]

# Keep line endings
lines_with_endings = text.splitlines(keepends=True)
print(lines_with_endings)  # ["Line 1\n", "Line 2\r\n", "Line 3\r", "Line 4"]
```

### join() Method

```python
# Basic joining
words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print(sentence)  # "Hello World Python"

# Join with different separators
numbers = ["1", "2", "3", "4", "5"]
print("-".join(numbers))    # "1-2-3-4-5"
print("".join(numbers))     # "12345"
print(" | ".join(numbers))  # "1 | 2 | 3 | 4 | 5"

# Join with newlines
lines = ["First line", "Second line", "Third line"]
multiline = "\n".join(lines)
print(multiline)
# First line
# Second line
# Third line
```

### Practical Examples

```python
# Processing CSV data
csv_line = "John,Doe,30,Engineer"
fields = csv_line.split(",")
print(f"Name: {fields[0]} {fields[1]}")  # "Name: John Doe"
print(f"Age: {fields[2]}")               # "Age: 30"
print(f"Job: {fields[3]}")               # "Job: Engineer"

# Creating file paths
path_parts = ["home", "user", "documents", "file.txt"]
file_path = "/".join(path_parts)
print(file_path)  # "home/user/documents/file.txt"

# Processing log entries
log_entry = "2024-01-15 10:30:45 ERROR Database connection failed"
parts = log_entry.split(" ", 3)  # Split into 4 parts maximum
date = parts[0]
time = parts[1]
level = parts[2]
message = parts[3]
print(f"Date: {date}, Time: {time}, Level: {level}")
print(f"Message: {message}")

# Converting between formats
# Space-separated to comma-separated
space_separated = "apple banana cherry date"
fruits_list = space_separated.split()
comma_separated = ",".join(fruits_list)
print(comma_separated)  # "apple,banana,cherry,date"
```

