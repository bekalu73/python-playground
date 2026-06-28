# Functions & Scope

> 📄 **Related code file:** [`05_functions_scope.py`](05_functions_scope.py)

## Overview

**Functions** are reusable blocks of code that perform a specific task. They help you avoid repetition, organize your program, and make code easier to test and understand. **Scope** defines where variables can be accessed.

## Defining Functions

Use the `def` keyword:

```python
def greet(name="World"):
    """Function with a default parameter (this is a docstring)."""
    return f"Hello, {name}!"

print(greet())          # Hello, World!
print(greet("Alice"))   # Hello, Alice!
```

- **Parameters** are the variables in the definition (`name`).
- **Arguments** are the actual values you pass (`"Alice"`).
- **Default parameters** provide a fallback value and must come *after* required ones.
- `return` sends a value back to the caller (functions without `return` give `None`).

## Multiple Parameters

```python
def calculate_area(length, width, unit="sq meters"):
    area = length * width
    return f"Area: {area} {unit}"

calculate_area(5, 3)            # positional arguments
calculate_area(5, 3, "sq feet")
calculate_area(width=3, length=5)  # keyword arguments (order doesn't matter)
```

## *args — Variable Positional Arguments

`*args` collects any number of extra positional arguments into a **tuple**.

```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_numbers(1, 2, 3)         # 6
sum_numbers(1, 2, 3, 4, 5)   # 15
```

## **kwargs — Variable Keyword Arguments

`**kwargs` collects extra keyword arguments into a **dictionary**.

```python
def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name="Alice", age=25, city="NYC")
```

## Parameter Order

When combining all types, they **must** appear in this order:

```python
def flexible(required, default="x", *args, **kwargs):
    ...
#   1. required positional
#   2. default values
#   3. *args
#   4. **kwargs
```

## Scope: Local vs Global

A variable's **scope** is where it can be accessed.

```python
global_var = "I'm global"   # Accessible everywhere

def scope_demo():
    local_var = "I'm local"  # Only exists inside this function
    print(global_var)        # Can read globals
    print(local_var)

scope_demo()
# print(local_var)  # NameError — local_var doesn't exist out here
```

### Modifying a global variable
```python
counter = 0

def increment():
    global counter   # Declare intent to modify the global
    counter += 1
    return counter
```

> ⚠️ Use `global` sparingly — it's usually better to pass values in and return results.

## Nested Functions & Closures

An inner function can access the outer function's variables. This is called a **closure**.

```python
def outer_function(x):
    def inner_function(y):
        return x + y   # Remembers x from the enclosing scope
    return inner_function

add_10 = outer_function(10)
print(add_10(5))   # 15
```

## Lambda Functions

A `lambda` is a small, anonymous one-line function.

```python
square = lambda x: x ** 2
print(square(5))   # 25

# Common with map/filter/sorted
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))   # [1, 4, 9, 16, 25]
```

## Common Mistakes

❌ **Mutable default arguments:**
```python
def add_item(item, items=[]):   # DANGER: the list is shared across calls!
    items.append(item)
    return items
# Fix: use None as the default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

❌ **Forgetting `return`** (function silently returns `None`).

❌ **Wrong parameter order** (`def f(*args, x)` before keyword-only handling).

## Best Practices

✅ Give functions descriptive verb names (`calculate_total`, `get_user`).
✅ Write a docstring describing what the function does.
✅ Keep functions small and focused on one task.
✅ Prefer returning values over modifying globals.
✅ Use `*args`/`**kwargs` only when you genuinely need flexibility.

## Exercises

1. **Temperature converter:** Write `celsius_to_fahrenheit(c)` returning `c * 9/5 + 32`.

2. **Flexible average:** Write `average(*args)` that returns the mean of any number of values.

3. **Profile builder:** Write `build_profile(name, **details)` that returns a dictionary combining the name with all extra details.

4. **Counter closure:** Write a function `make_counter()` that returns a function which increments and returns a count each time it's called.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 2
def average(*args):
    return sum(args) / len(args) if args else 0

# Exercise 4
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
```
</details>

## Key Takeaways

- Define functions with `def`; return values with `return`.
- `*args` gathers positional args (tuple); `**kwargs` gathers keyword args (dict).
- Variables have **local** or **global** scope; use `global`/`nonlocal` to modify outer variables.
- `lambda` creates small anonymous functions.

---

▶️ **Run the examples:** `python basic/05_functions_scope.py`
⏮️ **Previous:** [Control Flow](04_control_flow.md) | ⏭️ **Next:** [Lists & Dictionaries →](06_lists_dictionaries.md)
