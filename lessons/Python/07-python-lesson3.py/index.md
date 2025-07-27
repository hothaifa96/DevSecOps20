# Python Fundamentals: Complete Guide

## Table of Contents
1. [String Slicing](#string-slicing)
2. [Conditional Statements (if, elif, else)](#conditional-statements)
3. [Logical Operators (and, or, not)](#logical-operators)
4. [Comparison Operators](#comparison-operators)
5. [Random Module](#random-module)
6. [Datetime Module](#datetime-module)
7. [Timestamps](#timestamps)
8. [Math Module](#math-module)

---

## String Slicing

String slicing allows you to extract portions of a string using index positions.

### Basic Syntax
```python
string[start:end:step]
```

### Examples

```python
text = "Hello, World!"

# Basic slicing
print(text[0:5])     # Output: "Hello"
print(text[7:12])    # Output: "World"
print(text[:5])      # Output: "Hello" (start from beginning)
print(text[7:])      # Output: "World!" (go to end)

# Negative indexing
print(text[-6:-1])   # Output: "World"
print(text[-1])      # Output: "!" (last character)

# Step parameter
print(text[::2])     # Output: "Hlo ol!" (every 2nd character)
print(text[::-1])    # Output: "!dlroW ,olleH" (reverse string)

# Advanced examples
email = "user@example.com"
username = email[:email.index('@')]  # Output: "user"
domain = email[email.index('@')+1:]  # Output: "example.com"

# String manipulation with slicing
def mask_credit_card(card_number):
    return "*" * (len(card_number) - 4) + card_number[-4:]

print(mask_credit_card("1234567890123456"))  # Output: "************3456"
```

---

## Conditional Statements

Control flow using if, elif, and else statements.

### Basic Syntax
```python
if condition:
    # code block
elif another_condition:
    # code block
else:
    # code block
```

### Examples

```python
# Simple if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")

# if-elif-else chain
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

# Nested conditions
username = "admin"
password = "secret123"
is_active = True

if username == "admin":
    if password == "secret123":
        if is_active:
            print("Access granted")
        else:
            print("Account inactive")
    else:
        print("Invalid password")
else:
    print("Invalid username")

# DevOps example: Server health check
cpu_usage = 75
memory_usage = 60
disk_usage = 90

if cpu_usage > 80:
    print("HIGH CPU ALERT!")
elif cpu_usage > 60:
    print("CPU usage moderate")

if memory_usage > 85:
    print("HIGH MEMORY ALERT!")
elif memory_usage > 70:
    print("Memory usage elevated")

if disk_usage > 90:
    print("CRITICAL: Disk space low!")
elif disk_usage > 80:
    print("WARNING: Disk space getting full")
```

---

## Logical Operators

Combine multiple conditions using and, or, and not operators.

### Truth Tables

**AND Operator:**
- True and True = True
- True and False = False
- False and True = False
- False and False = False

**OR Operator:**
- True or True = True
- True or False = True
- False or True = True
- False or False = False

**NOT Operator:**
- not True = False
- not False = True

### Examples

```python
# AND operator
age = 25
has_license = True
if age >= 18 and has_license:
    print("Can drive")

# OR operator
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("No work today!")

# NOT operator
is_logged_in = False
if not is_logged_in:
    print("Please log in")

# Complex combinations
user_role = "admin"
is_authenticated = True
has_permission = True

if is_authenticated and (user_role == "admin" or has_permission):
    print("Access granted to admin panel")

# DevOps monitoring example
cpu_ok = True
memory_ok = False
disk_ok = True
network_ok = True

# System is healthy if all components are OK
system_healthy = cpu_ok and memory_ok and disk_ok and network_ok
print(f"System healthy: {system_healthy}")

# Alert if any critical component fails
critical_failure = not cpu_ok or not memory_ok
if critical_failure:
    print("CRITICAL SYSTEM ALERT!")

# Maintenance window check
is_maintenance_hour = False
is_emergency = True
allow_deployment = not is_maintenance_hour or is_emergency
print(f"Deployment allowed: {allow_deployment}")
```

---

## Comparison Operators

Compare values using various comparison operators.

### Operators
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to
- `==` : Equal to
- `!=` : Not equal to

### Examples

```python
# Numeric comparisons
a = 10
b = 20

print(a > b)   # False
print(a < b)   # True
print(a >= 10) # True
print(a <= 10) # True
print(a == 10) # True
print(a != b)  # True

# String comparisons
name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print(name1 == name3)  # True
print(name1 != name2)  # True
print(name1 < name2)   # True (lexicographic order)

# Comparing different types
print(10 == "10")      # False (different types)
print(10 == 10.0)      # True (same value, different types)

# DevOps examples
# Server monitoring
server_response_time = 250  # milliseconds
max_response_time = 500

if server_response_time > max_response_time:
    print("Server response time too high!")
elif server_response_time >= max_response_time * 0.8:
    print("Server response time approaching limit")

# Version comparison
current_version = "2.1.3"
required_version = "2.0.0"

# Simple string comparison (works for semantic versioning in many cases)
if current_version >= required_version:
    print("Version requirement satisfied")

# Resource allocation
allocated_memory = 8  # GB
required_memory = 4   # GB
available_memory = 16 # GB

if allocated_memory < required_memory:
    print("Insufficient memory allocated")
elif allocated_memory > available_memory:
    print("Cannot allocate more memory than available")
else:
    print("Memory allocation OK")
```

---

## Random Module

Generate random numbers and make random choices.

### Importing and Basic Functions

```python
import random

# Basic random functions
print(random.random())          # Random float between 0.0 and 1.0
print(random.randint(1, 10))    # Random integer between 1 and 10 (inclusive)
print(random.uniform(1.5, 10.5))  # Random float between 1.5 and 10.5
print(random.choice(['a', 'b', 'c']))  # Random choice from list
```

### Examples

```python
import random

# Random integers
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

# Random floats
temperature = random.uniform(20.0, 35.0)
print(f"Random temperature: {temperature:.2f}°C")

# Random choices
colors = ['red', 'blue', 'green', 'yellow']
random_color = random.choice(colors)
print(f"Random color: {random_color}")

# Random sampling (multiple items without replacement)
participants = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
winners = random.sample(participants, 3)
print(f"Winners: {winners}")

# Shuffling lists
deck = ['A', 'K', 'Q', 'J'] * 4
random.shuffle(deck)
print(f"Shuffled deck: {deck}")


## Datetime Module

Work with dates and times.

### Basic Classes
- `datetime.datetime`: Date and time
- `datetime.date`: Date only
- `datetime.time`: Time only
- `datetime.timedelta`: Duration/difference

### Examples

```python
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")

today = date.today()
print(f"Today's date: {today}")

current_time = datetime.now().time()
print(f"Current time: {current_time}")

# Creating specific dates and times
specific_date = date(2024, 12, 25)
print(f"Christmas 2024: {specific_date}")

specific_datetime = datetime(2024, 12, 25, 14, 30, 0)
print(f"Christmas 2024 at 2:30 PM: {specific_datetime}")

# Formatting dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted: {formatted_date}")

# Parsing strings to dates
date_string = "2024-07-27"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")

# Date arithmetic with timedelta
tomorrow = today + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

one_week_ago = now - timedelta(weeks=1)
print(f"One week ago: {one_week_ago}")

# DevOps examples
# Log rotation based on date
log_date = datetime(2024, 7, 20)
days_old = (datetime.now() - log_date).days
if days_old > 30:
    print(f"Log file is {days_old} days old - should be archived")

# Maintenance window scheduling
maintenance_start = datetime(2024, 7, 28, 2, 0)  # 2 AM
maintenance_duration = timedelta(hours=4)
maintenance_end = maintenance_start + maintenance_duration

print(f"Maintenance window: {maintenance_start} to {maintenance_end}")

# SSL certificate expiry check
cert_expiry = datetime(2024, 12, 31, 23, 59, 59)
days_until_expiry = (cert_expiry - datetime.now()).days
if days_until_expiry < 30:
    print(f"Certificate expires in {days_until_expiry} days - renew soon!")
```

---

## Timestamps

Work with Unix timestamps and conversions.

### Unix Timestamps
Unix timestamp represents seconds since January 1, 1970 (Unix epoch).