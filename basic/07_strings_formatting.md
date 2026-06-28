# Strings & Formatting

> 📄 **Related code file:** [`07_strings_formatting.py`](07_strings_formatting.py)

## Overview

**Strings** represent text and are one of the most-used data types. Python provides powerful tools for creating, manipulating, and formatting strings. Importantly, strings are **immutable** — every operation creates a new string rather than changing the original.

## Creating Strings

```python
single = 'Hello World'
double = "Hello World"
triple = """This is a
multiline string"""
```

## Indexing & Slicing

Strings work like sequences of characters.

```python
text = "Python Programming"
text[0]      # "P"   (first character)
text[-1]     # "g"   (last character)
text[0:6]    # "Python"  (slice)
text[7:]     # "Programming"
text[::2]    # every 2nd character
text[::-1]   # reversed string
```

## Common String Methods

Since strings are immutable, these all **return new strings**.

```python
s = "  Hello, Python!  "

# Case
s.upper()        # "  HELLO, PYTHON!  "
s.lower()        # "  hello, python!  "
s.title()        # "  Hello, Python!  "
s.capitalize()   # "  hello, python!  "

# Whitespace
s.strip()        # "Hello, Python!" (remove both ends)
s.lstrip()       # left only
s.rstrip()       # right only

# Search
s.find("Python")     # index, or -1 if not found
s.count("l")         # number of occurrences
s.startswith("  He") # True
s.endswith("!  ")    # True
s.replace("Python", "Java")
```

## Splitting & Joining

```python
# split: string → list
"a,b,c".split(",")          # ["a", "b", "c"]
"Hello World".split()       # ["Hello", "World"] (splits on whitespace)

# join: list → string
" | ".join(["a", "b", "c"]) # "a | b | c"
"/".join(["home", "user"])  # "home/user"
```

## String Formatting

### f-strings (Python 3.6+) — Preferred ✅
```python
name, age, score = "Alice", 25, 87.5
print(f"Name: {name}, Age: {age}")
print(f"Score: {score:.1f}%")        # one decimal place
print(f"Upper: {name.upper()}")      # expressions allowed
print(f"Sum: {10 + 20}")             # 30
```

### .format() method
```python
"Name: {}, Age: {}".format(name, age)
"Name: {0}, Age: {1}".format(name, age)        # positional
"Name: {n}, Age: {a}".format(n=name, a=age)    # named
```

### % formatting (older style)
```python
"Name: %s, Age: %d, Score: %.1f" % (name, age, score)
```

## Format Specifiers

```python
pi = 3.14159
f"{pi:.2f}"        # "3.14"  (2 decimals)
f"{name:<10}"      # left-aligned in 10 chars
f"{name:>10}"      # right-aligned
f"{name:^10}"      # centered
f"{1000000:,}"     # "1,000,000" (thousands separator)

from datetime import datetime
f"{datetime.now():%Y-%m-%d}"   # date formatting
```

## Escape Characters

```python
"Line 1\nLine 2"        # \n = newline
"Col 1\tCol 2"          # \t = tab
"He said, \"Hi\""       # \" = literal quote
"C:\\Users\\Alice"      # \\ = literal backslash

# Raw strings ignore escapes (useful for paths/regex)
r"C:\Users\Alice"       # backslashes stay literal
```

## String Validation

```python
"123".isdigit()    # True
"abc".isalpha()    # True
"abc123".isalnum() # True
"   ".isspace()    # True
```

## Common Mistakes

❌ **Trying to modify a string in place:**
```python
s = "hello"
s[0] = "H"   # TypeError — strings are immutable
s = "H" + s[1:]   # create a new string instead
```

❌ **Concatenating strings with non-strings:**
```python
"Age: " + 25      # TypeError
f"Age: {25}"      # use f-strings or str(25)
```

❌ **Forgetting `split()` returns a list, not a string.**

## Best Practices

✅ Use **f-strings** for formatting (clear and fast).
✅ Use raw strings (`r"..."`) for file paths and regex patterns.
✅ Build large strings with `"".join(list)` rather than repeated `+`.
✅ Use `.strip()` to clean user input.

## Exercises

1. **Palindrome check:** Write `is_palindrome(s)` that ignores case and spaces (e.g., "A man a plan a canal Panama" → True).

2. **Count vowels:** Write a function that counts the vowels in a string.

3. **Title formatter:** Given `"the lord of the rings"`, produce `"The Lord Of The Rings"`.

4. **Initials:** From a full name like `"Alice Marie Smith"`, produce `"A.M.S."`.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 1
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Exercise 2
def count_vowels(text):
    return sum(1 for c in text if c in "aeiouAEIOU")

# Exercise 4
initials = ".".join(word[0].upper() for word in name.split()) + "."
```
</details>

## Key Takeaways

- Strings are **immutable** sequences of characters.
- Slice with `[start:stop:step]`; `[::-1]` reverses.
- Prefer **f-strings** for formatting.
- Methods like `split()`, `join()`, `strip()`, `replace()` return new strings.

---

▶️ **Run the examples:** `python basic/07_strings_formatting.py`
⏮️ **Previous:** [Lists & Dictionaries](06_lists_dictionaries.md) | ⏭️ **Next:** [File I/O →](08_file_io.md)
