# Python OOP Summary- class code
## 1. Basic Class Definition
```python
class Dog:
    def eat(self):
        print('eating boonzo')
    
    def bark(self):
        print('whroph whrooph')

# Creating objects (instances)
jojo = Dog()
jojo.eat()    # calling methods
jojo.bark()
```

## 2. Constructor (__init__)
```python
class Server:
    def __init__(self, name, ip):
        self.name = name      # instance attributes
        self.ip = ip

# Creating objects with parameters
s1 = Server('db', '1.1.1.1')
s2 = Server('backend', '2.2.2.2')
```

## 3. Instance Attributes vs Class Attributes
```python
class Dog:
    name = 'james'  # Class attribute (shared by all instances)
    
    def bark(self):
        print(f'{self.name} says : how how')

d1 = Dog()
d2 = Dog()
d2.name = 'pingpong'  # Instance attribute (specific to d2)
```

## 4. Magic Methods (Dunder Methods)
```python
class Employee:
    def __init__(self, name, salary, lastname):
        self.name = name
        self.salary = salary
        self.lastname = lastname
    
    def __str__(self):
        """Controls what print() shows"""
        return f'Employee: {self.name} {self.lastname}'
    
    def __int__(self):
        """Controls what int() conversion returns"""
        return self.salary

emp1 = Employee('hodi', 10000, 'zoubi')
print(emp1)      # Uses __str__
print(int(emp1)) # Uses __int__
```

## 5. Inheritance
```python
class Animal:  # Parent/Base class
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def walk(self):
        print('walking')

class Horse(Animal):  # Child/Derived class
    def __init__(self, name, color, height):
        super().__init__(name, color)  # Call parent constructor
        self.height = height           # Add new attribute

h1 = Horse('shamsham', 'white', 132)
h1.walk()  # Inherited method from Animal
```

## 6. Method Override
```python
class Shape:
    def __init__(self, area, hekef):
        self.area = area
        self.hekef = hekef
    
    def calc_area(self):
        self.area = 0  # Default implementation

class Circle(Shape):
    def __init__(self, hekef, radius):
        self.__radius = radius  # Private attribute
        super().__init__(self.calc_area(), hekef)
    
    def calc_area(self):  # Override parent method
        self.area = (self.__radius ** 2) * 3.14

class Rectangle(Shape):
    def calc_area(self):  # Override parent method
        self.area = self.a * self.b
```

## 7. Private Attributes
```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private (name mangling with __)
    
# c1.__radius  # This will cause an error!
# Access is restricted to within the class
```

## 8. Type Checking with isinstance()
```python
a1 = Animal('cookie', 'brown')
h1 = Horse('shamsham', 'white', 132)

print(isinstance(a1, Animal))    # True
print(isinstance(h1, Animal))    # True (inheritance)
print(isinstance(h1, Horse))     # True
print(isinstance(a1, Horse))     # False
```

## Key OOP Concepts Demonstrated

### 1. **Encapsulation**
- Bundling data and methods together in classes
- Using private attributes with `__attribute_name`

### 2. **Inheritance** 
- Child classes inherit from parent classes
- Use `super()` to call parent methods
- Child classes can override parent methods

### 3. **Polymorphism**
- Same method name (`calc_area`) behaves differently in different classes
- Objects of different types can be treated uniformly

### 4. **Abstraction**
- Hide implementation details behind method interfaces
- Users don't need to know how `calc_area()` works internally

## Common Patterns from the Code

### Constructor Pattern
```python
def __init__(self, param1, param2):
    self.attribute1 = param1
    self.attribute2 = param2
```

### Method Definition Pattern  
```python
def method_name(self, parameters):
    # method implementation
    return result
```

### Inheritance Pattern
```python
class Child(Parent):
    def __init__(self, child_params, parent_params):
        super().__init__(parent_params)
        self.child_attribute = child_params
```

### String Representation Pattern
```python
def __str__(self):
    return f"Description of {self.attribute}"
```

## Error Noted in Code
```python
# This line at the end will cause an AttributeError:
print(c1.__radius)  # Can't access private attribute directly
```

Private attributes should be accessed through public methods if needed, or use name mangling `_ClassName__attribute` (not recommended).

