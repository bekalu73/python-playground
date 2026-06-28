# Regular Expressions

> 📄 **Related code file:** [`15_regular_expressions.py`](15_regular_expressions.py)

## Overview

**Regular expressions** (regex) are a powerful mini-language for matching patterns in text. They're used for validation (emails, phone numbers), searching, extraction, and find-and-replace. Python's `re` module provides full regex support.

```python
import re
```

## Core Functions

| Function | What it does |
|----------|--------------|
| `re.search(pattern, text)` | Find the **first** match anywhere |
| `re.match(pattern, text)` | Match only at the **start** of the string |
| `re.findall(pattern, text)` | Return **all** matches as a list |
| `re.sub(pattern, repl, text)` | **Replace** matches with new text |
| `re.compile(pattern)` | Pre-compile a pattern for reuse |

```python
text = "Email: support@example.com or sales@company.org"

re.search(r'\S+@\S+\.\S+', text).group()  # 'support@example.com'
re.findall(r'\S+@\S+\.\S+', text)         # both emails
```

> 💡 Always use **raw strings** (`r'...'`) for patterns so backslashes are treated literally.

## Character Classes

| Pattern | Matches |
|---------|---------|
| `\d` | A digit `[0-9]` |
| `\D` | A non-digit |
| `\w` | A word character `[a-zA-Z0-9_]` |
| `\W` | A non-word character |
| `\s` | Whitespace |
| `\S` | Non-whitespace |
| `.` | Any character (except newline) |
| `[aeiou]` | Any character in the set |
| `[A-Z]` | Any uppercase letter |

## Quantifiers & Anchors

| Pattern | Meaning |
|---------|---------|
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 (optional) |
| `{n}` | Exactly n |
| `{n,m}` | Between n and m |
| `^` | Start of string/line |
| `$` | End of string/line |
| `\b` | Word boundary |
| `|` | OR (`cat|dog`) |

```python
re.findall(r'\d+', "abc 123 def 456")     # ['123', '456']
re.findall(r'\b\w{4}\b', "this is a test") # ['this', 'test']  (4-letter words)
re.match(r'^Hello', "Hello world")          # matches start
```

## Validation Examples

```python
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    return bool(re.match(r'^\d{3}-\d{3}-\d{4}$', phone))   # 123-456-7890
```

## Groups & Capturing

Parentheses `()` create **groups** to extract parts of a match.

```python
date_text = "Date: 2024-03-15"
pattern = r'(\d{4})-(\d{2})-(\d{2})'

match = re.search(pattern, date_text)
match.group(1)   # '2024' (year)
match.group(2)   # '03'   (month)
match.group(3)   # '15'   (day)

# Named groups are clearer:
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, date_text)
match.groupdict()   # {'year': '2024', 'month': '03', 'day': '15'}
```

## Substitution

```python
text = "Call 123-456-7890 or email me@x.com"

re.sub(r'\d{3}-\d{3}-\d{4}', '[PHONE]', text)   # masks the phone

# Use groups in the replacement to reorder:
re.sub(r'(\w+) (\w+)', r'\2, \1', "John Smith")  # 'Smith, John'
```

## Flags

Flags modify matching behavior:

```python
re.findall(r'hello', "Hello HELLO hello", re.IGNORECASE)  # all three
re.findall(r'^line', text, re.MULTILINE)   # ^ matches each line start
# re.DOTALL — . also matches newlines
```

## Compiled Patterns

When using a pattern repeatedly, compile it once for better performance:

```python
email_re = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
email_re.search(text)
email_re.findall(text)
```

## Common Mistakes

❌ **Forgetting raw strings:**
```python
re.findall("\d+", text)    # \d may be misinterpreted; use r"\d+"
```

❌ **Confusing `match` and `search`:** `match` only checks the **start** of the string.

❌ **Greedy matching surprises:** `.*` matches as much as possible. Use `.*?` for non-greedy.
```python
re.findall(r'<.*>', "<a><b>")    # ['<a><b>'] (greedy)
re.findall(r'<.*?>', "<a><b>")   # ['<a>', '<b>'] (lazy)
```

❌ **Over-engineering email/URL regex** — for strict validation, prefer dedicated libraries.

## Best Practices

✅ Always use raw strings (`r'...'`) for patterns.
✅ Compile patterns you reuse with `re.compile()`.
✅ Use named groups for readability.
✅ Test patterns on real sample data (tools like regex101.com help).
✅ Keep patterns simple; comment complex ones with `re.VERBOSE`.

## Exercises

1. **Extract numbers:** Write a function that returns all integers found in a string.

2. **Validate a username:** Match usernames that are 3–16 characters of letters, digits, or underscores.

3. **Mask emails:** Replace every email in a text with `[EMAIL HIDDEN]`.

4. **Parse a log line:** Given `"2024-03-15 ERROR Something failed"`, extract the date, level, and message using named groups.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 1
def extract_numbers(text):
    return re.findall(r'\d+', text)

# Exercise 2
def valid_username(name):
    return bool(re.match(r'^\w{3,16}$', name))

# Exercise 4
m = re.match(r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>\w+) (?P<msg>.+)', line)
```
</details>

## Key Takeaways

- `re.search`, `re.match`, `re.findall`, `re.sub` are the core functions.
- Character classes (`\d`, `\w`, `\s`) and quantifiers (`*`, `+`, `?`, `{n}`) build patterns.
- Use `()` for capturing groups and `(?P<name>...)` for named groups.
- Always use raw strings and compile reused patterns.

---

▶️ **Run the examples:** `python advanced/15_regular_expressions.py`
⏮️ **Previous:** [Generators & Iteration](14_generators_iteration.md) | ⏭️ **Next:** [Asynchronous I/O →](16_async_io.md)
