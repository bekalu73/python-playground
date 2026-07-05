"""
INTERMEDIATE LEVEL PRACTICE QUESTIONS
======================================

Covers: OOP fundamentals, class methods, static methods, properties, composition, imports
"""

import math
import os
import tempfile
from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# QUESTION 1: CLASS WITH PROPERTIES
# ---------------------------------------------------------------------------
"""
Create a Rectangle class with width and height properties.
- Properties: width, height (with validation: must be positive)
- Methods: area(), perimeter()
- Property getters and setters using @property
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

# Tests
r = Rectangle(3, 4)
assert r.area() == 12
assert r.perimeter() == 14
assert r.width == 3
assert r.height == 4

try:
    Rectangle(-1, 5)
    assert False, "Should raise ValueError"
except ValueError:
    pass

r.width = 10
assert r.area() == 40
print("Q1 PASSED: Rectangle")


# ---------------------------------------------------------------------------
# QUESTION 2: CLASS METHOD & STATIC METHOD
# ---------------------------------------------------------------------------
"""
Create a Temperature class with:
- Instance method: to_fahrenheit() and to_celsius()
- Class method: from_fahrenheit(cls, f) — creates instance from Fahrenheit
- Static method: is_freezing(temp_c) — returns True if temp <= 0
"""
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def to_celsius(self):
        return self.celsius

    @classmethod
    def from_fahrenheit(cls, f):
        celsius = (f - 32) * 5 / 9
        return cls(celsius)

    @staticmethod
    def is_freezing(temp_c):
        return temp_c <= 0

# Tests
t = Temperature(0)
assert t.to_fahrenheit() == 32
assert t.to_celsius() == 0

t2 = Temperature.from_fahrenheit(212)
assert round(t2.celsius, 1) == 100.0

assert Temperature.is_freezing(0) is True
assert Temperature.is_freezing(-5) is True
assert Temperature.is_freezing(10) is False
print("Q2 PASSED: Temperature")


# ---------------------------------------------------------------------------
# QUESTION 3: COMPOSITION
# ---------------------------------------------------------------------------
"""
Create an Author class and a Book class using composition.
- Author has: name, birth_year
- Book has: title, year, author (Author instance)
- Book has a method: get_author_info() -> "Name (birth_year)"
"""
class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def get_author_info(self):
        return f"{self.author.name} ({self.author.birth_year})"

# Tests
author = Author("George Orwell", 1903)
book = Book("1984", 1949, author)
assert book.get_author_info() == "George Orwell (1903)"
assert book.title == "1984"
assert book.author.name == "George Orwell"
print("Q3 PASSED: Book & Author")


# ---------------------------------------------------------------------------
# QUESTION 4: CUSTOM EXCEPTION
# ---------------------------------------------------------------------------
"""
Define a custom InsufficientFundsError exception (inheriting from Exception).
Then implement a Wallet class that raises it on insufficient balance.
"""
class InsufficientFundsError(Exception):
    pass

class Wallet:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def spend(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"{self.owner} needs ${amount} but only has ${self.balance}"
            )
        self.balance -= amount
        return self.balance

    def earn(self, amount):
        self.balance += amount
        return self.balance

# Tests
w = Wallet("Alice", 100)
assert w.earn(50) == 150
assert w.spend(30) == 120
assert w.balance == 120

try:
    w.spend(200)
    assert False, "Should raise InsufficientFundsError"
except InsufficientFundsError as e:
    assert "Alice" in str(e)
    assert "120" in str(e)
print("Q4 PASSED: Wallet & InsufficientFundsError")


# ---------------------------------------------------------------------------
# QUESTION 5: MODULE-LIKE STRUCTURE
# ---------------------------------------------------------------------------
"""
Create a simple math toolkit using a class with static methods.
Implement: is_even, factorial (recursive), gcd, is_prime
"""
class MathTools:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("No negative factorial")
        if n <= 1:
            return 1
        return n * MathTools.factorial(n - 1)

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# Tests
assert MathTools.is_even(4) is True
assert MathTools.is_even(7) is False
assert MathTools.factorial(5) == 120
assert MathTools.factorial(0) == 1
assert MathTools.gcd(12, 8) == 4
assert MathTools.gcd(17, 5) == 1
assert MathTools.is_prime(7) is True
assert MathTools.is_prime(10) is False
print("Q5 PASSED: MathTools")


# ---------------------------------------------------------------------------
# QUESTION 6: EMPLOYEE WITH COUNTER
# ---------------------------------------------------------------------------
"""
Create an Employee class that tracks the total number of employees.
- Class variable: total_employees
- __init__: increments total_employees
- Class method: get_total()
- __del__ (or cleanup): decrements total_employees (just for demonstration)
"""
class Employee:
    total_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

    @classmethod
    def get_total(cls):
        return cls.total_employees

# Tests
initial = Employee.get_total()
e1 = Employee("Alice")
e2 = Employee("Bob")
e3 = Employee("Charlie")
assert Employee.get_total() == initial + 3
assert Employee.total_employees == initial + 3
print("Q6 PASSED: Employee counter")


# ---------------------------------------------------------------------------
# QUESTION 7: STRING REPRESENTATION
# ---------------------------------------------------------------------------
"""
Create a Point2D class with:
- __init__(self, x, y)
- __str__: "(x, y)" human-readable
- __repr__: "Point2D(x, y)" unambiguous
- __eq__: compare two points
- distance_to(self, other): Euclidean distance
"""
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Tests
p1 = Point2D(0, 0)
p2 = Point2D(3, 4)
assert str(p1) == "(0, 0)"
assert repr(p1) == "Point2D(0, 0)"
assert p1 == Point2D(0, 0)
assert p1 != p2
assert round(p1.distance_to(p2), 1) == 5.0
print("Q7 PASSED: Point2D")


# ---------------------------------------------------------------------------
# QUESTION 8: ENCAPSULATION (NAME MANGLING)
# ---------------------------------------------------------------------------
"""
Create a BankAccountV2 class with:
- Private attribute: __balance (name mangled)
- Methods: deposit(), withdraw(), get_balance()
- withdraw returns False if insufficient funds (no exception)
"""
class BankAccountV2:
    def __init__(self, owner, initial=0):
        self.owner = owner
        self.__balance = initial

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

# Tests
acc = BankAccountV2("Bob", 100)
assert acc.get_balance() == 100
assert acc.deposit(50) is True
assert acc.get_balance() == 150
assert acc.withdraw(200) is False
assert acc.get_balance() == 150
assert acc.withdraw(50) is True
assert acc.get_balance() == 100
assert hasattr(acc, "_BankAccountV2__balance")  # name mangling
print("Q8 PASSED: BankAccountV2")


# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------
print()
print("=" * 50)
print("ALL INTERMEDIATE PRACTICE QUESTIONS PASSED!")
print("=" * 50)
print()
print("Topics covered:")
print("  - @property getters/setters with validation")
print("  - @classmethod and @staticmethod")
print("  - Composition (objects within objects)")
print("  - Custom exceptions")
print("  - Static method toolkit class")
print("  - Class variables and counters")
print("  - __str__, __repr__, __eq__")
print("  - Encapsulation with name mangling")
