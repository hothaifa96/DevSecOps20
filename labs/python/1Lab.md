# Python Lab Tasks - Story-Based Programming Challenges

## 📋 Lab Overview

Welcome to your Python programming lab! You'll complete 5 story-based challenges that will test your understanding of all the concepts from Lesson 1. Each task builds upon the previous one, so complete them in order.

**Estimated Time:** 2-3 hours  
**Difficulty:** Beginner to Intermediate  
**Required Knowledge:** Python Lesson 1 concepts

---


## 📝 Task 1: The Pizza Party Problem 🍕

### Story Background
You're hosting a pizza party for your friends! You've ordered several delicious pizzas, and each pizza has 8 slices. Now comes the tricky part - you need to figure out how many slices each friend gets and if there will be any leftover slices for you to enjoy later.

Your friends are already at the door, and they're getting hungry. You need to solve this quickly before they start complaining!

### Your Mission
Create a Python program that:
1. Asks how many pizzas you ordered
2. Asks how many friends are coming to the party
3. Calculates how many slices each person gets (using floor division)
4. Calculates how many slices will be left over (using modulo)
5. Displays a nicely formatted result

### Requirements
- Use `int()` to convert user input
- Use floor division (`//`) for slices per person
- Use modulo (`%`) for leftover slices
- Each pizza has exactly 8 slices
- Use f-strings for output formatting
- Include decorative borders in your output

### Sample Output
```
How many pizzas did you order? 3
How many friends are coming? 7

========================================
You ordered 3 pizza(s)
You have 7 friends coming
Total slices available: 24
Each person gets: 3 slices
Leftover slices: 3
========================================
Great! You get 3 extra slice(s)!
```

### Python Concepts Used
- Variables and assignment
- `int()` type casting
- `input()` function
- Mathematical operators (`*`, `//`, `%`)
- F-strings
- Conditional statements (`if/else`)

### Hints
- Remember: `total_slices = pizzas * 8`
- Use `//` for whole slices (no fractions!)
- Use `%` to find the remainder
- Example: `17 // 5 = 3` and `17 % 5 = 2`

---

## 📝 Task 2: The Corner Store Adventure 🏪

### Story Background
You're working part-time at your neighborhood corner store. A customer walks in wanting to buy some snacks, but they only have a $20 bill. They want to know exactly how much they can spend and what their change will be.

The store owner trusts you to handle this transaction properly. You need to create a quick calculator to help the customer make their decision!

### Your Mission
Create a Python program that:
1. Greets the customer and asks for their name
2. Asks for the total price of items they want to buy
3. Calculates change from a $20 bill
4. Determines if they have enough money
5. Provides different messages based on the change amount
6. Creates a formatted receipt

### Requirements
- Use `input()` for customer name
- Use `float()` for price input (to handle cents)
- Store the $20 bill amount in a variable
- Use comparison operators to check if they have enough money
- Use string methods like `.upper()` for formatting
- Include conditional logic for different scenarios
- Format money to 2 decimal places using `:.2f`

### Sample Output
```
🏪 Welcome to Corner Store Helper! 🛒
-----------------------------------
What's your name? Alice
Nice to meet you, Alice! 😊
What's the total price of your items? $15.75

===================================
RECEIPT FOR ALICE
Money available: $20.00
Total cost: $15.75
Your change: $4.25
Transaction approved! 🎉
You could buy some gum with that change!
```

### Python Concepts Used
- Variables
- `input()` and `float()` functions
- String methods (`.upper()`)
- Boolean variables
- Comparison operators (`>=`, `<`)
- F-strings with number formatting
- Conditional statements

### Hints
- Use `float()` for prices that include cents
- Store `has_enough_money = money_available >= item_price`
- Use `:.2f` in f-strings to format money: `f"${amount:.2f}"`
- Create different messages for different change amounts

---

## 📝 Task 3: The Gaming Tournament 🎮

### Story Background
You're organizing a gaming tournament at your local community center. Players need to register, and you need to check if they meet the requirements: they must be at least 13 years old and have their own gaming controller.

The tournament is starting soon, and you have a line of excited gamers waiting to sign up. You need a quick registration system!

### Your Mission
Create a registration system that:
1. Gets the player's gamer name and age
2. Asks if they have their own controller (yes/no)
3. Validates both requirements
4. Generates a unique player ID
5. Assigns players to age-appropriate divisions
6. Displays a complete registration card

### Requirements
- Use `int()` for age conversion
- Convert controller input to boolean using string comparison
- Use logical operators (`and`) to combine conditions
- Generate a player ID using mathematical operations
- Use multiple conditional statements for age divisions
- Include both approval and denial scenarios

