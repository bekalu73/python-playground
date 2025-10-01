"""
PEP 8 & CODE STYLE
==================

Key Points:
- PEP 8 is the official Python style guide
- Naming conventions for variables, functions, classes
- Code layout and formatting rules
- Import organization
- Comments and docstrings
- Line length and indentation
"""

print("=== PEP 8 NAMING CONVENTIONS ===")

# ✅ CORRECT naming examples

# Variables and functions: snake_case
user_name = "alice"
total_score = 100
max_attempts = 3

def calculate_total(price, tax_rate):
    """Calculate total price including tax"""
    return price * (1 + tax_rate)

def get_user_info():
    """Get user information"""
    return {"name": "Alice", "age": 25}

# Constants: UPPER_SNAKE_CASE
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

# Classes: PascalCase (CapWords)
class UserAccount:
    """Represents a user account"""
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def get_display_name(self):
        """Get formatted display name"""
        return f"User: {self.username}"

class DatabaseConnection:
    """Handles database connections"""
    pass

# Modules and packages: lowercase with underscores
# Examples: my_module.py, data_processing.py, user_management/

print("✅ Proper naming conventions demonstrated")

print("\n=== CODE LAYOUT ===")

# ✅ CORRECT indentation (4 spaces)
def process_data(data_list):
    """Process a list of data items"""
    results = []
    for item in data_list:
        if item > 0:
            processed_item = item * 2
            results.append(processed_item)
        else:
            results.append(0)
    return results

# ✅ CORRECT line breaks and spacing
def long_function_name(
    parameter_one, parameter_two, parameter_three,
    parameter_four, parameter_five, parameter_six
):
    """Function with many parameters"""
    return parameter_one + parameter_two

# ✅ CORRECT operator spacing
result = (first_value + second_value) * multiplier
is_valid = (age >= 18) and (has_license is True)

# ✅ CORRECT list/dict formatting
shopping_list = [
    "apples",
    "bananas", 
    "cherries",
    "dates"
]

user_data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "active": True
}

print("✅ Proper code layout demonstrated")

print("\n=== IMPORT ORGANIZATION ===")

print("""
✅ CORRECT import order:

1. Standard library imports
2. Related third-party imports  
3. Local application/library imports

Example:
import os
import sys
from datetime import datetime

import requests
import numpy as np
from flask import Flask

from my_package import my_module
from . import sibling_module
""")

print("\n=== LINE LENGTH ===")

# ✅ CORRECT: Lines should be <= 79 characters
short_message = "This line is within the 79 character limit"

# ✅ CORRECT: Breaking long lines
long_message = (
    "This is a very long message that needs to be broken "
    "across multiple lines to stay within the character limit"
)

# ✅ CORRECT: Function calls with many arguments
result = some_function(
    first_argument,
    second_argument,
    third_argument,
    fourth_argument
)

print("✅ Proper line length management demonstrated")

print("\n=== COMMENTS AND DOCSTRINGS ===")

def calculate_compound_interest(principal, rate, time, compound_frequency=1):
    """
    Calculate compound interest.
    
    Args:
        principal (float): Initial amount of money
        rate (float): Annual interest rate (as decimal)
        time (float): Time in years
        compound_frequency (int): Number of times interest compounds per year
    
    Returns:
        float: Final amount after compound interest
    
    Example:
        >>> calculate_compound_interest(1000, 0.05, 2)
        1102.5
    """
    # Formula: A = P(1 + r/n)^(nt)
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    return round(amount, 2)

# ✅ CORRECT: Inline comments (sparingly used)
x = x + 1  # Increment x by 1

# ✅ CORRECT: Block comments
# This section handles user authentication
# It checks credentials against the database
# and returns appropriate response codes

print("✅ Proper comments and docstrings demonstrated")

print("\n=== COMMON PEP 8 VIOLATIONS TO AVOID ===")

print("""
❌ AVOID these common mistakes:

1. Wrong naming:
   userName = "alice"        # Should be: user_name
   CalculateTotal()          # Should be: calculate_total()
   MYCLASS                   # Should be: MyClass

2. Poor spacing:
   x=y+z                     # Should be: x = y + z
   if(x>5):                  # Should be: if x > 5:
   list=[1,2,3]             # Should be: list = [1, 2, 3]

3. Wrong indentation:
   if True:
   print("hello")            # Should be indented 4 spaces

4. Long lines:
   very_long_line = "This line is way too long and exceeds the 79 character limit which makes it hard to read"

5. Poor imports:
   from module import *      # Avoid wildcard imports
   import sys, os           # Should be separate lines
""")

print("\n=== TOOLS FOR PEP 8 COMPLIANCE ===")

tools_info = """
Useful tools for maintaining PEP 8 compliance:

1. flake8: Linting tool that checks PEP 8 compliance
   pip install flake8
   flake8 my_file.py

2. black: Automatic code formatter
   pip install black
   black my_file.py

3. autopep8: Automatically fixes PEP 8 violations
   pip install autopep8
   autopep8 --in-place my_file.py

4. pylint: Comprehensive code analysis
   pip install pylint
   pylint my_file.py

5. IDE extensions: Most IDEs have PEP 8 checking built-in
"""

print(tools_info)

print("\n=== PRACTICAL EXAMPLES ===")

# ✅ GOOD: Well-formatted class
class BankAccount:
    """A simple bank account class following PEP 8"""
    
    def __init__(self, account_number, initial_balance=0.0):
        """Initialize a new bank account"""
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount}")
        return self.balance
    
    def get_balance(self):
        """Get current account balance"""
        return self.balance

# Usage example
account = BankAccount("12345", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
print(f"Account balance: ${account.get_balance()}")

print("\n=== EXAM FOCUS: KEY RULES ===")

key_rules = """
Essential PEP 8 rules for exams:

1. Use 4 spaces for indentation (never tabs)
2. Lines should be ≤ 79 characters
3. snake_case for variables and functions
4. PascalCase for classes
5. UPPER_SNAKE_CASE for constants
6. Two blank lines before class definitions
7. One blank line before method definitions
8. Spaces around operators: x = y + z
9. No trailing whitespace
10. Import standard library first, then third-party, then local
"""

print(key_rules)

# Demonstrate proper spacing and formatting
def exam_example_function(param_one, param_two=None):
    """
    Example function demonstrating PEP 8 compliance.
    
    This function shows proper formatting, naming,
    and documentation practices.
    """
    # Proper variable naming
    result_value = param_one * 2
    
    # Proper conditional formatting
    if param_two is not None:
        result_value += param_two
    
    # Proper return statement
    return result_value

print("\nPEP 8 and code style mastered! ✓")