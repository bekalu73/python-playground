# File I/O

> 📄 **Related code file:** [`08_file_io.py`](08_file_io.py)

## Overview

**File I/O** (Input/Output) lets your programs read from and write to files on disk. This is essential for saving data, reading configuration, processing logs, and more. Python makes file handling simple and safe with the `with` statement.

## Opening Files

Use the built-in `open()` function, which takes a filename and a **mode**.

```python
file = open("data.txt", "r")   # open for reading
content = file.read()
file.close()                   # must remember to close!
```

## The `with` Statement (Context Manager) — Preferred ✅

The `with` statement automatically closes the file for you, even if an error occurs. **Always use it.**

```python
with open("data.txt", "r") as file:
    content = file.read()
# File is automatically closed here
```

Compare:
```python
# ❌ Manual (error-prone — easy to forget close())
file = open("data.txt", "r")
content = file.read()
file.close()

# ✅ Context manager (automatic cleanup)
with open("data.txt", "r") as file:
    content = file.read()
```

## File Modes

| Mode | Meaning |
|------|---------|
| `"r"` | Read (default) — error if file doesn't exist |
| `"w"` | Write — **overwrites** existing content |
| `"a"` | Append — adds to the end |
| `"x"` | Create — error if file already exists |
| `"r+"` | Read and write |
| `"b"` | Binary mode (e.g., `"rb"`, `"wb"`) |
| `"t"` | Text mode (default) |

## Reading Files

### Read the entire file
```python
with open("sample.txt", "r") as file:
    content = file.read()       # one big string
```

### Read line by line (memory-efficient)
```python
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())     # strip() removes the trailing newline
```

### Read all lines into a list
```python
with open("sample.txt", "r") as file:
    lines = file.readlines()    # ["line1\n", "line2\n", ...]
```

## Writing Files

### Write mode (overwrites)
```python
with open("output.txt", "w") as file:
    file.write("Hello World\n")
    file.writelines(["Line 1\n", "Line 2\n"])
```

### Append mode (adds to end)
```python
with open("output.txt", "a") as file:
    file.write("This is added at the end\n")
```

> ⚠️ **`"w"` deletes existing content!** Use `"a"` if you want to keep what's already there.

## Error Handling

Files may not exist or be inaccessible. Handle these cases gracefully.

```python
try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
```

## Working with File Paths (`os` module)

```python
import os

os.path.exists("sample.txt")    # True/False
os.path.getsize("sample.txt")   # size in bytes
os.remove("sample.txt")         # delete a file
os.listdir(".")                 # list files in a directory
```

## Common Patterns

```python
# Count lines in a file
def count_lines(filename):
    with open(filename, "r") as file:
        return len(file.readlines())

# Search for text in a file
def find_in_file(filename, term):
    with open(filename, "r") as file:
        for num, line in enumerate(file, 1):
            if term in line:
                print(f"Line {num}: {line.strip()}")

# Copy a file
with open("source.txt", "r") as src, open("dest.txt", "w") as dst:
    dst.write(src.read())
```

## Common Mistakes

❌ **Forgetting to close a file** (without `with`) — can corrupt data or leak resources.

❌ **Using `"w"` when you meant `"a"`** — silently erases the file!

❌ **Forgetting to strip newlines** when reading lines:
```python
for line in file:
    print(line)         # prints extra blank lines
    print(line.strip()) # better
```

❌ **Not handling `FileNotFoundError`** for files that might not exist.

## Best Practices

✅ Always use the `with` statement.
✅ Specify the mode explicitly so intent is clear.
✅ Handle exceptions (`FileNotFoundError`, `PermissionError`).
✅ Read large files line by line, not all at once.
✅ For CSV/JSON data, use the dedicated `csv` and `json` modules.

## Exercises

1. **Write & read:** Create a file `notes.txt`, write three lines to it, then read and print them.

2. **Line counter:** Write a function that returns the number of non-empty lines in a file.

3. **Append log:** Write a function `log_message(msg)` that appends a message to `app.log` on a new line.

4. **Word frequency:** Read a text file and print the 3 most common words.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 1
with open("notes.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")
with open("notes.txt", "r") as f:
    print(f.read())

# Exercise 3
def log_message(msg):
    with open("app.log", "a") as f:
        f.write(msg + "\n")
```
</details>

## Key Takeaways

- Always use `with open(...) as file:` — it auto-closes the file.
- Modes: `"r"` read, `"w"` overwrite, `"a"` append.
- Read with `read()`, `readline()`, `readlines()`, or by iterating.
- Handle `FileNotFoundError` and other I/O exceptions.

---

▶️ **Run the examples:** `python basic/08_file_io.py`
⏮️ **Previous:** [Strings & Formatting](07_strings_formatting.md) | ⏭️ **Next:** [Intermediate: Packaging & Virtual Environments →](../intermediate/09_packaging_venv.md)
