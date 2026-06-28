# PEP 8 & Code Style

> 📄 **Related code file:** [`10_pep8_code_style.py`](10_pep8_code_style.py)

## Overview

**PEP 8** is the official style guide for Python code. It defines conventions for naming, layout, and formatting so that Python code looks consistent across projects and teams. Following PEP 8 makes your code more readable and professional.

> "Code is read much more often than it is written." — PEP 8

## Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Variables | `snake_case` | `user_name`, `total_score` |
| Functions | `snake_case` | `calculate_total()` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_CONNECTIONS` |
| Classes | `PascalCase` | `UserAccount`, `BankAccount` |
| Modules | `lowercase` | `data_processing.py` |
| Private (convention) | `_leading_underscore` | `_internal_value` |

```python
# Variables and functions
user_name = "alice"
def calculate_total(price, tax_rate):
    return price * (1 + tax_rate)

# Constants
MAX_CONNECTIONS = 100
API_BASE_URL = "https://api.example.com"

# Classes
class UserAccount:
    def get_display_name(self):
        return f"User: {self.username}"
```

## Code Layout

### Indentation
- Use **4 spaces** per level (never tabs).

### Blank Lines
- **Two** blank lines before top-level function and class definitions.
- **One** blank line between methods inside a class.

### Line Length
- Keep lines **≤ 79 characters** (72 for comments/docstrings).
- Break long lines:

```python
# Implicit line continuation inside parentheses
long_message = (
    "This is a very long message that needs to be broken "
    "across multiple lines to stay within the limit"
)

# Function call with many arguments
result = some_function(
    first_argument,
    second_argument,
    third_argument,
)
```

### Spacing Around Operators
```python
# ✅ Good
x = y + z
is_valid = (age >= 18) and has_license

# ❌ Bad
x=y+z
is_valid=(age>=18)and has_license
```

## Import Organization

Group imports in this order, separated by blank lines:

```python
# 1. Standard library
import os
import sys
from datetime import datetime

# 2. Third-party packages
import requests
import numpy as np

# 3. Local application imports
from my_package import my_module
```

> Avoid wildcard imports (`from module import *`) — they make it unclear what's in scope.

## Comments and Docstrings

### Docstrings (for functions, classes, modules)
```python
def calculate_compound_interest(principal, rate, time):
    """
    Calculate compound interest.

    Args:
        principal (float): Initial amount of money
        rate (float): Annual interest rate (as decimal)
        time (float): Time in years

    Returns:
        float: Final amount after compound interest
    """
    return principal * (1 + rate) ** time
```

### Comments
```python
# Block comment explaining the next section
# of logic in plain language.

x = x + 1  # Inline comment (use sparingly, 2 spaces before #)
```

## Common PEP 8 Violations

| ❌ Violation | ✅ Correct |
|-------------|-----------|
| `userName = "x"` | `user_name = "x"` |
| `def CalculateTotal():` | `def calculate_total():` |
| `x=y+z` | `x = y + z` |
| `if(x>5):` | `if x > 5:` |
| `list=[1,2,3]` | `numbers = [1, 2, 3]` |
| `import sys, os` | `import sys` (each on its own line) |
| `from module import *` | `from module import specific_name` |

## Tools for PEP 8 Compliance

You don't have to check everything manually — let tools help:

```bash
# Linter — flags style issues
pip install flake8
flake8 my_file.py

# Auto-formatter — reformats code to a consistent style
pip install black
black my_file.py

# Auto-fix PEP 8 issues
pip install autopep8
autopep8 --in-place my_file.py

# Comprehensive analysis
pip install pylint
pylint my_file.py
```

> 💡 In VS Code, enable "Format on Save" with `black` to format automatically (see [VS Code Extensions](../setup/vscode-extensions.md)).

## A Well-Formatted Example

```python
class BankAccount:
    """A simple bank account following PEP 8."""

    def __init__(self, account_number, initial_balance=0.0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance
```

## Best Practices

✅ Run a formatter (`black`) and linter (`flake8`) as part of your workflow.
✅ Write docstrings for every public function and class.
✅ Keep functions short and names descriptive.
✅ Be consistent — consistency matters more than personal preference.

## Exercises

1. **Fix the style:** Rewrite this to follow PEP 8:
   ```python
   def AddNums(X,Y):return X+Y
   ```

2. **Naming:** Rename these correctly: a constant for max retries, a class for a "shopping cart", a function that fetches user data.

3. **Run a linter:** Install `flake8` and run it on one of your own files. Fix any warnings.

4. **Docstring:** Add a proper docstring (with Args and Returns) to a function you've written.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 1
def add_nums(x, y):
    return x + y

# Exercise 2
MAX_RETRIES = 3
class ShoppingCart: ...
def get_user_data(): ...
```
</details>

## Key Takeaways

- PEP 8 is Python's official style guide.
- `snake_case` for variables/functions, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants.
- 4-space indentation, lines ≤ 79 chars, spaces around operators.
- Use tools like `black`, `flake8`, and `pylint` to enforce style automatically.

---

▶️ **Run the examples:** `python intermediate/10_pep8_code_style.py`
⏮️ **Previous:** [Packaging & Virtual Environments](09_packaging_venv.md) | ⏭️ **Next:** [OOP Fundamentals →](11_oop_fundamentals.md)
