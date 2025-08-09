# Lesson 10: REST API, Dictionaries, JSON, and pip - Complete Summary

## Table of Contents
1. [Python Dictionaries](#python-dictionaries)
2. [Dictionary Operations and Methods](#dictionary-operations-and-methods)
3. [Looping Through Dictionaries](#looping-through-dictionaries)
4. [Package Management with pip](#package-management-with-pip)
5. [JSON and Data Formats](#json-and-data-formats)
6. [REST API Basics](#rest-api-basics)
7. [Making HTTP GET Requests](#making-http-get-requests)
8. [Practical Examples](#practical-examples)
9. [Common Patterns and Best Practices](#common-patterns-and-best-practices)

## Python Dictionaries

### What are Dictionaries?
Dictionaries are Python's built-in data type for storing key-value pairs. Unlike lists that use numeric indices, dictionaries use keys to access values.

```python
# List vs Dictionary comparison
grades_list = [11, 19, 99, 68, 79]  # Access by index: grades_list[0]
grades_dict = {'hodi': 11, 'raed': 19, 'shlomi': 99, 'max': 68, 'shay': 79}  # Access by key: grades_dict['hodi']
```

### Creating Dictionaries
```python
# Empty dictionary
empty_dict = {}

# Dictionary with initial data
car = {
    'make': 'byd', 
    'model': 'atto3', 
    'distance': 404, 
    'ev': True, 
    'belts': [False, False, False, False, False]
}

# Student data example
student = {
    'name': 'John',
    'age': 20,
    'grades': [85, 92, 78],
    'enrolled': True
}
```

### Dictionary Characteristics
- **Unordered**: Items don't have a defined order (Python 3.7+ maintains insertion order)
- **Mutable**: Can be changed after creation
- **Key Requirements**: Keys must be immutable (strings, numbers, tuples)
- **Unique Keys**: Each key can appear only once

## Dictionary Operations and Methods

### Reading Dictionary Data
```python
car = {'make': 'byd', 'model': 'atto3', 'distance': 404, 'ev': True}

# Basic information
print(car)                    # Print entire dictionary
print(type(car))             # <class 'dict'>
print(len(car))              # Number of key-value pairs: 4

# Accessing values
print(car['make'])           # 'byd' - Direct access
print(car['ev'])             # True

# Safe access (won't cause error if key doesn't exist)
print(car.get('wheels'))     # None (key doesn't exist)
print(car.get('wheels', 4))  # 4 (default value if key doesn't exist)

# This would cause an error:
# print(car['wheels'])       # KeyError!
```

### Modifying Dictionary Data
```python
car = {'make': 'byd', 'model': 'atto3', 'distance': 404, 'ev': True}

# Update existing value
car['distance'] = 555
print(car['distance'])       # 555

# Add new key-value pair
car['color'] = 'grey'
print(car)                   # Now includes 'color': 'grey'

# Multiple ways to delete items
del car['make']              # Delete specific key
car.pop('distance')          # Remove and return value
car.clear()                  # Remove all items
```

### Dictionary Methods
```python
car = {'make': 'byd', 'model': 'atto3', 'distance': 404, 'ev': True}

# Get all keys, values, and items
print(car.keys())            # dict_keys(['make', 'model', 'distance', 'ev'])
print(car.values())          # dict_values(['byd', 'atto3', 404, True])
print(car.items())           # dict_items([('make', 'byd'), ('model', 'atto3'), ...])

# Check if key exists
print('make' in car.keys())  # True
print('wheels' in car)       # False (shorter syntax)

# Using variables as keys
data = 'make'
print(car[data])             # 'byd' - same as car['make']
```

## Looping Through Dictionaries

### Different Ways to Loop
```python
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 96}

# Loop through keys only
print("Student names:")
for student in student_grades:
    print(student)

# Loop through keys explicitly
print("Student names (explicit):")
for student in student_grades.keys():
    print(student)

# Loop through values only
print("Grades:")
for grade in student_grades.values():
    print(grade)

# Loop through key-value pairs
print("Student grades:")
for student, grade in student_grades.items():
    print(f"{student}: {grade}")
```

### Practical Dictionary Looping Examples

#### Example 1: Class Management System
```python
import random

# Generate random student counts for each class
classes = {
    'class_A': random.randint(0, 50), 
    'class_B': random.randint(0, 50), 
    'class_C': random.randint(0, 50),
    'class_D': random.randint(0, 50), 
    'class_E': random.randint(0, 50), 
    'class_F': random.randint(0, 50)
}

print("Class enrollment data:")
print(classes)

# i) Print number of students in class E
print(f"Number of students in class E: {classes['class_E']}")

# ii) Print all class names
print("All class names:")
print(list(classes.keys()))

# iii) Update class A and add new class
classes['class_A'] = 0      # Override existing
classes['class_X'] = 20     # Add new class

print("Updated classes:")
print(classes)

# iv) Calculate average students per class
total_students = 0
for student_count in classes.values():
    total_students += student_count

average = total_students / len(classes)
print(f"Average students per class: {average:.2f}")

# Alternative calculation using built-in sum()
total_students = sum(classes.values())
average = total_students / len(classes)
print(f"Average (using sum()): {average:.2f}")
```

#### Example 2: Employee Data Processing
```python
employee = {
    'name': ['haim', 'or'], 
    'car': "audi rs7", 
    'role': 'DevOps Eng', 
    'salary': 32000, 
    'office_days': 3,
    'cibus': 1140
}

print("Employee information:")

# Process each key-value pair
total_compensation = 0
for key, value in employee.items():
    print(f"Key: {key}, Value: {value}")
    
    # Calculate total compensation
    if key == 'salary' or key == 'cibus':
        total_compensation += value
    
    # Handle list values specially
    if isinstance(value, list):  # Check if value is a list
        print(f"Processing list for {key}:")
        for item in value:
            if item == 'haim':
                print("Found special name: shakshoka")
            else:
                print(f"Name: {item}")

print(f"Total compensation: {total_compensation}")
```

## Package Management with pip

### What is pip?
`pip` is Python's package installer. It allows you to install, update, and manage Python packages from the Python Package Index (PyPI).

### Basic pip Commands
```bash
# Install a package
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Install multiple packages
pip install requests pillow matplotlib

# Upgrade a package
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Show package information
pip show package_name

# Create requirements file
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

### Example: Installing and Using PIL (Pillow)
```bash
# Install Pillow for image processing
pip install Pillow
```

```python
# Using PIL after installation
from PIL import Image

# Interactive image viewer
choice = input('What image you want to see: (panda, pizza) ')

if choice == 'panda':
    image = Image.open('panda.jpg')
else:
    image = Image.open('download.jpg')

# Resize and display image
resized_image = image.resize((1300, 1100))
resized_image.show()
```

### Understanding pip freeze
```bash
# See all installed packages with versions
pip freeze

# Example output:
# requests==2.28.1
# Pillow==9.2.0
# urllib3==1.26.12

# Save to requirements.txt
pip freeze > requirements.txt

# Install exact same versions on another machine
pip install -r requirements.txt
```

## JSON and Data Formats

### What is JSON?
JSON (JavaScript Object Notation) is a lightweight, text-based data interchange format. It's easy for humans to read and write, and easy for machines to parse and generate.

### JSON Structure
```json
{
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "hobbies": ["reading", "swimming", "coding"],
  "married": false,
  "address": {
    "street": "123 Main St",
    "zipcode": "10001"
  }
}
```

### JSON vs Python Dictionary
```python
# Python dictionary
python_dict = {
    "name": "John",
    "age": 30,
    "active": True,
    "scores": [85, 92, 78]
}

# When converted to JSON string, it looks very similar
# but with slight syntax differences (true vs True, etc.)
```

## REST API Basics

### What is a REST API?
REST (Representational State Transfer) is an architectural style for designing web services. A REST API allows different applications to communicate over HTTP using standard methods.

### HTTP Methods
- **GET**: Retrieve data from server
- **POST**: Send data to server (create new resource)
- **PUT**: Update existing resource
- **DELETE**: Remove resource

### HTTP Status Codes
```python
# Common status codes
# 200-299: Success
# 200: OK
# 201: Created
# 204: No Content

# 400-499: Client errors
# 400: Bad Request
# 401: Unauthorized
# 404: Not Found

# 500-599: Server errors
# 500: Internal Server Error
# 503: Service Unavailable
```

### API Endpoints
An endpoint is a specific URL where an API can be accessed. Examples:
- `https://jsonplaceholder.typicode.com/users` - Get all users
- `https://jsonplaceholder.typicode.com/users/1` - Get user with ID 1
- `https://jsonplaceholder.typicode.com/posts` - Get all posts

## Making HTTP GET Requests

### Installing requests
```bash
pip install requests
```

### Basic GET Request
```python
import requests

# Make a GET request
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

# Check the response
print(response)                    # <Response [200]>
print(response.status_code)        # 200

# Check if request was successful
if 200 <= response.status_code < 300:
    print('Success response')
    
    # Get JSON data
    data = response.json()
    print(type(data))              # <class 'list'>
    print(type(data[0]))           # <class 'dict'>
    
    # Process the data
    for user in data:
        print(f"Name: {user['name']}, Email: {user['email']}")
```

### Error Handling
```python
import requests

url = 'https://jsonplaceholder.typicode.com/users'

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        print('Request successful')
        users = response.json()
        
        for user in users:
            print(f"User: {user['name']}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
```

## Practical Examples

### Example 1: User Data Processing
```python
import requests

# Fetch user data
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    
    print("All user names:")
    for user in users:
        print(f"- {user['name']} ({user['email']})")
    
    print(f"\nTotal users: {len(users)}")
else:
    print(f"Failed to fetch data: {response.status_code}")
```

### Example 2: Post Analysis
```python
import requests

# Fetch posts data
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    print('Data fetched successfully')
    posts = response.json()
    print(f"Total posts: {len(posts)}")
    
    # Find posts with titles longer than 60 characters
    long_titles = []
    
    for post in posts:
        title = post.get('title', '')
        
        if len(title) > 60:
            long_titles.append(title)
            print(f"Long title: {title}")
            
            # Count spaces and words
            space_count = title.count(' ')
            word_count = space_count + 1
            
            print(f"Spaces: {space_count}")
            print(f"Words: {word_count}")
            print("-" * 50)
    
    print(f"\nFound {len(long_titles)} posts with long titles")
else:
    print(f"Failed to fetch posts: {response.status_code}")
```

### Example 3: Data Analysis and Statistics
```python
import requests

# Get posts data
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    
    # Analyze title lengths
    title_lengths = []
    total_characters = 0
    
    for post in posts:
        title = post['title']
        length = len(title)
        title_lengths.append(length)
        total_characters += length
    
    # Calculate statistics
    average_length = total_characters / len(posts)
    shortest_title = min(title_lengths)
    longest_title = max(title_lengths)
    
    print(f"Title Statistics:")
    print(f"- Total posts: {len(posts)}")
    print(f"- Average title length: {average_length:.2f} characters")
    print(f"- Shortest title: {shortest_title} characters")
    print(f"- Longest title: {longest_title} characters")
    
    # Find posts by user
    user_post_count = {}
    for post in posts:
        user_id = post['userId']
        if user_id in user_post_count:
            user_post_count[user_id] += 1
        else:
            user_post_count[user_id] = 1
    
    print(f"\nPosts per user:")
    for user_id, count in user_post_count.items():
        print(f"User {user_id}: {count} posts")
```

## Common Patterns and Best Practices

### 1. Always Check Response Status
```python
import requests

url = 'https://api.example.com/data'
response = requests.get(url)

# Good practice: Always check status before processing
if response.status_code == 200:
    data = response.json()
    # Process data
elif response.status_code == 404:
    print("Data not found")
elif response.status_code == 500:
    print("Server error")
else:
    print(f"Unexpected status code: {response.status_code}")
```

### 2. Handle JSON Parsing Errors
```python
import requests
import json

url = 'https://api.example.com/data'
response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
        # Process data
    except json.JSONDecodeError:
        print("Response is not valid JSON")
        print("Raw response:", response.text)
else:
    print(f"Request failed: {response.status_code}")
```

### 3. Safe Dictionary Access
```python
# When working with API data, use .get() for safe access
user_data = {
    'name': 'John',
    'email': 'john@example.com'
    # 'phone' might not always be present
}

# Safe access with default values
name = user_data.get('name', 'Unknown')
phone = user_data.get('phone', 'Not provided')
address = user_data.get('address', {})

print(f"Name: {name}")
print(f"Phone: {phone}")
```

### 4. Processing Nested Data
```python
# API responses often contain nested dictionaries
user = {
    'name': 'John Doe',
    'contact': {
        'email': 'john@example.com',
        'address': {
            'street': '123 Main St',
            'city': 'Boston'
        }
    }
}

# Safe nested access
email = user.get('contact', {}).get('email', 'No email')
city = user.get('contact', {}).get('address', {}).get('city', 'No city')

print(f"Email: {email}")
print(f"City: {city}")
```

### 5. Iterating Through API Results
```python
import requests

# When API returns a list of items
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    
    # Process each user
    for index, user in enumerate(users, 1):
        name = user.get('name', 'Unknown')
        email = user.get('email', 'No email')
        company = user.get('company', {}).get('name', 'No company')
        
        print(f"{index}. {name}")
        print(f"   Email: {email}")
        print(f"   Company: {company}")
        print()
```

## Key Takeaways

### Dictionaries
- Use dictionaries for key-value data relationships
- Always use `.get()` for safe access to avoid KeyError
- Use `.items()` when you need both keys and values in loops
- Dictionaries are mutable and unordered (insertion order preserved in Python 3.7+)

### pip Package Management
- `pip install package_name` to install packages
- `pip freeze > requirements.txt` to save dependencies
- `pip install -r requirements.txt` to install from requirements
- Always work in virtual environments for project isolation

### REST APIs and requests
- Use `requests.get()` for HTTP GET requests
- Always check `response.status_code` before processing data
- Use `response.json()` to parse JSON responses
- Handle exceptions and errors gracefully

