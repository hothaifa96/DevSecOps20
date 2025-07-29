# Python DevOps Guide: Lists, Tuples, Sets, Loops & Ranges

## Table of Contents
1. [Conditional Statements](#conditional-statements)
2. [Lists](#lists)
3. [Tuples](#tuples)
4. [Sets](#sets)
5. [Range Function](#range-function)
6. [For Loops](#for-loops)
7. [Nested Loops & Sorting](#nested-loops--sorting)
8. [Practice Examples](#practice-examples)

---

## Conditional Statements

### CPU Usage Monitor Example
```python
cpu_usage = abs(float(input("Enter CPU usage percentage: ")))
# abs(n) -> positive n  -9→9, -119→119, 6→6

if cpu_usage >= 90:
    print('critical !!!!!!! ')
elif 70 <= cpu_usage < 90:
    print('high :( ')
elif 50 <= cpu_usage < 70:
    print('medium :| ')
elif cpu_usage < 50:  # else:
    print('normal :) ')
```

**Variable Table Example:**
| Input | cpu_usage | Output |
|-------|-----------|--------|
| 95 | 95.0 | critical !!!!!!! |
| 75 | 75.0 | high :( |
| 60 | 60.0 | medium :| |
| 30 | 30.0 | normal :) |

---

## Lists

### Basic List Operations
```python
# Creating and accessing lists
gang = ['eliran', 'holtsa afora', 4, True]
print(gang)           # ['eliran', 'holtsa afora', 4, True]
print(len(gang))      # 4
print(type(gang))     # <class 'list'>
print(gang[0])        # 'eliran'
print(gang[-1])       # True (last item)
```

**Index Reference:**
```
Index:    0         1            2    3
gang = ['eliran', 'holtsa afora', 4, True]
Index:   -4        -3           -2   -1
```

### List Methods
```python
employees = ['yuval', 'dani', 'neria', 'shlomi', 'mohammed']

# Common methods
print(employees.count('yuval'))  # 1
employees.append('or')           # Add to end
employees.remove('dani')         # Remove by value
employees.pop(0)                 # Remove by index
employees.insert(1, 'new_guy')  # Insert at position
```

### String Slicing in Lists
```python
gang = ['eliran', 'holtsa afora', 4, True]
word = gang[1]  # 'holtsa afora'
print(gang[1][0:len(gang[1])//2])  # 'holtsa' (first half)
print(gang[1][2])                  # 'l' (third character)
```

---

## Tuples

### Basic Tuple Operations
```python
# Creating tuples
t = tuple()           # Empty tuple
t = ()               # Empty tuple
t = (1, 55, 66, 77)  # Tuple with values

print(t)             # (1, 55, 66, 77)
print(type(t))       # <class 'tuple'>
print(t[2])          # 66
# t.append(22)       # ERROR! Tuples are immutable
```

### Converting Between Types
```python
t = ('hothaifa', 'zoubi')  # tuple
t = list(t)                # convert to list
t.insert(1, 'sos')         # modify list
t = tuple(t)               # convert back to tuple
print(t)                   # ('hothaifa', 'sos', 'zoubi')
```

**Variable Table for Conversion:**
| Step | Variable | Type | Value |
|------|----------|------|-------|
| 1 | t | tuple | ('hothaifa', 'zoubi') |
| 2 | t | list | ['hothaifa', 'zoubi'] |
| 3 | t | list | ['hothaifa', 'sos', 'zoubi'] |
| 4 | t | tuple | ('hothaifa', 'sos', 'zoubi') |

---

## Sets

### Set Characteristics
```python
grades = [100, 200, 300, 300, 300, 300, 300]
tuple_grades = (100, 200, 300, 300, 300, 300, 300)
set_grades = {100, 200, 300, 300, 300, 300, 300}

print(grades)        # [100, 200, 300, 300, 300, 300, 300]
print(tuple_grades)  # (100, 200, 300, 300, 300, 300, 300)
print(set_grades)    # {100, 200, 300} - no duplicates!

set_grades.add(6600)
print(set_grades)    # {100, 200, 300, 6600}
print(5500 in set_grades)  # False
```

**Key Differences:**
- **Lists**: Ordered, mutable, allow duplicates
- **Tuples**: Ordered, immutable, allow duplicates
- **Sets**: Unordered, mutable, no duplicates

---

## Range Function

### Basic Range Usage
```python
# range(start, stop, step)
print(list(range(10)))        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10)))     # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 100, 2))) # [0, 2, 4, 6, 8, ..., 98]
print(list(range(100, -1, -1))) # [100, 99, 98, ..., 1, 0]
```

### Practice Exercise Solution
```python
# Numbers divisible by 7 within range 0-77
result = tuple(range(0, 78, 7))
print(result)  # (0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77)
```

---

## For Loops

### Basic Loop Examples

#### Example 1: Names Processing
```python
names = ['Donald', 'Yuval', 'yossil', 'montana']

# Print names ending with 'l'
for name in names:
    if name.endswith('l'):
        print(name)  # Output: Yuval, yossil
```

#### Example 2: User Input Processing
```python
# Get 4 numbers and find maximum
numbers = []
for i in range(4):
    numbers.append(int(input('enter a number : ')))
print(max(numbers))
```

**Variable Table for Input [5, 10, 3, 8]:**
| Iteration | i | Input | numbers |
|-----------|---|-------|---------|
| 0 | 0 | 5 | [5] |
| 1 | 1 | 10 | [5, 10] |
| 2 | 2 | 3 | [5, 10, 3] |
| 3 | 3 | 8 | [5, 10, 3, 8] |
| Final | - | - | max = 10 |

#### Example 3: Sum Calculation
```python
sum = 0
for i in range(6):
    n = int(input(f'please enter the {i + 1} number: '))
    sum += n  # sum = sum + n
print(sum)
```

---

## Nested Loops & Sorting

### Bubble Sort Implementation
```python
points = [(1, 2), (1, 3), (2, 5), (2, 6), (1, 1), (3, 4), (4, 4)]
print("Original:", points)

# Bubble sort by second element of tuple
for i in range(len(points)):
    for j in range(0, len(points) - i - 1):
        if points[j][1] > points[j + 1][1]:
            points[j], points[j + 1] = points[j + 1], points[j]

print("Sorted:", points)
# Output: [(1, 1), (1, 2), (1, 3), (3, 4), (4, 4), (2, 5), (2, 6)]
```

### Detailed Variable Table for First Pass:
| i | j | points[j] | points[j+1] | Comparison | Swap? | Array State |
|---|---|-----------|-------------|------------|--------|-------------|
| 0 | 0 | (1,2) | (1,3) | 2 > 3? No | No | No change |
| 0 | 1 | (1,3) | (2,5) | 3 > 5? No | No | No change |
| 0 | 2 | (2,5) | (2,6) | 5 > 6? No | No | No change |
| 0 | 3 | (2,6) | (1,1) | 6 > 1? Yes | Yes | Swap positions |
| 0 | 4 | (2,6) | (3,4) | 6 > 4? Yes | Yes | Swap positions |
| 0 | 5 | (2,6) | (4,4) | 6 > 4? Yes | Yes | Swap positions |

---

## Practice Examples

### Easy Level

#### 1. List Creation and Access
```python
# Create a list of your favorite foods
foods = ['pizza', 'sushi', 'chocolate', 'ice cream']
print(f"My favorite food is {foods[0]}")
print(f"I have {len(foods)} favorite foods")
```

#### 2. Simple Range
```python
# Print numbers 1 to 5
for i in range(1, 6):
    print(i)
```

#### 3. Basic Set Operations
```python
colors = {'red', 'blue', 'green', 'blue', 'red'}
print(colors)  # {'red', 'blue', 'green'}
colors.add('yellow')
print('purple' in colors)  # False
```

### Medium Level

#### 4. List Comprehension Alternative
```python
# Create list of squares
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)  # [1, 4, 9, 16, 25]
```

#### 5. Tuple Unpacking
```python
coordinates = [(0, 0), (1, 2), (3, 4)]
for x, y in coordinates:
    distance = (x**2 + y**2) ** 0.5
    print(f"Point ({x}, {y}) is {distance:.2f} units from origin")
```

#### 6. Character Frequency
```python
chars = ['a','b','a','a','c','w','t','t','t','t','t','t']
unique_chars = []
for char in chars:
    if char not in unique_chars:
        unique_chars.append(char)
print(unique_chars)  # ['a', 'b', 'c', 'w', 't']
```

### Hard Level

#### 7. Matrix Operations
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Transpose matrix
transposed = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transposed.append(row)
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

#### 8. Advanced Sorting
```python
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('Diana', 92)]
# Sort by grade (descending), then by name (ascending)
for i in range(len(students)):
    for j in range(0, len(students) - i - 1):
        # First compare grades (descending)
        if (students[j][1] < students[j + 1][1] or 
            (students[j][1] == students[j + 1][1] and students[j][0] > students[j + 1][0])):
            students[j], students[j + 1] = students[j + 1], students[j]
print(students)  # [('Diana', 92), ('Bob', 90), ('Alice', 85), ('Charlie', 78)]
```

#### 9. Complex Data Processing
```python
# Process server logs
logs = [
    ('192.168.1.1', 'GET', '/api/users', 200),
    ('192.168.1.2', 'POST', '/api/login', 401),
    ('192.168.1.1', 'GET', '/api/data', 500),
    ('192.168.1.3', 'DELETE', '/api/users/1', 200)
]

# Count errors by IP
error_count = {}
for ip, method, endpoint, status in logs:
    if status >= 400:  # Error status codes
        if ip in error_count:
            error_count[ip] += 1
        else:
            error_count[ip] = 1

print(error_count)  # {'192.168.1.2': 1, '192.168.1.1': 1}
```

---

## Key DevOps Applications

### 1. Log Processing
```python
log_levels = ['INFO', 'WARNING', 'ERROR', 'ERROR', 'INFO']
error_count = log_levels.count('ERROR')
print(f"Found {error_count} errors in logs")
```

### 2. Server Monitoring
```python
servers = [
    ('web-01', 45, 'healthy'),
    ('web-02', 78, 'warning'),
    ('db-01', 92, 'critical')
]

for server, cpu, status in servers:
    if cpu > 80:
        print(f"ALERT: {server} CPU usage: {cpu}%")
```

### 3. Configuration Management
```python
configs = {
    'database_url': 'localhost:5432',
    'api_key': 'secret123',
    'debug_mode': True
}

required_configs = ['database_url', 'api_key']
for config in required_configs:
    if config not in configs:
        print(f"Missing required config: {config}")
```


Remember the DRY principle: **Don't Repeat Yourself** - use loops instead of writing repetitive code!