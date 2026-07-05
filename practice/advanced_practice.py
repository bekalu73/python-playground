"""
ADVANCED LEVEL PRACTICE QUESTIONS
==================================

Covers: inheritance, magic methods, generators, regex, async, decorators, context managers
"""

import asyncio
import re
import time
from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# QUESTION 1: INHERITANCE & SUPER()
# ---------------------------------------------------------------------------
"""
Create a class hierarchy:
- Animal (base): __init__(name), make_sound() -> abstract
- Dog (inherits): make_sound() -> "Woof!"
- Cat (inherits): make_sound() -> "Meow!"
- LoudDog (inherits Dog): make_sound() -> "WOOF!" (calls super() and uppercases)
"""
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class LoudDog(Dog):
    def make_sound(self):
        return super().make_sound().upper() + "!"

# Tests
dog = Dog("Rex")
cat = Cat("Luna")
loud = LoudDog("King")
assert dog.make_sound() == "Woof!"
assert cat.make_sound() == "Meow!"
assert loud.make_sound() == "WOOF!!"
assert isinstance(dog, Animal)
assert isinstance(loud, Dog)
assert isinstance(loud, Animal)
assert not isinstance(cat, Dog)
print("Q1 PASSED: Inheritance")


# ---------------------------------------------------------------------------
# QUESTION 2: MAGIC METHODS - VECTOR
# ---------------------------------------------------------------------------
"""
Create a Vector2D class with magic methods:
- __init__(x, y)
- __add__, __sub__ (vector + vector)
- __mul__ (vector * scalar OR scalar * vector)
- __abs__ (magnitude)
- __bool__ (True if non-zero)
"""
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

# Tests
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
assert v1 + v2 == Vector2D(4, 6)
assert v2 - v1 == Vector2D(2, 2)
assert v1 * 3 == Vector2D(3, 6)
assert 3 * v1 == Vector2D(3, 6)
assert round(abs(Vector2D(3, 4)), 1) == 5.0
assert bool(Vector2D(0, 0)) is False
assert bool(Vector2D(1, 0)) is True
print("Q2 PASSED: Vector2D magic methods")


# ---------------------------------------------------------------------------
# QUESTION 3: GENERATOR - INFINITE SEQUENCE
# ---------------------------------------------------------------------------
"""
Write a generator that yields an infinite sequence:
- Even numbers starting from 0: 0, 2, 4, 6, 8, ...
- Use yield and a loop — no external list
"""
def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

# Tests
gen = even_numbers()
first_5 = [next(gen) for _ in range(5)]
assert first_5 == [0, 2, 4, 6, 8]

gen2 = even_numbers()
for _ in range(100):
    next(gen2)
assert next(gen2) == 200
print("Q3 PASSED: even_numbers generator")


# ---------------------------------------------------------------------------
# QUESTION 4: GENERATOR - YIELD FROM
# ---------------------------------------------------------------------------
"""
Write a generator that flattens nested lists using yield from.
Example: flatten([1, [2, [3, 4], 5], 6]) -> 1, 2, 3, 4, 5, 6
"""
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

# Tests
result = list(flatten([1, [2, [3, 4], 5], 6]))
assert result == [1, 2, 3, 4, 5, 6]
assert list(flatten([])) == []
assert list(flatten([1, 2, 3])) == [1, 2, 3]
assert list(flatten([[[]]])) == []
print("Q4 PASSED: flatten generator")


# ---------------------------------------------------------------------------
# QUESTION 5: REGEX - DATA EXTRACTION
# ---------------------------------------------------------------------------
"""
Write a function to parse log lines and extract structured data.
Log format: "[2024-01-15 10:30:45] ERROR (app.py:42): Connection timeout"
Return: {"timestamp": "...", "level": "...", "file": "...", "line": "...", "message": "..."}
"""
def parse_log_line(line):
    pattern = r"\[(.+?)\]\s+(\w+)\s+\((.+?):(\d+)\):\s+(.+)"
    match = re.match(pattern, line.strip())
    if not match:
        return None
    return {
        "timestamp": match.group(1),
        "level": match.group(2),
        "file": match.group(3),
        "line": int(match.group(4)),
        "message": match.group(5),
    }

# Tests
log = "[2024-01-15 10:30:45] ERROR (app.py:42): Connection timeout"
result = parse_log_line(log)
assert result["timestamp"] == "2024-01-15 10:30:45"
assert result["level"] == "ERROR"
assert result["file"] == "app.py"
assert result["line"] == 42
assert result["message"] == "Connection timeout"
assert parse_log_line("invalid") is None
print("Q5 PASSED: parse_log_line")


