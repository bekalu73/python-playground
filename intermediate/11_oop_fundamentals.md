# OOP Fundamentals

> 📄 **Related code file:** [`11_oop_fundamentals.py`](11_oop_fundamentals.py)

## Overview

**Object-Oriented Programming (OOP)** organizes code around **objects** — bundles of data (attributes) and behavior (methods). A **class** is a blueprint, and an **object** (instance) is a specific thing built from that blueprint. OOP helps model real-world entities and write reusable, organized code.

## Defining a Class

Use the `class` keyword (classes use `PascalCase`).

```python
class Dog:
    """A simple Dog class."""

    species = "Canis lupus"   # Class variable (shared by all dogs)

    def __init__(self, name, age, breed):
        """Constructor — runs when a new Dog is created."""
        self.name = name       # Instance variables (unique per dog)
        self.age = age
        self.breed = breed

    def bark(self):            # Instance method
        return f"{self.name} says Woof!"
```

### Creating Objects (Instances)
```python
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "German Shepherd")

print(dog1.name)      # "Buddy"
print(dog1.bark())    # "Buddy says Woof!"
print(Dog.species)    # "Canis lupus"
```

## The `__init__` Method and `self`

- **`__init__`** is the **constructor** — automatically called when you create an object. It sets up the initial state.
- **`self`** refers to the specific instance being worked on. It must be the **first parameter** of every instance method. You don't pass it manually — Python does that for you.

```python
dog = Dog("Rex", 2, "Beagle")
# Python calls Dog.__init__(dog, "Rex", 2, "Beagle") behind the scenes
```

## Instance vs Class Variables

| Type | Defined | Shared? |
|------|---------|---------|
| Instance variable | `self.x = ...` inside methods | Unique to each object |
| Class variable | directly in the class body | Shared by all instances |

```python
class Counter:
    total_counters = 0          # Class variable

    def __init__(self, name):
        self.name = name        # Instance variable
        self.count = 0
        Counter.total_counters += 1   # Modify the shared class variable

c1 = Counter("A")
c2 = Counter("B")
print(Counter.total_counters)   # 2
```

## Method Types

```python
class MathUtils:
    pi = 3.14159

    def __init__(self, precision=2):
        self.precision = precision

    def round_number(self, number):       # Instance method (uses self)
        return round(number, self.precision)

    @classmethod
    def get_pi(cls):                      # Class method (uses cls)
        return cls.pi

    @staticmethod
    def add_numbers(a, b):                # Static method (no self/cls)
        return a + b
```

- **Instance method** — operates on instance data; takes `self`.
- **Class method** (`@classmethod`) — operates on the class; takes `cls`.
- **Static method** (`@staticmethod`) — a utility function that doesn't need instance or class data.

## Object Identity and Equality

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
p2 = Person("Alice", 25)
p3 = p1

p1 is p2    # False — different objects in memory
p1 is p3    # True  — same object
```

By default, two different objects are never "equal" even if their data matches — to change that, you implement `__eq__` (covered in [Magic Methods](../advanced/13_magic_methods.md)).

## A Practical Example

```python
class BankAccount:
    total_accounts = 0
    bank_name = "Python Bank"

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        BankAccount.total_accounts += 1
        self.account_number = f"ACC{BankAccount.total_accounts:04d}"

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive"
        self.balance += amount
        return f"Deposited ${amount}. Balance: ${self.balance}"

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def calculate_interest(principal, rate, time):
        return principal * rate * time
```

## Common Mistakes

❌ **Forgetting `self`:**
```python
def bark():           # Missing self
    return "Woof"
# TypeError when called as a method
```

❌ **Mutable class variables shared unexpectedly:**
```python
class Team:
    members = []      # SHARED across all teams!
# Use instance variables in __init__ instead:
    def __init__(self):
        self.members = []
```

❌ **Accessing instance variables before they're set** (set them in `__init__`).

❌ **Confusing class and instance variables** when assigning.

## Best Practices

✅ Use `PascalCase` for class names.
✅ Initialize all instance variables in `__init__`.
✅ Write a docstring for each class and method.
✅ Use class variables only for data truly shared across all instances.
✅ Keep methods focused; one responsibility each.

## Exercises

1. **Rectangle class:** Create a `Rectangle` with `width` and `height`, plus methods `area()` and `perimeter()`.

2. **Instance counter:** Add a class variable to your `Rectangle` that counts how many rectangles have been created.

3. **Static utility:** Add a `@staticmethod` `is_square(width, height)` that returns whether the dimensions form a square.

4. **Bank account:** Build a simplified `BankAccount` with `deposit`, `withdraw` (rejecting overdrafts), and `get_balance`.

<details>
<summary>💡 Solution hints</summary>

```python
class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    @staticmethod
    def is_square(width, height):
        return width == height
```
</details>

## Key Takeaways

- A **class** is a blueprint; an **object** is an instance of it.
- `__init__` is the constructor; `self` refers to the current instance.
- **Instance variables** are per-object; **class variables** are shared.
- Method types: instance (`self`), class (`@classmethod`, `cls`), static (`@staticmethod`).

---

▶️ **Run the examples:** `python intermediate/11_oop_fundamentals.py`
⏮️ **Previous:** [PEP 8 & Code Style](10_pep8_code_style.md) | ⏭️ **Next:** [Advanced: OOP Principles →](../advanced/12_oop_principles.md)
