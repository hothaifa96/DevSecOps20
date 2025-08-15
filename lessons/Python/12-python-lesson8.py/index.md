# Python Classes, Instances & Object-Oriented Programming - Complete Guide

## Table of Contents

1. [Introduction to Object-Oriented Programming](#introduction-to-object-oriented-programming)
2. [Classes and Objects](#classes-and-objects)
3. [Creating Classes](#creating-classes)
4. [Instances and Instance Variables](#instances-and-instance-variables)
5. [Methods](#methods)
6. [The `__init__` Method (Constructor)](#the-__init__-method-constructor)
7. [Instance vs Class Variables](#instance-vs-class-variables)
8. [Method Types](#method-types)
9. [Inheritance](#inheritance)
10. [Encapsulation](#encapsulation)
11. [Polymorphism](#polymorphism)
12. [Special Methods (Magic Methods)](#special-methods-magic-methods)
13. [Property Decorators](#property-decorators)
14. [Abstract Classes](#abstract-classes)
15. [Best Practices](#best-practices)
16. [Common Pitfalls](#common-pitfalls)
17. [Practice Exercises](#practice-exercises)

---

## Introduction to Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which contain data (attributes) and code (methods). Python supports OOP and provides all the standard features needed to create robust, maintainable applications.

### Key OOP Concepts:

- **Encapsulation**: Bundling data and methods that work on that data within one unit
- **Inheritance**: Creating new classes based on existing classes
- **Polymorphism**: The ability of different objects to respond to the same interface
- **Abstraction**: Hiding complex implementation details and showing only essential features

---

## Classes and Objects

### What is a Class?

A class is a blueprint or template for creating objects. It defines the attributes and methods that objects of that class will have.

### What is an Object/Instance?

An object (also called an instance) is a specific realization of a class. It's created from the class template and has actual values for the attributes defined in the class.

```python
# Think of it like this:
# Class = Blueprint of a house
# Object/Instance = Actual house built from that blueprint
```

---

## Creating Classes

### Basic Class Syntax

```python
class ClassName:
    """Class docstring"""
    # Class body
    pass
```

### Simple Example

```python
class Dog:
    """A simple Dog class"""

    # Class variable (shared by all instances)
    species = "Canis lupus"

    def bark(self):
        return "Woof!"

# Creating an instance
my_dog = Dog()
print(my_dog.species)  # Output: Canis lupus
print(my_dog.bark())   # Output: Woof!
```

---

## Instances and Instance Variables

### Creating Instances

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

# Creating instances
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30
```

### Instance Variables

Instance variables are unique to each instance of a class. They are typically defined in the `__init__` method.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make      # Instance variable
        self.model = model    # Instance variable
        self.year = year      # Instance variable
        self.odometer = 0     # Instance variable with default value

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

# Each instance has its own set of variables
print(car1.make)   # Output: Toyota
print(car2.make)   # Output: Honda
```

---

## Methods

### Instance Methods

Instance methods are functions defined inside a class that operate on instances of that class.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def display_info(self):
        """Display rectangle information"""
        print(f"Rectangle: {self.width}x{self.height}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

# Using the methods
rect = Rectangle(5, 3)
rect.display_info()
```

### The `self` Parameter

- `self` refers to the instance of the class
- It must be the first parameter of instance methods
- It's automatically passed when calling methods on an instance

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

counter = Counter()
counter.increment()  # Python automatically passes 'counter' as 'self'
print(counter.get_count())  # Output: 1
```

---

## The `__init__` Method (Constructor)

The `__init__` method is a special method called when an instance is created. It's used to initialize the instance's attributes.

```python
class Student:
    def __init__(self, name, student_id, grade=None):
        """Initialize a new student"""
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.courses = []  # Empty list for courses

    def add_course(self, course):
        """Add a course to the student's course list"""
        self.courses.append(course)

    def display_info(self):
        """Display student information"""
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Grade: {self.grade}")
        print(f"Courses: {', '.join(self.courses)}")

# Creating students
student1 = Student("Emma", "S001", "A")
student2 = Student("Jake", "S002")  # grade defaults to None

student1.add_course("Math")
student1.add_course("Science")
student1.display_info()
```

---

## Instance vs Class Variables

### Instance Variables

- Unique to each instance
- Defined in `__init__` or other instance methods
- Accessed with `self.variable_name`

### Class Variables

- Shared by all instances of the class
- Defined directly in the class body
- Accessed with `ClassName.variable_name` or `self.variable_name`

```python
class Employee:
    # Class variables
    company_name = "TechCorp"
    employee_count = 0

    def __init__(self, name, position, salary):
        # Instance variables
        self.name = name
        self.position = position
        self.salary = salary

        # Increment class variable when new employee is created
        Employee.employee_count += 1

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Company: {self.company_name}")
        print(f"Total Employees: {Employee.employee_count}")

# Creating employees
emp1 = Employee("Alice", "Developer", 70000)
emp2 = Employee("Bob", "Designer", 65000)

print(f"Company: {Employee.company_name}")
print(f"Total Employees: {Employee.employee_count}")  # Output: 2
```

### Important Note About Class Variables

```python
class Example:
    class_var = []  # Dangerous! Shared mutable object

    def __init__(self, name):
        self.name = name
        self.class_var.append(name)  # This modifies the shared list!

# This can lead to unexpected behavior
obj1 = Example("A")
obj2 = Example("B")
print(obj1.class_var)  # Output: ['A', 'B'] - Unexpected!

# Better approach:
class BetterExample:
    def __init__(self, name):
        self.name = name
        self.instance_list = []  # Each instance gets its own list
```

---

## Method Types

### 1. Instance Methods

Regular methods that operate on instance data.

### 2. Class Methods

Methods that operate on the class itself, not on instances.

```python
class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def get_population(cls):
        """Class method to get total population"""
        return cls.population

    @classmethod
    def create_baby(cls, name):
        """Class method that returns a new instance"""
        return cls(name, 0)

# Using class methods
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(Person.get_population())  # Output: 2
baby = Person.create_baby("Charlie")
print(Person.get_population())  # Output: 3
```

### 3. Static Methods

Methods that don't access instance or class data.

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        """Static method for addition"""
        return x + y

    @staticmethod
    def is_even(number):
        """Check if a number is even"""
        return number % 2 == 0

# Using static methods
result = MathUtils.add(5, 3)  # Output: 8
print(MathUtils.is_even(4))   # Output: True

# Can also be called on instances
utils = MathUtils()
print(utils.add(2, 3))  # Output: 5
```

---

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

### Basic Inheritance

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"

    def info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent's __init__
        self.breed = breed

    def make_sound(self):  # Override parent method
        return "Woof!"

    def fetch(self):  # New method specific to Dog
        return f"{self.name} is fetching the ball!"

class Cat(Animal):  # Cat also inherits from Animal
    def __init__(self, name, indoor):
        super().__init__(name, "Cat")
        self.indoor = indoor

    def make_sound(self):  # Override parent method
        return "Meow!"

    def climb(self):  # New method specific to Cat
        return f"{self.name} is climbing!"

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", True)

print(dog.info())        # Inherited method
print(dog.make_sound())  # Overridden method
print(dog.fetch())       # New method

print(cat.info())        # Inherited method
print(cat.make_sound())  # Overridden method
print(cat.climb())       # New method
```

### Multiple Inheritance

```python
class Flyable:
    def fly(self):
        return "Flying through the air!"

class Swimmable:
    def swim(self):
        return "Swimming through water!"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Duck")

    def make_sound(self):
        return "Quack!"

duck = Duck("Donald")
print(duck.info())   # From Animal
print(duck.fly())    # From Flyable
print(duck.swim())   # From Swimmable
print(duck.make_sound())  # Overridden
```

---

## Encapsulation

Encapsulation is about bundling data and methods together and restricting access to some components.

### Public, Protected, and Private Attributes

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public
        self._balance = balance               # Protected (convention)
        self.__pin = "1234"                   # Private (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount, pin):
        if self.__verify_pin(pin) and amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Invalid withdrawal"

    def __verify_pin(self, pin):  # Private method
        return pin == self.__pin

    def get_balance(self):  # Public method to access protected data
        return self._balance

account = BankAccount("123456", 1000)

# Public access
print(account.account_number)  # Works fine

# Protected access (still accessible but discouraged)
print(account._balance)  # Works but not recommended

# Private access (name mangling makes it harder to access)
# print(account.__pin)  # AttributeError
# But still accessible as: account._BankAccount__pin

print(account.deposit(500))
print(account.withdraw(200, "1234"))
```

### Property Decorators for Encapsulation

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter for radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for radius with validation"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Calculated property"""
        return 3.14159 * self._radius ** 2

    @property
    def diameter(self):
        """Calculated property"""
        return 2 * self._radius

circle = Circle(5)
print(circle.radius)    # Output: 5
print(circle.area)      # Output: 78.53975
print(circle.diameter)  # Output: 10

circle.radius = 3  # Uses setter
print(circle.area)  # Output: 28.27431

# circle.radius = -1  # Raises ValueError
```

---

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common base class.

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Polymorphism in action
shapes = [
    Rectangle(5, 3),
    Circle(2),
    Rectangle(4, 4)
]

for shape in shapes:
    print(f"Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
```

---

## Special Methods (Magic Methods)

Special methods (also called magic methods or dunder methods) allow you to define how objects behave with built-in operations.

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """String representation for end users"""
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        """String representation for developers"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        """Return length (number of pages)"""
        return self.pages

    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Book):
            return (self.title == other.title and
                   self.author == other.author)
        return False

    def __lt__(self, other):
        """Less than comparison (by pages)"""
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented

    def __add__(self, other):
        """Addition (combine pages)"""
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented

book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)
book3 = Book("1984", "George Orwell", 328)

print(book1)           # Uses __str__
print(repr(book1))     # Uses __repr__
print(len(book1))      # Uses __len__
print(book1 == book3)  # Uses __eq__
print(book1 < book2)   # Uses __lt__
print(book1 + book2)   # Uses __add__
```

### Common Special Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)    # Vector(4, 6)
print(v1 - v2)    # Vector(2, 2)
print(v1 * 2)     # Vector(6, 8)
print(abs(v1))    # 5.0
print(v1[0])      # 3 (using __getitem__)
v1[0] = 5         # Using __setitem__
print(v1)         # Vector(5, 4)
```

---

## Property Decorators

Properties allow you to access methods like attributes, enabling better encapsulation.

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature using Fahrenheit"""
        self.celsius = (value - 32) * 5/9

    @property
    def kelvin(self):
        """Get temperature in Kelvin"""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        """Set temperature using Kelvin"""
        self.celsius = value - 273.15

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
print(temp.kelvin)      # 298.15

temp.fahrenheit = 100
print(temp.celsius)     # 37.77777777777778

temp.kelvin = 300
print(temp.celsius)     # 26.85
```

---

## Abstract Classes

Abstract classes cannot be instantiated and are meant to be subclassed.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        """Abstract method - must be implemented by subclasses"""
        pass

    @abstractmethod
    def move(self):
        """Abstract method - must be implemented by subclasses"""
        pass

    def sleep(self):
        """Concrete method - can be used by subclasses"""
        return f"{self.name} is sleeping"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Running on four legs"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

    def move(self):
        return "Flying with wings"

# animal = Animal("Generic")  # TypeError - cannot instantiate abstract class
dog = Dog("Buddy")
bird = Bird("Tweety")

print(dog.make_sound())  # Woof!
print(bird.move())       # Flying with wings
print(dog.sleep())       # Buddy is sleeping
```

---

## Best Practices

### 1. Class Naming

```python
# Use PascalCase for class names
class StudentRecord:    # Good
    pass

class student_record:   # Bad
    pass
```

### 2. Method Naming

```python
class Calculator:
    def add_numbers(self, a, b):     # Good - descriptive
        return a + b

    def calc(self, a, b):            # Bad - not descriptive
        return a + b
```

### 3. Use Properties for Validation

```python
class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value
```

### 4. Composition Over Inheritance

```python
# Instead of complex inheritance hierarchies
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        return self.engine.start()
```

### 5. Use `__slots__` for Memory Optimization

```python
class Point:
    __slots__ = ['x', 'y']  # Restricts attributes and saves memory

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## Common Pitfalls

### 1. Mutable Default Arguments

```python
# Bad
class MyClass:
    def __init__(self, items=[]):  # Dangerous!
        self.items = items

# Good
class MyClass:
    def __init__(self, items=None):
        self.items = items if items is not None else []
```

### 2. Forgetting `self`

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        count += 1  # Error! Should be self.count += 1
```

### 3. Not Using `super()` in Inheritance

```python
# Bad
class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self, name)  # Fragile
        self.age = age

# Good
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Robust
        self.age = age
```

---

## Practice Exercises

### Exercise 1: Basic Class Creation

Create a `Book` class with the following requirements:

- Attributes: title, author, isbn, pages
- Methods: display_info(), is_long_book() (returns True if > 300 pages)

### Exercise 2: Inheritance

Create a `Vehicle` base class and `Car` and `Motorcycle` subclasses:

- Vehicle should have make, model, year
- Car should add number_of_doors
- Motorcycle should add engine_size
- All should have a start_engine() method

### Exercise 3: Encapsulation

Create a `BankAccount` class with:

- Private balance attribute
- deposit() and withdraw() methods with validation
- Property for read-only account balance

### Exercise 4: Polymorphism

Create different shape classes (Circle, Rectangle, Triangle) that all implement area() and perimeter() methods. Create a function that can calculate total area of a list of mixed shapes.

### Exercise 5: Advanced Features

Create a `Student` class that:

- Uses properties for grade validation (0-100)
- Implements comparison operators based on grades
- Has a class method to create honor students (grade >= 90)
- Uses `__str__` and `__repr__` appropriately

---
