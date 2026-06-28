# Control Flow

> 📄 **Related code file:** [`04_control_flow.py`](04_control_flow.py)

## Overview

**Control flow** determines the order in which your code runs. With conditional statements (`if`/`elif`/`else`) and loops (`for`/`while`), you can make decisions and repeat actions — the foundation of all programming logic.

## Conditional Statements

### if / elif / else

```python
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
```

- `if` — checked first
- `elif` — ("else if") checked if previous conditions were false; you can have many
- `else` — runs if none of the above were true (optional)

> 📌 Note: It's `elif`, not `else if`.

## For Loops

`for` loops iterate over a sequence (list, string, range, etc.).

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```

### Using `range()`
```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 11, 2):   # start=2, stop=11, step=2 → 2,4,6,8,10
    print(i)
```

### Using `enumerate()` for index + value
```python
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

## While Loops

A `while` loop repeats as long as a condition is `True`. Use it when you don't know the number of iterations in advance.

```python
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1   # Don't forget to update — or it loops forever!
```

## break and continue

- **`break`** — exit the loop immediately
- **`continue`** — skip to the next iteration

```python
# Skip even numbers with continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")   # 1 3 5 7 9

# Stop at first negative with break
for num in [1, 3, -2, 5]:
    if num < 0:
        break
    print(num, end=" ")   # 1 3
```

## The Loop-else Clause (Python-Specific!)

A unique Python feature: an `else` attached to a loop runs **only if the loop completed without hitting `break`**.

```python
for i in range(3):
    print(i)
else:
    print("Loop completed normally!")   # Runs

for i in range(5):
    if i == 2:
        break
else:
    print("This won't run")   # Skipped because of break
```

**Practical use — searching:**
```python
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found {target}!")
            break
    else:
        print(f"{target} not found")
```

## Nested Loops

A loop inside another loop. The inner loop completes fully for each iteration of the outer loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()   # New line after each row
```

## Common Mistakes

❌ **Infinite `while` loop** (forgetting to update the condition):
```python
count = 0
while count < 3:
    print(count)   # Runs forever — count never changes!
```

❌ **Modifying a list while iterating over it:**
```python
for item in my_list:
    my_list.remove(item)   # Skips elements — iterate over a copy instead
```

❌ **Confusing `break` and `continue`.**

## Best Practices

✅ Prefer `for` loops when iterating over a known sequence.
✅ Use `enumerate()` instead of manually tracking an index.
✅ Keep loop bodies short; extract complex logic into functions.
✅ Use the loop-`else` clause for search/validation patterns.

## Exercises

1. **FizzBuzz:** Print numbers 1–20. For multiples of 3 print "Fizz", multiples of 5 print "Buzz", multiples of both print "FizzBuzz".

2. **Sum until zero:** Using a `while` loop, keep adding numbers from a list until you reach a `0`, then stop.

3. **Prime checker:** Use a `for`/`else` loop to determine if a number is prime.

4. **Multiplication table:** Print the full 5×5 multiplication table using nested loops.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 1
for n in range(1, 21):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# Exercise 3
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True
```
</details>

## Key Takeaways

- Use `if`/`elif`/`else` for decisions.
- `for` loops iterate over sequences; `while` loops repeat on a condition.
- `break` exits a loop; `continue` skips to the next iteration.
- The **loop-`else`** runs only when the loop finishes without `break`.

---

▶️ **Run the examples:** `python basic/04_control_flow.py`
⏮️ **Previous:** [Operators](03_operators.md) | ⏭️ **Next:** [Functions & Scope →](05_functions_scope.md)