### Sample Output
```
🎮 GAMING TOURNAMENT REGISTRATION 🏆
****************************************
Requirements: Age 13+, Own controller
****************************************
Enter your gamer name: PyThonMaster
Enter your age: 16
Do you have your own controller? (yes/no): yes

=============================================

Player: PyThonMaster
Age: 16 years old
Has controller: True
Player ID: 192
Age requirement (13+): True

---------------------------------------------
REGISTRATION APPROVED!
Welcome to the tournament!
You'll compete in: Adult Division
Tournament starts in 30 minutes!
=============================================
```

### Python Concepts Used
- Boolean variables and logic
- String methods (`.lower()`, `.upper()`)
- Logical operators (`and`)
- Comparison operators
- Type casting
- Built-in functions (`len()`)
- Complex conditional statements

### Hints
- Use `controller_input.lower() == 'yes'` to create a boolean
- Combine conditions: `can_participate = meets_age_requirement and has_controller`
- Generate ID: `player_id = len(player_name) * age`
- Age divisions: Junior (13-15), Adult (16-24), Veteran (25+)

---

## 📝 Task 4: The Secret Message 📱

### Story Background
You and your best friend have decided to create a secret messaging system! You want to encode messages by creating special patterns and formatting. Your friend is waiting for you to send the first coded message.

The code works by taking a person's name and a secret word, then creating a special formatted message with patterns and repetitions.

### Your Mission
Create a secret message encoder that:
1. Gets sender and recipient names
2. Gets a secret word to encode
3. Creates decorative borders using string repetition
4. Encodes the secret word using a simple cipher
5. Formats everything into a secret transmission
6. Provides decoding statistics

### Requirements
- Use string repetition (`*`) for borders
- Use `len()` to determine border lengths
- Implement a simple Caesar cipher (shift letters by 1)
- Use multiline strings with triple quotes (`"""`)
- Include multiple f-string examples
- Use string methods for case conversion
- Create dynamic borders based on word length

### Sample Output
```
🕵️ SECRET MESSAGE ENCODER 🔐
===================================
Enter your name: Alice
Who is this message for? Bob
Enter your secret word: python

************************************************
*      SECRET MESSAGE TRANSMISSION      *
************************************************

FROM: ALICE
TO: BOB
STATUS: ENCRYPTED 

--------------------
SECRET CODE: QZUIPO
ORIGINAL LENGTH: 6 characters
DECODE HINT: Shift each letter back by 1
--------------------

DECRYPTION FORMULA:
python --> qzuipo

MESSAGE ENDS HERE
************************************************

MESSAGE STATISTICS:
Original word: ****** (6 chars)
Encoded word: qzuipo
Encryption key: Caesar cipher (+1)
Border length: 48 characters
From Alice to Bob

Hint: PSST! Bob, to decode 'qzuipo', shift each letter backward!
```

### Python Concepts Used
- String repetition with `*`
- String concatenation with `+`
- `len()` function
- F-strings and multiline strings
- String methods (`.upper()`, `.lower()`)
- For loops and string iteration
- `ord()` and `chr()` functions for ASCII manipulation
- Advanced string formatting

### Hints
- Create borders: `border = "*" * (len(secret_word) + 20)`
- For Caesar cipher: `new_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))`
- Use triple quotes for multiline formatted output
- Combine f-strings with multiline strings for complex formatting

---

## 📝 Task 5: The Grade Calculator Challenge 🎯

### Story Background
It's the end of the semester, and you're helping your teacher calculate final grades for the class. Each student has taken 3 exams and completed several homework assignments. You need to create a comprehensive grade calculator that determines their final grade and letter grade.

This is the most important calculation of the semester - students are anxiously waiting for their results!

### Your Mission
Create a complete grade calculator that:
1. Collects student information (name, ID, course)
2. Gets all exam scores (3 exams)
3. Gets homework scores (variable number of assignments)
4. Calculates weighted final grade (exams 70%, homework 30%)
5. Determines letter grade and pass/fail status
6. Analyzes performance trends
7. Generates a comprehensive report

### Requirements
- Use loops to collect multiple homework scores
- Implement weighted average calculation
- Use multiple conditional statements for letter grades
- Use built-in functions (`max()`, `min()`)
- Include performance analysis and improvement tracking
- Create a professional-looking report format
- Handle edge cases (no homework, perfect scores, etc.)

