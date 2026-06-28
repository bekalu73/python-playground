# Syntax & Indentation

> 📄 **Related code file:** [`01_syntax_indentation.py`](01_syntax_indentation.py)

## Overview

Unlike many programming languages that use curly braces `{}` to group code, Python uses **indentation** (whitespace) to define blocks of code. This makes Python code clean and readable, but it also means indentation is **mandatory**, not optional.

## The Concept

In Python, a **code block** is a group of statements that belong together — like the body of a loop, an `if` statement, or a function. Python knows which statements belong to a block based on how they're indented.

```python
if True:
    print("This is inside the if block")   # Indented = inside the block
    print("This too")                       # Same indentation = same block
print("This is outside the if block")       # Not indented = outside
```

## Syntax Rules

1. **Use 4 spaces** per indentation level (the official standard).
2. **Be consistent** — don't mix tabs and spaces.
3. A **colon `:`** introduces a new block (after `if`, `for`, `while`, `def`, `class`, etc.).
4. All statements in the same block must have the **same indentation**.

```python
def function_name():       # Colon starts a block
    statement_1            # 4 spaces indentation
    statement_2            # Same level = same block
    if condition:          # Nested block needs another colon
        nested_statement   # 8 spaces (two levels deep)
```

## Practical Examples

### Example 1: A function with conditionals

```python
def check_grade(score):
    if score >= 90:
        print("A grade")
    elif score >= 80:
        print("B grade")
    else:
        print("Need improvement")

check_grade(95)   # Output: A grade
check_grade(75)   # Output: Need improvement
```

### Example 2: Loops with nested conditions

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
```

## Common Mistakes

❌ **Inconsistent indentation:**
```python
if True:
    print("First line")
      print("Second line")   # IndentationError: unexpected indent
```

❌ **Forgetting indentation entirely:**
```python
if True:
print("Hello")   # IndentationError: expected an indented block
```

❌ **Mixing tabs and spaces:**
```python
if True:
    print("uses spaces")
	print("uses a tab")   # TabError: inconsistent use of tabs and spaces
```

❌ **Forgetting the colon:**
```python
if True          # SyntaxError: expected ':'
    print("Hi")
```

## Best Practices

✅ Always use **4 spaces** (configure your editor to insert spaces when you press Tab).
✅ Enable "show whitespace" in your editor to catch mixing.
✅ Keep nesting shallow — deeply nested code is hard to read.
✅ Let VS Code auto-indent for you (it adds indentation after a colon automatically).

## Exercises

1. **Fix the indentation:** The following code has errors. Rewrite it correctly.
   ```python
   def greet(name):
   print("Hello", name)
       print("Welcome!")
   ```

2. **Write a function** `describe_number(n)` that prints `"positive"`, `"negative"`, or `"zero"` using proper `if/elif/else` indentation.

3. **Create a nested loop** that prints a 3×3 grid of asterisks (`*`), using indentation correctly.

<details>
<summary>💡 Solution hints</summary>

```python
# Exercise 1
def greet(name):
    print("Hello", name)
    print("Welcome!")

# Exercise 3
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()
```
</details>

## Key Takeaways

- Python uses **indentation** instead of braces to define code blocks.
- The standard is **4 spaces** per level.
- A **colon** `:` always precedes an indented block.
- Inconsistent indentation raises `IndentationError` or `TabError`.

---

▶️ **Run the examples:** `python basic/01_syntax_indentation.py`
⏭️ **Next:** [Data Types & Dynamic Typing →](02_data_types.md)
