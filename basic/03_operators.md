# Operators

> 📄 **Related code file:** [`03_operators.py`](03_operators.py)

## Overview

**Operators** are special symbols that perform operations on values and variables (called operands). Python groups them into several categories: arithmetic, comparison, logical, membership, and identity.

## Arithmetic Operators

Perform mathematical calculations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `17 + 5` | `22` |
| `-` | Subtraction | `17 - 5` | `12` |
| `*` | Multiplication | `17 * 5` | `85` |
| `/` | Division | `17 / 5` | `3.4` (always float) |
| `//` | Floor division | `17 // 5` | `3` (rounds down) |
| `%` | Modulus | `17 % 5` | `2` (remainder) |
| `**` | Exponentiation | `17 ** 2` | `289` |

```python
a, b = 17, 5
print(a / b)    # 3.4
print(a // b)   # 3
print(a % b)    # 2
print(a ** b)   # 1419857
```

> 💡 The modulus `%` is great for checking even/odd: `n % 2 == 0` means even.

## Comparison Operators

Compare two values and return `True` or `False`.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `10 == 20` → `False` |
| `!=` | Not equal to | `10 != 20` → `True` |
| `<` | Less than | `10 < 20` → `True` |
| `>` | Greater than | `10 > 20` → `False` |
| `<=` | Less than or equal | `10 <= 10` → `True` |
| `>=` | Greater than or equal | `20 >= 10` → `True` |

## Logical Operators

Combine boolean expressions.

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | True if **both** are true | `True and False` → `False` |
| `or` | True if **at least one** is true | `True or False` → `True` |
| `not` | Inverts the value | `not True` → `False` |

```python
age = 25
has_license = True
can_drive = age >= 18 and has_license   # True
```

## Membership Operators

Check whether a value exists in a sequence.

```python
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)        # True
print("grape" not in fruits)    # True
print("Py" in "Python")         # True (works on strings too)
```

## Identity Operators

Check whether two variables point to the **same object** in memory (not just equal values).

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 is list2)   # False — different objects
print(list1 is list3)   # True  — same object
print(list1 == list2)   # True  — same content
```

> ⚠️ **`is` vs `==`:** `==` compares **values**; `is` compares **identity** (memory location). Use `==` for value comparison and reserve `is` for `None` checks (`if x is None:`).

## Common Mistakes

❌ **Using `=` instead of `==`:**
```python
if x = 5:    # SyntaxError — = is assignment, == is comparison
```

❌ **Using `is` to compare values:**
```python
if name is "Alice":   # Unreliable! Use ==
if name == "Alice":   # Correct
```

❌ **Forgetting `/` always returns a float:**
```python
result = 4 / 2   # 2.0, not 2
```

## Best Practices

✅ Use `==` for comparing values, `is` only for `None`/singletons.
✅ Use parentheses to make complex expressions clear: `(a > b) and (c < d)`.
✅ Remember operator precedence: `**` first, then `*` `/` `//` `%`, then `+` `-`.
✅ Use `//` when you specifically need an integer result.

## Exercises

1. **Even or odd:** Write an expression that returns `True` if a number `n` is even.

2. **Leap year check:** A year is a leap year if it's divisible by 4 but not 100, unless also divisible by 400. Write the boolean expression.

3. **Identity vs equality:** Create two lists with the same contents. Show that `==` is `True` but `is` is `False`.

4. **Calculate:** Without running it, predict the output of `7 // 2 + 7 % 2`, then verify.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 1
is_even = n % 2 == 0

# Exercise 2
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Exercise 4
# 7 // 2 = 3, 7 % 2 = 1, so 3 + 1 = 4
```
</details>

## Key Takeaways

- `/` always gives a float; use `//` for integer division and `%` for remainder.
- Comparison operators return booleans.
- `and`, `or`, `not` combine boolean logic.
- `in` checks membership; `is` checks object identity (use `==` for values).

---

▶️ **Run the examples:** `python basic/03_operators.py`
⏮️ **Previous:** [Data Types](02_data_types.md) | ⏭️ **Next:** [Control Flow →](04_control_flow.md)
