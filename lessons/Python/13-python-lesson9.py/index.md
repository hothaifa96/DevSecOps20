# Python Object-Oriented Programming (OOP) Complete Tutorial

## Table of Contents
1. [Introduction to OOP](#introduction-to-oop)
2. [The Four Pillars of OOP](#the-four-pillars-of-oop)
3. [Encapsulation](#encapsulation)
4. [Abstraction](#abstraction)
5. [Inheritance](#inheritance)
6. [Polymorphism](#polymorphism)
7. [Import Systems in Python](#import-systems-in-python)
8. [Running Python from Terminal](#running-python-from-terminal)
9. [Code Analysis and Best Practices](#code-analysis-and-best-practices)

## Introduction to OOP

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects and classes. It's based on the concept of "objects" which contain data (attributes) and code (methods).

### Key Benefits:
- **Code Reusability**: Write once, use multiple times
- **Modularity**: Organize code into manageable pieces
- **Maintainability**: Easier to modify and extend
- **Real-world Modeling**: Map real-world entities to code objects

## The Four Pillars of OOP

### 1. Encapsulation
### 2. Abstraction
### 3. Inheritance
### 4. Polymorphism

---

## Encapsulation

**Definition**: Encapsulation is the bundling of data (attributes) and methods that operate on that data within a single unit (class). It also involves restricting access to some of the object's components.

### Access Modifiers in Python

```python
class BankAccount:
    def __init__(self, holder, balance, account_number):
        self.holder = holder           # Public attribute
        self._balance = balance        # Protected attribute (convention)
        self.__account_number = account_number  # Private attribute (name mangling)
    
    # Public method
    def get_balance(self):
        return self._balance
    
    # Public method to safely modify private data
    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Balance cannot be negative")
```

### Access Level Examples:

**Public** (`self.attribute`):
- Accessible from anywhere
- No restrictions

**Protected** (`self._attribute`):
- Convention-based privacy
- Intended for internal use and subclasses
- Can still be accessed but shouldn't be

**Private** (`self.__attribute`):
- Name mangling occurs
- Harder to access from outside
- Python changes the name internally

### Practical Example from Your Code:

```python
acc1 = CheckingAccount('roman', 1233, [], 15000)
acc1.__balance = 120_000  # This creates a NEW attribute, doesn't modify _balance!
acc1.set_balance(120000)  # Proper way to modify balance
print(acc1.get_balance())  # Proper way to access balance
```

**Important Note**: In your example, `acc1.__balance = 120_000` doesn't actually modify the internal `_balance`. It creates a completely new attribute called `__balance` on the instance!

---

## Abstraction

**Definition**: Abstraction means hiding complex implementation details while showing only essential features of an object. It defines a contract for what a class should do, not how it should do it.

### Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder, balance, account_number):
        self.holder = holder
        self._balance = balance
        self.account_number = account_number
    
    @abstractmethod
    def withdraw(self, amount):
        """Must be implemented by all subclasses"""
        pass
    
    @abstractmethod
    def deposit(self, amount):
        """Must be implemented by all subclasses"""
        pass
    
    @abstractmethod
    def get_balance(self):
        """Must be implemented by all subclasses"""
        pass
    
    @abstractmethod
    def set_balance(self, balance):
        """Must be implemented by all subclasses"""
        pass
    
    def __str__(self):
        return f'Balance: {self._balance}'
```

### Key Points about Abstraction:
- Cannot instantiate an abstract class directly
- Forces subclasses to implement required methods
- Provides a common interface for related classes
- Ensures consistency across implementations

### Why Use Abstraction?

```python
# This would raise an error:
# acc = BankAccount('John', 1000, 12345)  # TypeError!

# But this works because CheckingAccount implements all abstract methods:
acc = CheckingAccount('John', 12345, [], 15000)
```

---

## Inheritance

**Definition**: Inheritance allows a class (child/derived class) to inherit attributes and methods from another class (parent/base class). It promotes code reuse and establishes relationships between classes.

### Types of Inheritance:

#### Single Inheritance
```python
class BankAccount:  # Parent class
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

class CheckingAccount(BankAccount):  # Child class
    def __init__(self, holder, account_number, last_activities, credit_limit):
        super().__init__(holder, 0)  # Call parent constructor
        self.account_number = account_number
        self.last_activities = last_activities
        self.credit_limit = credit_limit
```

#### Method Resolution Order (MRO)

```python
class A:
    def method(self):
        print("A's method")

class B(A):
    def method(self):
        print("B's method")
        super().method()  # Call parent method

class C(B):
    def method(self):
        print("C's method")
        super().method()  # Call parent method

# Usage
obj = C()
obj.method()
# Output:
# C's method
# B's method
# A's method
```

### The `super()` Function

```python
class CheckingAccount(BankAccount):
    def __init__(self, holder, account_number, last_activities, credit_limit):
        # super() calls the parent class constructor
        super().__init__(holder, 0, account_number)
        self.last_activities = last_activities
        self.credit_limit = credit_limit
```

**Benefits of `super()`**:
- Maintains inheritance chain
- Allows for easy modification of parent class
- Supports multiple inheritance scenarios
- Makes code more maintainable

---

## Polymorphism

**Definition**: Polymorphism allows objects of different types to be treated as instances of the same type through a common interface. The same method name can behave differently based on the object that calls it.

### Types of Polymorphism:

#### Method Overriding
```python
class BankAccount(ABC):
    @abstractmethod
    def get_balance(self):
        pass

class CheckingAccount(BankAccount):
    def get_balance(self):
        return self._balance * 0.82  # After tax calculation

class SavingAccount(BankAccount):
    def get_balance(self):
        return self._balance * (1 + self.interest_rate)  # With interest
```

#### Duck Typing (Python's Approach)
```python
def process_account(account):
    """This function works with any object that has these methods"""
    account.deposit(100)
    print(f"Balance: {account.get_balance()}")
    account.withdraw(50)

# Works with any account type
checking = CheckingAccount('Alice', 12345, [], 5000)
savings = SavingAccount('Bob', 67890, '2024-01-01', 0.05)

process_account(checking)  # Uses CheckingAccount's methods
process_account(savings)   # Uses SavingAccount's methods
```

#### Operator Overloading
```python
class BankAccount:
    def __str__(self):  # Override string representation
        return f'Balance: {self._balance}'
    
    def __add__(self, other):  # Override + operator
        if isinstance(other, BankAccount):
            return self._balance + other._balance
        return self._balance + other
    
    def __eq__(self, other):  # Override == operator
        return self._balance == other._balance

# Usage
acc1 = CheckingAccount('Alice', 12345, [], 5000)
acc2 = CheckingAccount('Bob', 67890, [], 3000)

print(acc1)  # Calls __str__
total = acc1 + acc2  # Calls __add__
are_equal = acc1 == acc2  # Calls __eq__
```

---

## Import Systems in Python

### Types of Imports

#### 1. Standard Import
```python
import math
import os

# Usage
result = math.sqrt(16)
current_dir = os.getcwd()
```

#### 2. From Import
```python
from math import sqrt, pi
from os import getcwd

# Usage (no module prefix needed)
result = sqrt(16)
current_dir = getcwd()
```

#### 3. Wildcard Import (Use Sparingly!)
```python
from math import *

# Usage
result = sqrt(16)  # All functions available directly
```

#### 4. Aliased Import
```python
import numpy as np
from matplotlib import pyplot as plt

# Usage
array = np.array([1, 2, 3])
plt.plot(array)
```

### Local vs Global Imports

#### Global Import (at module level)
```python
# At the top of the file
from app.config import *
from eran_bank import *

def some_function():
    # config variables available here
    print(password)
```

#### Local Import (inside function)
```python
def some_function():
    from app.config import password  # Only imported when function is called
    from datetime import datetime
    
    print(password)
    return datetime.now()
```

### Project Structure Example
```
project/
├── main.py
├── app/
│   ├── __init__.py
│   ├── config.py
│   └── utils.py
├── eran_bank.py
└── tests/
    └── test_bank.py
```

#### config.py
```python
# app/config.py
DATABASE_URL = "postgresql://localhost:5432/bank"
SECRET_KEY = "your-secret-key"
DEBUG = True

def get_date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")
```

#### main.py
```python
# main.py
from app.config import *  # Imports all variables and functions
from eran_bank import *   # Imports all classes

# Now you can use:
print(SECRET_KEY)  # From config
print(get_date())  # From config
acc1 = CheckingAccount('roman', 1233, [], 15000)  # From eran_bank
```

### Import Best Practices

1. **Be Explicit**: Prefer specific imports over wildcards
2. **Organize Imports**: Standard library, third-party, then local
3. **Use Aliases**: For long module names
4. **Avoid Circular Imports**: Structure your code to prevent circular dependencies

```python
# Good practice
import os
import sys
from datetime import datetime

import requests
import numpy as np

from app.config import DATABASE_URL
from eran_bank import CheckingAccount
```

---

## Running Python from Terminal

### Basic Execution

#### Running a Python File
```bash
# Navigate to your project directory
cd /path/to/your/project

# Run the main file
python main.py

# Or with Python 3 specifically
python3 main.py
```

#### Running Python Interactively
```bash
# Start Python REPL
python

# Start with a specific file imported
python -i main.py
```

### Module Execution

#### The `if __name__ == '__main__':` Pattern

```python
# eran_bank.py
class CheckingAccount(BankAccount):
    # ... class definition ...

def main():
    """Main function for testing"""
    acc1 = CheckingAccount('roman', 1233, [], 15000)
    print('test', acc1)

if __name__ == '__main__':
    main()
```

**What this means**:
- When file is run directly: `__name__ == '__main__'` is True
- When file is imported: `__name__ == 'eran_bank'` (the module name)

#### Running as a Module
```bash
# If you have proper package structure
python -m app.main

# Run specific module
python -m eran_bank
```

### Command Line Arguments

```python
import sys

def main():
    if len(sys.argv) > 1:
        account_holder = sys.argv[1]
        initial_balance = float(sys.argv[2]) if len(sys.argv) > 2 else 0
    else:
        account_holder = 'Default User'
        initial_balance = 0
    
    acc = CheckingAccount(account_holder, 12345, [], initial_balance)
    print(f"Created account for {account_holder} with balance {initial_balance}")

if __name__ == '__main__':
    main()
```

```bash
# Usage
python eran_bank.py "John Doe" 1000
```

### Environment and Path

#### Setting PYTHONPATH
```bash
# Linux/Mac
export PYTHONPATH="${PYTHONPATH}:/path/to/your/project"

# Windows
set PYTHONPATH=%PYTHONPATH%;C:\path\to\your\project
```

#### Virtual Environments
```bash
# Create virtual environment
python -m venv myenv

# Activate (Linux/Mac)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Install packages
pip install requests numpy

# Deactivate
deactivate
```

---

## Code Analysis and Best Practices

### Analysis of Your Code

#### Issues Found:

1. **Encapsulation Misunderstanding**:
```python
acc1.__balance = 120_000  # This doesn't modify the internal _balance!
```
This creates a new attribute instead of modifying the protected `_balance`.

2. **Inconsistent Method Logic**:
```python
def get_balance(self):
    return self._balance * 0.82  # Why multiply by 0.82?

def set_balance(self, balance):
    self._balance = balance - 5.9  # Why subtract 5.9?
```

3. **Withdraw Method Issue**:
```python
def withdraw(self, amount):
    return amount if self._balance > amount else 0  # Should modify balance!
```

#### Improved Version:

```python
from abc import ABC, abstractmethod
from datetime import datetime

class BankAccount(ABC):
    def __init__(self, holder, balance, account_number):
        self.holder = holder
        self._balance = balance
        self.account_number = account_number
        self._transactions = []
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    def get_balance(self):
        """Default implementation - can be overridden"""
        return self._balance
    
    def set_balance(self, balance):
        """Safely set balance with validation"""
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = balance
        self._add_transaction("Balance Set", balance)
    
    def _add_transaction(self, transaction_type, amount):
        """Private method to track transactions"""
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'timestamp': datetime.now(),
            'balance': self._balance
        }
        self._transactions.append(transaction)
    
    def get_transaction_history(self):
        """Public method to view transactions"""
        return self._transactions.copy()  # Return copy to prevent external modification
    
    def __str__(self):
        return f'Account holder: {self.holder}, Balance: ${self._balance:,.2f}'

class CheckingAccount(BankAccount):
    TAX_RATE = 0.18  # Class constant
    SERVICE_FEE = 5.90  # Class constant
    
    def __init__(self, holder, account_number, last_activities, credit_limit):
        super().__init__(holder, 0, account_number)
        self.last_activities = last_activities
        self.credit_limit = credit_limit
    
    def withdraw(self, amount):
        """Withdraw money with overdraft protection"""
        if amount <= 0:
            return False
        
        available_balance = self._balance + self.credit_limit
        if amount <= available_balance:
            self._balance -= amount
            self._add_transaction("Withdrawal", -amount)
            return True
        return False
    
    def deposit(self, amount):
        """Deposit money to account"""
        if amount > 0:
            self._balance += amount
            self._add_transaction("Deposit", amount)
            return True
        return False
    
    def get_balance(self):
        """Get balance after tax calculation"""
        return self._balance * (1 - self.TAX_RATE)
    
    def set_balance(self, balance):
        """Set balance with service fee"""
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = balance - self.SERVICE_FEE
        self._add_transaction("Balance Set (with fee)", -self.SERVICE_FEE)

class SavingsAccount(BankAccount):
    def __init__(self, holder, account_number, interest_rate, minimum_balance=1000):
        super().__init__(holder, 0, account_number)
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        """Withdraw with minimum balance requirement"""
        if amount <= 0:
            return False
        
        if (self._balance - amount) >= self.minimum_balance:
            self._balance -= amount
            self._add_transaction("Withdrawal", -amount)
            return True
        return False
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self._balance += amount
            self._add_transaction("Deposit", amount)
            return True
        return False
    
    def apply_interest(self):
        """Apply monthly interest"""
        interest = self._balance * (self.interest_rate / 12)
        self._balance += interest
        self._add_transaction("Interest Applied", interest)

def main():
    """Main function for testing"""
    # Create accounts
    checking = CheckingAccount('Roman Smith', 1233, [], 15000)
    savings = SavingsAccount('Alice Johnson', 5678, 0.05, 500)
    
    # Test operations
    checking.deposit(1000)
    checking.withdraw(200)
    
    savings.deposit(2000)
    savings.apply_interest()
    
    # Display results
    print("=== Account Information ===")
    print(checking)
    print(f"Available balance: ${checking.get_balance():.2f}")
    print()
    print(savings)
    print(f"Balance with interest: ${savings.get_balance():.2f}")
    
    # Show transaction history
    print("\n=== Transaction History ===")
    for transaction in checking.get_transaction_history():
        print(f"{transaction['timestamp'].strftime('%Y-%m-%d %H:%M')} - "
              f"{transaction['type']}: ${transaction['amount']:,.2f}")

if __name__ == '__main__':
    main()
```

### Best Practices Summary

1. **Use meaningful variable names**
2. **Add proper error handling**
3. **Document your code with docstrings**
4. **Use constants for magic numbers**
5. **Follow the Single Responsibility Principle**
6. **Use proper access modifiers**
7. **Implement comprehensive testing**

### Testing Your OOP Code

```python
# test_bank.py
import unittest
from eran_bank import CheckingAccount, SavingsAccount

class TestBankAccounts(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.checking = CheckingAccount('Test User', 12345, [], 1000)
        self.savings = SavingsAccount('Test User', 67890, 0.05, 500)
    
    def test_deposit(self):
        """Test deposit functionality"""
        initial_balance = self.checking.get_balance()
        self.assertTrue(self.checking.deposit(500))
        self.assertGreater(self.checking.get_balance(), initial_balance)
    
    def test_withdraw(self):
        """Test withdrawal functionality"""
        self.checking.deposit(1000)
        initial_balance = self.checking.get_balance()
        self.assertTrue(self.checking.withdraw(200))
        self.assertLess(self.checking.get_balance(), initial_balance)
    
    def test_negative_deposit(self):
        """Test that negative deposits are rejected"""
        self.assertFalse(self.checking.deposit(-100))

if __name__ == '__main__':
    unittest.main()
```

---

# And 
- **Encapsulation** protects data and provides controlled access
- **Abstraction** hides complexity and defines contracts
- **Inheritance** promotes code reuse and establishes relationships
- **Polymorphism** enables flexible and extensible designs
