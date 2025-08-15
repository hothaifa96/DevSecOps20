# Python Concepts Cheatsheet for Tic-Tac-Toe Project

## 1. Working with Nested Lists (2D Arrays)

### Creating and Accessing
```python
# Create a shopping cart as nested list
shopping_list = [
    ["apples", "bananas", "oranges"],
    ["bread", "milk", "eggs"],
    ["chicken", "beef", "fish"]
]

# Access specific item
item = shopping_list[1][2]  # Gets "eggs"
print(item)

# Modify specific item
shopping_list[0][1] = "grapes"  # Changes "bananas" to "grapes"
```

### Iterating Through Nested Lists
```python
# Print all items in categories
for category in shopping_list:
    for item in category:
        print(f"- {item}")

# Check if specific item exists
def find_item(cart, target):
    for row in cart:
        if target in row:
            return True
    return False
```

## 2. Input Validation Patterns

### Basic Number Validation
```python
def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 18 <= age <= 100:
                return age
            else:
                print("Age must be between 18-100")
        except ValueError:
            print("Please enter a valid number")

# Usage
user_age = get_age()
```

### Range and Condition Validation
```python
def get_menu_choice():
    menu = ["Pizza", "Burger", "Salad"]
    
    while True:
        print("Menu:")
        for i, item in enumerate(menu):
            print(f"{i}: {item}")
        
        try:
            choice = int(input("Choose (0-2): "))
            if 0 <= choice < len(menu):
                return choice
            else:
                print(f"Please choose 0-{len(menu)-1}")
        except ValueError:
            print("Enter numbers only!")
```

## 3. Function Organization

### Single Responsibility Functions
```python
# Each function does ONE thing
def calculate_tax(price):
    return price * 0.17

def format_price(amount):
    return f"₪{amount:.2f}"

def get_total_with_tax(price):
    tax = calculate_tax(price)
    return price + tax

# Usage
item_price = 100
total = get_total_with_tax(item_price)
formatted = format_price(total)
print(f"Total: {formatted}")
```

### Functions with Multiple Return Values
```python
def get_student_info():
    name = input("Enter name: ")
    grade = int(input("Enter grade: "))
    return name, grade  # Returns tuple

def validate_credentials(username, password):
    if len(username) < 3:
        return False, "Username too short"
    if len(password) < 6:
        return False, "Password too short"
    return True, "Valid credentials"

# Usage
is_valid, message = validate_credentials("john", "123")
print(message)
```

## 4. Loop Control and Conditions

### While Loops with Multiple Conditions
```python
def atm_withdrawal():
    balance = 1000
    attempts = 0
    max_attempts = 3
    
    while balance > 0 and attempts < max_attempts:
        try:
            amount = int(input(f"Balance: ₪{balance}. Withdraw how much? "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrew ₪{amount}")
                break
            else:
                print("Insufficient funds!")
        except ValueError:
            print("Enter valid amount!")
        
        attempts += 1
    
    if attempts >= max_attempts:
        print("Too many attempts!")
```

### Pattern Matching with Conditions
```python
def check_grade(score):
    if score >= 90:
        return "A", "Excellent"
    elif score >= 80:
        return "B", "Good"
    elif score >= 70:
        return "C", "Average"
    elif score >= 60:
        return "D", "Pass"
    else:
        return "F", "Fail"

# Check multiple conditions
def analyze_weather(temp, humidity, wind):
    conditions = []
    
    if temp > 30:
        conditions.append("hot")
    elif temp < 10:
        conditions.append("cold")
    
    if humidity > 80:
        conditions.append("humid")
    
    if wind > 20:
        conditions.append("windy")
    
    return conditions if conditions else ["pleasant"]
```

## 5. List Operations and Checks

### Checking List Contents
```python
# Example: Parking lot management
parking_spots = ["car1", "empty", "car2", "empty", "car3"]

def find_empty_spot(spots):
    for i, spot in enumerate(spots):
        if spot == "empty":
            return i
    return -1  # No empty spots

def is_lot_full(spots):
    return "empty" not in spots

def count_cars(spots):
    return len([spot for spot in spots if spot != "empty"])
```

