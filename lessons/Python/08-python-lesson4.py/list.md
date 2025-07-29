# Python Methods Reference: Lists, Tuples & Sets

## Table of Contents
1. [List Methods](#list-methods)
2. [Tuple Methods](#tuple-methods)
3. [Set Methods](#set-methods)
4. [Common Operations](#common-operations)
5. [Performance Comparison](#performance-comparison)

---

## List Methods

### Modifying Methods (Change the original list)

#### `append(item)`
Adds an item to the end of the list
```python
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)  # ['apple', 'banana', 'orange']
```

#### `insert(index, item)`
Inserts an item at a specific position
```python
fruits = ['apple', 'banana']
fruits.insert(1, 'grape')
print(fruits)  # ['apple', 'grape', 'banana']
```

#### `extend(iterable)`
Adds all items from an iterable to the end of the list
```python
fruits = ['apple', 'banana']
fruits.extend(['orange', 'grape'])
print(fruits)  # ['apple', 'banana', 'orange', 'grape']
```

#### `remove(item)`
Removes the first occurrence of an item
```python
fruits = ['apple', 'banana', 'apple']
fruits.remove('apple')
print(fruits)  # ['banana', 'apple']
```

#### `pop(index)`
Removes and returns item at index (default: last item)
```python
fruits = ['apple', 'banana', 'orange']
removed = fruits.pop(1)
print(removed)  # 'banana'
print(fruits)   # ['apple', 'orange']

last = fruits.pop()
print(last)     # 'orange'
print(fruits)   # ['apple']
```

#### `clear()`
Removes all items from the list
```python
fruits = ['apple', 'banana', 'orange']
fruits.clear()
print(fruits)  # []
```

#### `reverse()`
Reverses the list in place
```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
```

#### `sort(key=None, reverse=False)`
Sorts the list in place
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5]

numbers.sort(reverse=True)
print(numbers)  # [5, 4, 3, 1, 1]

# Sort by length
words = ['python', 'java', 'c', 'javascript']
words.sort(key=len)
print(words)  # ['c', 'java', 'python', 'javascript']
```

### Non-Modifying Methods (Return information)

#### `count(item)`
Returns the number of occurrences of an item
```python
numbers = [1, 2, 3, 2, 2, 4]
print(numbers.count(2))  # 3
print(numbers.count(5))  # 0
```

#### `index(item, start=0, end=len)`
Returns the index of the first occurrence of an item
```python
fruits = ['apple', 'banana', 'orange', 'banana']
print(fruits.index('banana'))     # 1
print(fruits.index('banana', 2))  # 3 (search from index 2)
# print(fruits.index('grape'))    # ValueError: 'grape' is not in list
```

#### `copy()`
Returns a shallow copy of the list
```python
original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print(original)  # [1, 2, 3]
print(copied)    # [1, 2, 3, 4]
```

### List Comprehension (Alternative to loops)
```python
# Instead of:
squares = []
for i in range(5):
    squares.append(i**2)

# Use:
squares = [i**2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition:
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

---

## Tuple Methods

**Note: Tuples are immutable, so they have fewer methods**

#### `count(item)`
Returns the number of occurrences of an item
```python
numbers = (1, 2, 3, 2, 2, 4)
print(numbers.count(2))  # 3
print(numbers.count(5))  # 0
```

#### `index(item, start=0, end=len)`
Returns the index of the first occurrence of an item
```python
fruits = ('apple', 'banana', 'orange', 'banana')
print(fruits.index('banana'))     # 1
print(fruits.index('banana', 2))  # 3
# print(fruits.index('grape'))    # ValueError: 'grape' is not in tuple
```

### Tuple Operations
```python
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = (1, 2) * 3
print(repeated)  # (1, 2, 1, 2, 1, 2)

# Unpacking
point = (3, 4)
x, y = point
print(f"x: {x}, y: {y}")  # x: 3, y: 4

# Multiple assignment
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"Point: ({x}, {y})")
```

### Converting Tuples
```python
# Tuple to List (for modification)
t = (1, 2, 3)
l = list(t)
l.append(4)
t = tuple(l)
print(t)  # (1, 2, 3, 4)

# Tuple to Set (remove duplicates)
t = (1, 2, 2, 3, 3, 4)
s = set(t)
print(s)  # {1, 2, 3, 4}
```

---

## Set Methods

### Adding Elements

#### `add(item)`
Adds a single item to the set
```python
fruits = {'apple', 'banana'}
fruits.add('orange')
print(fruits)  # {'apple', 'banana', 'orange'}

# Adding duplicate has no effect
fruits.add('apple')
print(fruits)  # {'apple', 'banana', 'orange'}
```

#### `update(iterable)`
Adds multiple items from an iterable
```python
fruits = {'apple', 'banana'}
fruits.update(['orange', 'grape', 'apple'])
print(fruits)  # {'apple', 'banana', 'orange', 'grape'}

# Can update with multiple iterables
fruits.update(['kiwi'], ('mango',), {'pear'})
print(fruits)  # {'apple', 'banana', 'orange', 'grape', 'kiwi', 'mango', 'pear'}
```

### Removing Elements

#### `remove(item)`
Removes an item (raises KeyError if not found)
```python
fruits = {'apple', 'banana', 'orange'}
fruits.remove('banana')
print(fruits)  # {'apple', 'orange'}

# fruits.remove('grape')  # KeyError: 'grape'
```

#### `discard(item)`
Removes an item (no error if not found)
```python
fruits = {'apple', 'banana', 'orange'}
fruits.discard('banana')
fruits.discard('grape')  # No error
print(fruits)  # {'apple', 'orange'}
```

#### `pop()`
Removes and returns an arbitrary item
```python
fruits = {'apple', 'banana', 'orange'}
removed = fruits.pop()
print(f"Removed: {removed}")
print(fruits)  # Remaining items (order not guaranteed)
```

#### `clear()`
Removes all items from the set
```python
fruits = {'apple', 'banana', 'orange'}
fruits.clear()
print(fruits)  # set()
```

### Set Operations

#### `union(other)` or `|`
Returns a new set with items from both sets
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # {1, 2, 3, 4, 5}

# Using operator
result = set1 | set2
print(result)  # {1, 2, 3, 4, 5}
```

#### `intersection(other)` or `&`
Returns a new set with common items
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.intersection(set2)
print(result)  # {3, 4}

# Using operator
result = set1 & set2
print(result)  # {3, 4}
```

#### `difference(other)` or `-`
Returns a new set with items in first set but not in second
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.difference(set2)
print(result)  # {1, 2}

# Using operator
result = set1 - set2
print(result)  # {1, 2}
```

#### `symmetric_difference(other)` or `^`
Returns a new set with items in either set, but not both
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.symmetric_difference(set2)
print(result)  # {1, 2, 5, 6}

# Using operator
result = set1 ^ set2
print(result)  # {1, 2, 5, 6}
```

### Set Comparison Methods

#### `issubset(other)` or `<=`
Checks if all items in set are in other
```python
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # True
print(set1 <= set2)         # True
```

#### `issuperset(other)` or `>=`
Checks if set contains all items in other
```python
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set1.issuperset(set2))  # True
print(set1 >= set2)           # True
```

#### `isdisjoint(other)`
Checks if sets have no common items
```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}
print(set1.isdisjoint(set2))  # True
print(set1.isdisjoint(set3))  # False
```

### Set Comprehension
```python
# Square of even numbers
squares = {x**2 for x in range(10) if x % 2 == 0}
print(squares)  # {0, 4, 16, 36, 64}

# Unique lengths of words
words = ['python', 'java', 'c', 'javascript', 'go']
lengths = {len(word) for word in words}
print(lengths)  # {1, 4, 6, 10}
```

---

## Common Operations

### Membership Testing
```python
# Lists, Tuples, Sets
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}

print(3 in my_list)   # True
print(6 not in my_tuple)  # True
print(4 in my_set)    # True (fastest for large collections)
```

### Length and Iteration
```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}

# Length
print(len(my_list))   # 3
print(len(my_tuple))  # 3
print(len(my_set))    # 3

# Iteration
for item in my_list:   # Ordered
    print(item)
    
for item in my_tuple:  # Ordered  
    print(item)
    
for item in my_set:    # Unordered
    print(item)
```

### Type Conversion
```python
# From list
my_list = [1, 2, 3, 2, 1]
print(tuple(my_list))  # (1, 2, 3, 2, 1)
print(set(my_list))    # {1, 2, 3} - removes duplicates

# From tuple
my_tuple = (1, 2, 3, 2, 1)
print(list(my_tuple))  # [1, 2, 3, 2, 1]
print(set(my_tuple))   # {1, 2, 3} - removes duplicates

# From set
my_set = {1, 2, 3}
print(list(my_set))    # [1, 2, 3] - arbitrary order
print(tuple(my_set))   # (1, 2, 3) - arbitrary order
```

---

## Performance Comparison

### Time Complexity (Big O)

| Operation | List | Tuple | Set |
|-----------|------|-------|-----|
| Access by index | O(1) | O(1) | N/A |
| Search (in) | O(n) | O(n) | O(1) |
| Insert at end | O(1) | N/A | O(1) |
| Insert at beginning | O(n) | N/A | O(1) |
| Delete | O(n) | N/A | O(1) |

### When to Use What

#### Use **Lists** when:
- You need ordered data
- You need to access items by index
- You need to modify the collection frequently
- You allow duplicate values

#### Use **Tuples** when:
- You need ordered, immutable data
- You want to ensure data doesn't change
- You need to use as dictionary keys
- You're returning multiple values from functions

#### Use **Sets** when:
- You need unique values only
- You need fast membership testing
- You need set operations (union, intersection, etc.)
- Order doesn't matter

### DevOps Examples
```python
# Server names (unique) - Use Set
servers = {'web-01', 'web-02', 'db-01', 'cache-01'}

# Log entries (ordered, with duplicates) - Use List
log_entries = [
    '2024-01-01 INFO: Server started',
    '2024-01-01 ERROR: Connection failed',
    '2024-01-01 INFO: Server started'  # Duplicate is meaningful
]

# Configuration (immutable) - Use Tuple
database_config = ('localhost', 5432, 'production')
```

---