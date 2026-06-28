# Data Types & Dynamic Typing

> 📄 **Related code file:** [`02_data_types.py`](02_data_types.py)

## Overview

Every value in Python has a **type** that determines what you can do with it. Python is **dynamically typed**, meaning you don't declare types explicitly — Python figures them out automatically, and a variable can even change type during a program's life.

## Dynamic Typing

In statically typed languages (like Java or C++), you must declare a variable's type. In Python, you just assign a value:

```python
x = 42           # x is an int
x = "forty-two"  # now x is a str
x = 3.14         # now x is a float
x = True         # now x is a bool
```

The **type belongs to the value**, not the variable. Use `type()` to check:

```python
print(type(42))        # <class 'int'>
print(type("hello"))   # <class 'str'>
print(type(3.14))      # <class 'float'>
```

## The Built-in Data Types

### Numbers
```python
integer_num = 100         # int — whole numbers
float_num = 3.14159       # float — decimal numbers
complex_num = 3 + 4j      # complex — real + imaginary
```

### Text (Strings)
```python
text = "Python Programming"
multiline = """This is a
multiline string"""
```

### Boolean
```python
is_python_fun = True
is_difficult = False
```

### Collections

| Type | Syntax | Ordered? | Mutable? | Duplicates? |
|------|--------|----------|----------|-------------|
| `list` | `[1, 2, 3]` | ✅ | ✅ | ✅ |
| `tuple` | `(1, 2, 3)` | ✅ | ❌ | ✅ |
| `dict` | `{"a": 1}` | ✅* | ✅ | Keys unique |
| `set` | `{1, 2, 3}` | ❌ | ✅ | ❌ |

```python
my_list = [1, 2, 3, "mixed", True]   # ordered, changeable
my_tuple = (1, 2, 3)                  # ordered, unchangeable
my_dict = {"name": "Alice", "age": 25}  # key-value pairs
my_set = {1, 2, 3, 3}                # unique elements → {1, 2, 3}
```

*Dictionaries preserve insertion order since Python 3.7.

## Type Checking and Conversion

### Checking types safely with `isinstance()`
```python
value = 42
if isinstance(value, int):
    print("It's an integer")
```

> `isinstance()` is preferred over `type(value) == int` because it also handles subclasses correctly.

### Type conversion (casting)
```python
int("123")      # 123  (str → int)
str(123)        # "123" (int → str)
float("3.14")   # 3.14 (str → float)
list("abc")     # ['a', 'b', 'c']
bool(0)         # False
bool(1)         # True
```

## Common Mistakes

❌ **Mixing incompatible types:**
```python
"Age: " + 25        # TypeError: can only concatenate str to str
# Fix:
"Age: " + str(25)   # "Age: 25"
```

❌ **Assuming `int` division gives an int:**
```python
10 / 3   # 3.333... (always a float with /)
10 // 3  # 3 (use // for integer division)
```

❌ **Confusing `type()` comparison with `isinstance()`:**
```python
type(True) == int   # False
isinstance(True, int)  # True (bool is a subclass of int!)
```

## Best Practices

✅ Use `isinstance()` for type checks.
✅ Convert input explicitly — `input()` always returns a string.
✅ Use tuples for fixed collections, lists for changeable ones.
✅ Use descriptive variable names that hint at the type (`names_list`, `age_count`).

## Exercises

1. **Predict the type:** What does `type(3 / 1)` return? Verify by running it.

2. **Convert and calculate:** The variable `age = "30"` is a string. Convert it to an integer and add 5.

3. **Build a collection:** Create a dictionary representing a book with keys `title`, `author`, and `year`. Print each value with its type.

4. **Deduplicate:** Given `nums = [1, 2, 2, 3, 3, 3]`, use a `set` to find the unique values.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 2
age = "30"
print(int(age) + 5)   # 35

# Exercise 4
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)    # {1, 2, 3}
```
</details>

## Key Takeaways

- Python is **dynamically typed** — no need to declare types.
- Core types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`.
- Use `type()` to inspect and `isinstance()` to check types.
- Convert between types with `int()`, `str()`, `float()`, `list()`, etc.

---

▶️ **Run the examples:** `python basic/02_data_types.py`
⏮️ **Previous:** [Syntax & Indentation](01_syntax_indentation.md) | ⏭️ **Next:** [Operators →](03_operators.md)
