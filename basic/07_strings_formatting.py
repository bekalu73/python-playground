"""
STRINGS & FORMATTING (f-strings, methods)
=========================================

Key Points:
- String creation and indexing
- String methods: split, join, strip, replace, etc.
- String formatting: f-strings, .format(), % formatting
- String operations and concatenation
- Escape characters
"""

print("=== STRING BASICS ===")
# Note: Strings are immutable sequences - operations create new strings

# Creating strings
single_quote = 'Hello World'
double_quote = "Hello World"
triple_quote = """This is a
multiline string"""

print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"Triple quote: {triple_quote}")

# String indexing and slicing
text = "Python Programming"
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Slice [0:6]: {text[0:6]}")
print(f"Slice [7:]: {text[7:]}")
print(f"Every 2nd character: {text[::2]}")

print("\n=== STRING METHODS ===")
# Note: Strings have many built-in methods for manipulation - they don't modify original

sample_text = "  Hello, Python World!  "
print(f"Original: '{sample_text}'")

# Case methods
print(f"Upper: {sample_text.upper()}")
print(f"Lower: {sample_text.lower()}")
print(f"Title: {sample_text.title()}")
print(f"Capitalize: {sample_text.capitalize()}")

# Whitespace methods
print(f"Strip: '{sample_text.strip()}'")
print(f"Left strip: '{sample_text.lstrip()}'")
print(f"Right strip: '{sample_text.rstrip()}'")

# Search methods
print(f"Find 'Python': {sample_text.find('Python')}")
print(f"Count 'l': {sample_text.count('l')}")
print(f"Starts with '  Hello': {sample_text.startswith('  Hello')}")
print(f"Ends with '!  ': {sample_text.endswith('!  ')}")

# Replace method
replaced = sample_text.replace("Python", "Java")
print(f"Replaced: {replaced}")

print("\n=== STRING SPLITTING AND JOINING ===")
# Note: split() breaks strings into lists, join() combines lists into strings

# Split method
sentence = "apple,banana,cherry,orange"
fruits = sentence.split(",")
print(f"Split by comma: {fruits}")

words = "Hello Python World".split()
print(f"Split by whitespace: {words}")

# Join method
joined = " | ".join(fruits)
print(f"Joined with ' | ': {joined}")

# Join with different separator
path = "/".join(["home", "user", "documents", "file.txt"])
print(f"Path: {path}")

print("\n=== STRING FORMATTING ===")
# Note: f-strings (f'') are the modern, preferred way to format strings in Python

name = "Alice"
age = 25
score = 87.5

# f-strings (Python 3.6+) - PREFERRED METHOD
print(f"Name: {name}, Age: {age}, Score: {score}")
print(f"Score percentage: {score:.1f}%")
print(f"Name in uppercase: {name.upper()}")

# .format() method
print("Name: {}, Age: {}, Score: {}".format(name, age, score))
print("Name: {0}, Age: {1}, Score: {0}".format(name, age))  # Positional
print("Name: {n}, Age: {a}, Score: {s}".format(n=name, a=age, s=score))  # Named

# % formatting (older style)
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))

print("\n=== ADVANCED F-STRING FEATURES ===")
# Note: f-strings can contain expressions, function calls, and formatting specifiers

# Expressions in f-strings
x, y = 10, 20
print(f"Sum: {x + y}")
print(f"Max: {max(x, y)}")

# Formatting numbers
pi = 3.14159
print(f"Pi: {pi:.2f}")        # 2 decimal places
print(f"Pi: {pi:.4f}")        # 4 decimal places

# Formatting with width and alignment
print(f"Left aligned: '{name:<10}'")
print(f"Right aligned: '{name:>10}'")
print(f"Center aligned: '{name:^10}'")

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"Current time: {now:%Y-%m-%d %H:%M:%S}")

print("\n=== ESCAPE CHARACTERS ===")
# Note: Backslash (\) escapes special characters - use raw strings r'' to ignore escapes

# Common escape characters
print("Line 1\nLine 2")           # Newline
print("Column 1\tColumn 2")       # Tab
print("He said, \"Hello!\"")      # Quote
print("Path: C:\\Users\\Alice")   # Backslash

# Raw strings (ignore escape characters)
raw_path = r"C:\Users\Alice\Documents"
print(f"Raw string: {raw_path}")

print("\n=== STRING VALIDATION ===")
# Note: String validation methods return True/False - useful for input checking

# Check string properties
test_strings = ["123", "abc", "ABC", "Hello World", "  ", ""]

for s in test_strings:
    print(f"'{s}': digit={s.isdigit()}, alpha={s.isalpha()}, "
          f"alnum={s.isalnum()}, space={s.isspace()}")

print("\n=== EXAM FOCUS: COMMON PATTERNS ===")

# String reversal
text = "Python"
reversed_text = text[::-1]
print(f"Reversed '{text}': {reversed_text}")

# Check palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

test_words = ["racecar", "hello", "A man a plan a canal Panama"]
for word in test_words:
    print(f"'{word}' is palindrome: {is_palindrome(word)}")

# Count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

print(f"Vowels in 'Python Programming': {count_vowels('Python Programming')}")

# Template strings
template = "Hello {name}, your score is {score}%"
result = template.format(name="Bob", score=95)
print(f"Template result: {result}")

print("\nStrings and formatting mastered! ✓")