# ---------------------------------------------------------------------------
# QUESTION 6: REGEX - PASSWORD VALIDATION
# ---------------------------------------------------------------------------
"""
Write a function that validates a password:
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character (@, #, $, %, &, *)
Return True/False.
"""
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[@#$%&*]", password):
        return False
    return True

# Tests
assert validate_password("Pass1234#") is True
assert validate_password("Sh1#") is False  # too short
assert validate_password("nouppercase1#") is False
assert validate_password("NOLOWERCASE1#") is False
assert validate_password("NoDigits#") is False
assert validate_password("NoSpecial1") is False
print("Q6 PASSED: validate_password")


# ---------------------------------------------------------------------------
# QUESTION 7: CONTEXT MANAGER
# ---------------------------------------------------------------------------
"""
Create a Timer context manager that measures how long a code block takes.
Usage:
with Timer("my task") as timer:
    do_something()
print(timer.elapsed)  # seconds
"""
class Timer:
    def __init__(self, name="timer"):
        self.name = name
        self.elapsed = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start

# Tests
with Timer("test") as timer:
    pass
assert timer.elapsed >= 0
assert isinstance(timer.elapsed, float)

with Timer("sleep") as timer:
    time.sleep(0.01)
assert timer.elapsed >= 0.01
print("Q7 PASSED: Timer context manager")


# ---------------------------------------------------------------------------
# QUESTION 8: DECORATOR - RETRY
# ---------------------------------------------------------------------------
"""
Write a @retry decorator that retries a function up to n times if it raises an exception.
@retry(max_attempts=3)
def unstable_function():
    ...
"""
def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    if attempt < max_attempts - 1:
                        continue
            raise last_exc
        return wrapper
    return decorator

# Tests
call_count = 0

@retry(max_attempts=3)
def flaky_function():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ValueError("Not yet")
    return "success"

result = flaky_function()
assert result == "success"
assert call_count == 3

call_count2 = 0

@retry(max_attempts=2)
def always_fails():
    global call_count2
    call_count2 += 1
    raise ValueError("always")

try:
    always_fails()
    assert False, "Should raise"
except ValueError:
    assert call_count2 == 2
print("Q8 PASSED: retry decorator")


# ---------------------------------------------------------------------------
# QUESTION 9: ASYNC - CONCURRENT FETCH WITH TIMEOUT
# ---------------------------------------------------------------------------
"""
Write async functions that simulate concurrent API calls with a timeout.
- fetch_data(name, delay): simulates a request
- fetch_all_with_timeout(names, delays, timeout): runs them concurrently
  but raises asyncio.TimeoutError if any single task exceeds timeout
"""
async def fetch_data(name, delay):
    await asyncio.sleep(delay)
    return f"{name}_result"

async def fetch_all_with_timeout(names, delays, timeout):
    tasks = []
    for name, delay in zip(names, delays):
        tasks.append(asyncio.create_task(
            asyncio.wait_for(fetch_data(name, delay), timeout=timeout)
        ))
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results

async def _test_async():
    results = await fetch_all_with_timeout(["a", "b", "c"], [0.01, 0.02, 0.01], timeout=5.0)
    assert results == ["a_result", "b_result", "c_result"]

    results2 = await fetch_all_with_timeout(["a", "b"], [0.01, 0.5], timeout=0.1)
    assert isinstance(results2[0], str)
    assert isinstance(results2[1], asyncio.TimeoutError)

asyncio.run(_test_async())
print("Q9 PASSED: async fetch with timeout")


# ---------------------------------------------------------------------------
# QUESTION 10: MULTIPLE INHERITANCE & MRO
# ---------------------------------------------------------------------------
"""
Create a class hierarchy demonstrating MRO:
- A: method() -> "A"
- B(A): method() -> "B"
- C(A): method() -> "C"
- D(B, C): no method() — should resolve via MRO to C
"""
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

# Tests
d = D()
assert d.method() == "B"  # D -> B -> C -> A, first match is B
assert D.__mro__[0] == D
assert D.__mro__[1] == B
assert D.__mro__[2] == C
assert D.__mro__[3] == A
print("Q10 PASSED: MRO")


# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------
print()
print("=" * 50)
print("ALL ADVANCED PRACTICE QUESTIONS PASSED!")
print("=" * 50)
print()
print("Topics covered:")
print("  - Inheritance, abstract classes, super()")
print("  - Magic methods (__add__, __mul__, __abs__, __bool__)")
print("  - Generators (infinite, yield from, flatten)")
print("  - Regex (groups, parsing, validation)")
print("  - Context managers (__enter__, __exit__)")
print("  - Decorators (retry with arguments)")
print("  - Async IO (wait_for, gather, timeout)")
print("  - Multiple inheritance & MRO")
