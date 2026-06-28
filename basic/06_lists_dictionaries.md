# Lists & Dictionaries

> 📄 **Related code file:** [`06_lists_dictionaries.py`](06_lists_dictionaries.py)

## Overview

**Lists** and **dictionaries** are the two most important data structures in Python. Lists store ordered sequences of items; dictionaries store key-value pairs for fast lookups. Mastering them is essential for almost every Python program.

## Lists

A **list** is an ordered, mutable collection that allows duplicates.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]   # can mix types
```

### Accessing Elements (Indexing & Slicing)
```python
fruits[0]      # "apple"   (first — index starts at 0)
fruits[-1]     # "cherry"  (last — negative counts from the end)
fruits[1:3]    # ["banana", "cherry"]  (slice: start:stop)
fruits[::2]    # every 2nd element
```

### Common List Methods
```python
fruits.append("orange")        # add to end
fruits.insert(1, "grape")      # insert at index
fruits.extend(["mango", "kiwi"])  # add multiple
fruits.remove("grape")         # remove by value
last = fruits.pop()            # remove & return last
fruits.count("apple")          # how many times it appears
fruits.index("cherry")         # position of a value

numbers.sort()                 # sort in place
numbers.reverse()              # reverse in place
```

## List Comprehensions

A concise way to create lists from existing iterables.

```python
squares = [x**2 for x in range(5)]              # [0, 1, 4, 9, 16]
evens = [n for n in range(10) if n % 2 == 0]    # [0, 2, 4, 6, 8]
lengths = [len(word) for word in ["hi", "bye"]] # [2, 3]
```

**Syntax:** `[expression for item in iterable if condition]`

## Dictionaries

A **dictionary** stores key-value pairs. Keys must be unique and immutable.

```python
student = {"name": "Alice", "age": 20, "grade": "A"}
```

### Accessing Values
```python
student["name"]                  # "Alice"  (KeyError if missing)
student.get("age")               # 20
student.get("city", "Unknown")   # "Unknown" (safe — returns default)
```

### Modifying Dictionaries
```python
student["city"] = "New York"               # add/update one key
student.update({"major": "CS", "year": 2}) # add/update multiple
grade = student.pop("grade")               # remove & return value
```

### Iterating
```python
student.keys()      # all keys
student.values()    # all values
student.items()     # all (key, value) pairs

for key, value in student.items():
    print(f"{key}: {value}")
```

## Dictionary Comprehensions

```python
squares = {x: x**2 for x in range(5)}          # {0:0, 1:1, 2:4, ...}
word_lengths = {w: len(w) for w in ["a", "bb"]}  # {"a":1, "bb":2}
```

## Nested Structures

You can combine lists and dictionaries to model complex data.

```python
# List of dictionaries
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
]
for s in students:
    print(s["name"], s["grade"])

# Dictionary of lists
grades = {"math": [85, 90], "science": [92, 88]}
```

## Useful Patterns

```python
# Merge dictionaries (Python 3.9+)
merged = dict1 | dict2          # or {**dict1, **dict2}

# Build dict from two lists
person = dict(zip(["name", "age"], ["Alice", 25]))

# Find key with max value
scores = {"Alice": 85, "Bob": 92}
best = max(scores, key=scores.get)   # "Bob"
```

## Common Mistakes

❌ **KeyError from missing keys** — use `.get()` when unsure:
```python
student["phone"]            # KeyError!
student.get("phone", "")    # safe
```

❌ **Modifying a list while looping over it** — iterate over a copy instead.

❌ **Using a mutable type (list) as a dict key** — keys must be immutable (use tuples).

❌ **Confusing `append()` and `extend()`:**
```python
[1, 2].append([3, 4])   # [1, 2, [3, 4]]
[1, 2].extend([3, 4])   # [1, 2, 3, 4]
```

## Best Practices

✅ Use `.get()` for safe dictionary access.
✅ Use list/dict comprehensions for clarity (but don't over-nest them).
✅ Choose dictionaries for fast lookups by key; lists for ordered sequences.
✅ Use meaningful keys in dictionaries.

## Exercises

1. **Filter & transform:** From `nums = [1,2,3,4,5,6]`, build a list of squares of only the even numbers.

2. **Word counter:** Given a sentence, build a dictionary mapping each word to how many times it appears.

3. **Grade book:** Create a list of student dictionaries, then print the name of the student with the highest grade.

4. **Invert a dict:** Given `{"a": 1, "b": 2}`, produce `{1: "a", 2: "b"}` using a dict comprehension.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 1
result = [n**2 for n in nums if n % 2 == 0]

# Exercise 2
counts = {}
for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1

# Exercise 4
inverted = {v: k for k, v in original.items()}
```
</details>

## Key Takeaways

- **Lists** are ordered and mutable; access by index, slice with `[start:stop]`.
- **Dictionaries** store key-value pairs; use `.get()` for safe access.
- **Comprehensions** create lists/dicts concisely.
- Nest structures to model real-world data.

---

▶️ **Run the examples:** `python basic/06_lists_dictionaries.py`
⏮️ **Previous:** [Functions & Scope](05_functions_scope.md) | ⏭️ **Next:** [Strings & Formatting →](07_strings_formatting.md)