### Sample Input/Output
```
🎓 FINAL GRADE CALCULATOR 📊
==================================================
Enter student information and exam scores
==================================================
Student's full name: John Smith
Student ID: 12345
Course name: Introduction to Python

📝 Entering grades for John Smith...
------------------------------
Enter Exam 1 score (0-100): 85
Enter Exam 2 score (0-100): 92
Enter Exam 3 score (0-100): 88
How many homework assignments? 4

Enter 4 homework scores:
Homework 1 score: 95
Homework 2 score: 87
Homework 3 score: 91
Homework 4 score: 89

============================================================
OFFICIAL GRADE REPORT FOR JOHN SMITH
============================================================
Student ID: 12345
Course: Introduction to Python
Report Date: 2025-07-19
------------------------------------------------------------

EXAM SCORES:
   Exam 1: 85.0%
   Exam 2: 92.0%
   Exam 3: 88.0%
   Average: 88.33%

HOMEWORK SCORES:
   Total assignments: 4
   Total points: 362.0
   Average: 90.50%

FINAL CALCULATION:
   Exams (70%): 88.33 × 0.7 = 61.83
   Homework (30%): 90.50 × 0.3 = 27.15
   FINAL GRADE: 88.98%

GRADE SUMMARY:
   Letter Grade: B
   Status: PASSED 
   Comment: Good job! 

PERFORMANCE ANALYSIS:
   Highest exam score: 92.0%
   Lowest exam score: 85.0%
   Score range: 7.0 points
   Improvement: +3.0 points (getting better! 📈)

Great work! Keep it up!
============================================================
Report generated by Python Grade Calculator v1.0
============================================================
```

### Python Concepts Used
- **All concepts from previous tasks PLUS:**
- For loops with `range()`
- Accumulator pattern (`total += value`)
- Built-in functions (`max()`, `min()`)
- Complex conditional logic (`if/elif/else`)
- Mathematical calculations with multiple variables
- Advanced f-string formatting
- Multiple data types working together

### Hints
- Use a loop: `for i in range(hw_count):`
- Accumulator pattern: `total_hw_score += hw_score`
- Weighted average: `final = (exam_avg * 0.7) + (hw_avg * 0.3)`
- Grade ranges: A(90+), B(80+), C(70+), D(60+), F(<60)
- Use `max(exam1, exam2, exam3)` and `min(exam1, exam2, exam3)`
- Track improvement: `improvement = exam3 - exam1`

---

## 🏆 Bonus Challenges

After completing all 5 tasks, try these bonus challenges:

### Bonus 1: Error Handling
Add input validation to any of your programs:
- Check if numbers are in valid ranges
- Handle invalid yes/no responses
- Ensure grades are between 0-100

### Bonus 2: Enhanced Features
- Add color output using ANSI codes
- Save results to a text file
- Create a menu system to run multiple calculators

### Bonus 3: Code Optimization
- Combine multiple programs into one menu-driven application
- Create reusable functions for common operations
- Add more sophisticated calculations

---

## 📚 Assessment Rubric

### Excellent (90-100%)
- All 5 tasks completed correctly
- Code is well-formatted and readable
- Proper use of all required Python concepts
- Creative additions or improvements
- Comprehensive testing with different inputs

### Good (80-89%)
- 4-5 tasks completed correctly
- Minor errors in formatting or logic
- Most Python concepts used properly
- Good code organization

### Satisfactory (70-79%)
- 3-4 tasks completed
- Some errors in implementation
- Basic Python concepts demonstrated
- Code runs but may have issues

### Needs Improvement (60-69%)
- 1-2 tasks completed
- Significant errors or incomplete solutions
- Limited understanding of concepts

### Unsatisfactory (<60%)
- Tasks not completed or major errors
- Code doesn't run or produces incorrect results

---

## 🤝 Submission Guidelines

1. **File Organization:**
   - Create separate `.py` files for each task
   - Name them: `task1_pizza.py`, `task2_store.py`, etc.
   - Include comments explaining your code

2. **Documentation:**
   - Add a comment at the top of each file with:
     - Your name and student ID
     - Task number and title
     - Date completed
     - Brief description of what the program does

3. **Testing:**
   - Test each program with different inputs
   - Include edge cases (zero values, large numbers, etc.)
   - Take screenshots of your output

4. **Code Style:**
   - Use meaningful variable names
   - Follow snake_case convention
   - Include appropriate spacing and indentation
   - Add comments for complex calculations

---

## 💡 Tips for Success

1. **Read the story carefully** - Understanding the context helps you write better code
2. **Start simple** - Get basic functionality working before adding features
3. **Test frequently** - Run your code often to catch errors early
4. **Use the hints** - They contain important technical guidance
5. **Be creative** - Add your own touches to make the programs unique
6. **Ask questions** - Don't hesitate to seek help when stuck
7. **Review concepts** - Refer back to Lesson 1 materials as needed

