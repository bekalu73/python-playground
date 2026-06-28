# Generators & Iteration

> 📄 **Related code file:** [`14_generators_iteration.py`](14_generators_iteration.py)

## Overview

**Generators** are a special kind of function that produce values **one at a time, on demand**, instead of building a whole list in memory. This makes them extremely memory-efficient and perfect for large (or even infinite) sequences. They're built on Python's **iterator protocol**.

## Basic Generators

A generator function uses `yield` instead of `return`. Each `yield` pauses the function and hands back a value; execution resumes from there on the next request.

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
for value in gen:
    print(value)   # 1, 2, 3
```

## Generator vs Regular Function

```python
# Regular function — builds and returns the whole list at once
def regular():
    result = []
    for i in range(5):
        result.append(i ** 2)
    return result        # [0, 1, 4, 9, 16]

# Generator — yields one value at a time
def generator():
    for i in range(5):
        yield i ** 2     # produces values lazily
```

The generator doesn't compute anything until you iterate over it — this is **lazy evaluation**.

## Practical Examples

```python
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(10):
    print(num, end=" ")   # 0 1 1 2 3 5 8 13 21 34
```

```python
def file_reader(filename):
    """Read a file line by line without loading it all into memory."""
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()
```

## Generator Expressions

Like list comprehensions, but with **parentheses** — they create a generator instead of a list.

```python
squares_gen = (x**2 for x in range(5))    # generator
squares_list = [x**2 for x in range(5)]   # list

# Huge memory difference for large ranges:
import sys
sys.getsizeof([x**2 for x in range(1000)])  # large (stores all values)
sys.getsizeof((x**2 for x in range(1000)))  # tiny (just the generator)
```

## The Iterator Protocol

Generators are iterators. You can build your own iterator with `__iter__` and `__next__`:

```python
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration     # signals iteration is done
        self.start -= 1
        return self.start + 1

for num in CountDown(5):
    print(num, end=" ")   # 5 4 3 2 1
```

- `__iter__` returns the iterator object.
- `__next__` returns the next value or raises `StopIteration`.
- Built-ins `iter()` and `next()` use these under the hood.

## yield from

Delegate to another generator or iterable cleanly:

```python
def sub_gen():
    yield "A"
    yield "B"

def main_gen():
    yield "Start"
    yield from sub_gen()      # delegate to another generator
    yield from [1, 2, 3]      # works with any iterable
    yield "End"

list(main_gen())   # ['Start', 'A', 'B', 1, 2, 3, 'End']
```

## Advanced: send() and close()

Generators can receive values and be closed:

```python
def echo():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo()
next(gen)          # prime the generator
gen.send("hello")  # Received: hello
gen.close()        # stop the generator
```

## Generator Pipelines

Chain generators to build data-processing pipelines — each stage is lazy:

```python
def numbers():
    for i in range(10):
        yield i

def squares(nums):
    for n in nums:
        yield n ** 2

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

pipeline = evens(squares(numbers()))
print(list(pipeline))   # [0, 4, 16, 36, 64]
```

## Common Mistakes

❌ **Reusing an exhausted generator:**
```python
gen = (x for x in range(3))
list(gen)   # [0, 1, 2]
list(gen)   # [] — already consumed!
```

❌ **Using `[]` when you meant `()`** for a generator (or vice versa).

❌ **Iterating an infinite generator without a stop condition** — it never ends:
```python
def infinite():
    n = 0
    while True:
        yield n
        n += 1
# Use itertools.islice or break after N values
```

❌ **Expecting `len()` to work** on a generator — it doesn't (no known length).

## Best Practices

✅ Use generators for large datasets and streaming to save memory.
✅ Use generator expressions when you only iterate once.
✅ Use `yield from` to delegate instead of manual loops.
✅ Remember generators are **single-use** — recreate them to iterate again.
✅ Pair infinite generators with `itertools.islice` or a `break`.

## Exercises

1. **Even generator:** Write a generator `evens(limit)` that yields even numbers up to `limit`.

2. **Running total:** Write a generator that takes a list of numbers and yields the running total after each one.

3. **Chunker:** Write `batch(data, size)` that yields successive chunks of `size` items from a list.

4. **Memory comparison:** Compare `sys.getsizeof` of a list comprehension vs a generator expression for `range(100000)`.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 1
def evens(limit):
    for n in range(0, limit + 1, 2):
        yield n

# Exercise 3
def batch(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]
```
</details>

## Key Takeaways

- Generators use `yield` to produce values lazily, one at a time.
- Generator expressions use `()` and are memory-efficient.
- The iterator protocol is `__iter__` + `__next__` (raising `StopIteration`).
- `yield from` delegates to another iterable; generators are single-use.

---

▶️ **Run the examples:** `python advanced/14_generators_iteration.py`
⏮️ **Previous:** [Magic Methods](13_magic_methods.md) | ⏭️ **Next:** [Regular Expressions →](15_regular_expressions.md)