### List Modifications
```python
# Example: Restaurant seating
tables = [
    ["empty", "empty", "empty", "empty"],
    ["John", "empty", "Mary", "empty"],
    ["empty", "Bob", "empty", "Alice"]
]

def seat_customer(tables, customer_name):
    for row_idx, row in enumerate(tables):
        for col_idx, seat in enumerate(row):
            if seat == "empty":
                tables[row_idx][col_idx] = customer_name
                return row_idx, col_idx
    return None, None  # No seats available

def free_table(tables, row, col):
    if tables[row][col] != "empty":
        tables[row][col] = "empty"
        return True
    return False
```

## 6. String and Character Operations

### String Comparisons and Manipulations
```python
def process_user_input(text):
    # Clean input
    cleaned = text.strip().lower()
    
    # Validate
    if not cleaned:
        return None, "Empty input"
    
    if len(cleaned) > 20:
        return None, "Input too long"
    
    return cleaned, "Valid"

# Character checking
def validate_game_symbol(symbol):
    allowed_symbols = ['X', 'O', '*', '+']
    return symbol.upper() in allowed_symbols

# Multiple string checks
def analyze_password(password):
    checks = {
        'length': len(password) >= 8,
        'has_number': any(c.isdigit() for c in password),
        'has_letter': any(c.isalpha() for c in password),
        'has_special': any(not c.isalnum() for c in password)
    }
    return checks
```

## 7. Error Handling Patterns

### Comprehensive Input Handling
```python
def safe_input(prompt, input_type=str, validator=None):
    while True:
        try:
            user_input = input(prompt).strip()
            
            # Handle empty input
            if not user_input:
                print("Input cannot be empty!")
                continue
            
            # Convert type
            if input_type == int:
                value = int(user_input)
            elif input_type == float:
                value = float(user_input)
            else:
                value = user_input
            
            # Custom validation
            if validator and not validator(value):
                print("Invalid input!")
                continue
                
            return value
            
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}!")
        except KeyboardInterrupt:
            print("\nExiting...")
            return None

# Usage examples
age = safe_input("Enter age: ", int, lambda x: 0 < x < 120)
email = safe_input("Enter email: ", str, lambda x: "@" in x)
```

## 8. Game State Management

### State Tracking
```python
# Example: Quiz game state
class QuizState:
    def __init__(self):
        self.questions = [
            {"q": "What is 2+2?", "a": "4"},
            {"q": "Capital of France?", "a": "Paris"},
            {"q": "Largest planet?", "a": "Jupiter"}
        ]
        self.current_question = 0
        self.score = 0
        self.is_finished = False
    
    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
        else:
            self.is_finished = True
    
    def check_answer(self, answer):
        correct_answer = self.questions[self.current_question]["a"]
        if answer.strip().lower() == correct_answer.lower():
            self.score += 1
            return True
        return False

# Simpler state with dictionaries
game_state = {
    "player_turn": "player1",
    "moves_made": 0,
    "game_over": False,
    "winner": None
}

def switch_player(state):
    state["player_turn"] = "player2" if state["player_turn"] == "player1" else "player1"
    state["moves_made"] += 1
```

## 9. Pattern Recognition

### Checking Patterns in Data
```python
# Example: Check patterns in a grid
grid = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

def check_diagonal_pattern(grid):
    # Main diagonal
    main_diag = [grid[i][i] for i in range(len(grid))]
    
    # Anti-diagonal  
    anti_diag = [grid[i][len(grid)-1-i] for i in range(len(grid))]
    
    return main_diag, anti_diag

def find_sequence(grid, target_length):
    """Find sequences of identical elements"""
    sequences = []
    
    # Check rows
    for row in grid:
        current_seq = []
        for item in row:
            if current_seq and item != current_seq[-1]:
                if len(current_seq) >= target_length:
                    sequences.append(current_seq.copy())
                current_seq = [item]
            else:
                current_seq.append(item)
    
    return sequences
```

