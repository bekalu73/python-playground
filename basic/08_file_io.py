"""
FILE I/O (open, context managers)
=================================

Key Points:
- Opening files with open()
- File modes: 'r', 'w', 'a', 'x', 'b', 't'
- Context managers (with statement)
- Reading methods: read(), readline(), readlines()
- Writing methods: write(), writelines()
- File handling best practices
"""

import os

print("=== BASIC FILE OPERATIONS ===")

# Create a sample file first
sample_content = """Line 1: Hello World
Line 2: Python Programming
Line 3: File I/O Operations
Line 4: Context Managers
Line 5: Best Practices"""

# Writing to file (creates new file or overwrites existing)
with open("sample.txt", "w") as file:
    file.write(sample_content)
print("✓ Created sample.txt")

print("\n=== READING FILES ===")

# Method 1: Read entire file
with open("sample.txt", "r") as file:
    content = file.read()
    print("Entire file content:")
    print(content)

print("\n" + "="*40)

# Method 2: Read line by line
with open("sample.txt", "r") as file:
    print("Reading line by line:")
    line_number = 1
    for line in file:
        print(f"{line_number}: {line.strip()}")
        line_number += 1

print("\n" + "="*40)

# Method 3: Read all lines into a list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("All lines as list:")
    for i, line in enumerate(lines, 1):
        print(f"{i}: {line.strip()}")

print("\n=== WRITING FILES ===")

# Writing mode ('w') - overwrites existing file
data_to_write = ["Apple\n", "Banana\n", "Cherry\n", "Date\n"]

with open("fruits.txt", "w") as file:
    file.writelines(data_to_write)
print("✓ Created fruits.txt")

# Append mode ('a') - adds to existing file
with open("fruits.txt", "a") as file:
    file.write("Elderberry\n")
    file.write("Fig\n")
print("✓ Appended to fruits.txt")

# Read the updated file
with open("fruits.txt", "r") as file:
    print("Updated fruits.txt:")
    print(file.read())

print("\n=== FILE MODES ===")

# Different file modes
modes_explanation = {
    'r': 'Read only (default)',
    'w': 'Write only (overwrites existing)',
    'a': 'Append only',
    'x': 'Create new file (fails if exists)',
    'r+': 'Read and write',
    'w+': 'Write and read (overwrites)',
    'a+': 'Append and read',
    'rb': 'Read binary',
    'wb': 'Write binary',
    'ab': 'Append binary'
}

print("File modes:")
for mode, description in modes_explanation.items():
    print(f"  '{mode}': {description}")

print("\n=== CONTEXT MANAGERS (WITH STATEMENT) ===")

# Why use context managers?
print("Without context manager (NOT RECOMMENDED):")
print("file = open('sample.txt', 'r')")
print("content = file.read()")
print("file.close()  # Must remember to close!")

print("\nWith context manager (RECOMMENDED):")
print("with open('sample.txt', 'r') as file:")
print("    content = file.read()")
print("# File automatically closed!")

# Demonstrating automatic file closing
with open("sample.txt", "r") as file:
    print(f"File closed? {file.closed}")  # False
print(f"File closed after with block? {file.closed}")  # True

print("\n=== ERROR HANDLING ===")

# Handling file not found
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ File not found!")

# Handling permission errors
try:
    with open("readonly.txt", "w") as file:
        file.write("test")
except PermissionError:
    print("❌ Permission denied!")

print("\n=== WORKING WITH CSV-LIKE DATA ===")

# Writing structured data
students = [
    "Name,Age,Grade",
    "Alice,20,A",
    "Bob,21,B",
    "Charlie,19,A-"
]

with open("students.csv", "w") as file:
    for line in students:
        file.write(line + "\n")

# Reading structured data
with open("students.csv", "r") as file:
    print("Student data:")
    for line in file:
        print(f"  {line.strip()}")

print("\n=== FILE OPERATIONS ===")

# Check if file exists
if os.path.exists("sample.txt"):
    print("✓ sample.txt exists")
    
    # Get file size
    size = os.path.getsize("sample.txt")
    print(f"File size: {size} bytes")

# List files in current directory
print("\nFiles in current directory:")
for file in os.listdir("."):
    if file.endswith(".txt") or file.endswith(".csv"):
        print(f"  {file}")

print("\n=== EXAM FOCUS: COMMON PATTERNS ===")

# Pattern 1: Count lines in file
def count_lines(filename):
    try:
        with open(filename, "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0

print(f"Lines in sample.txt: {count_lines('sample.txt')}")

# Pattern 2: Find specific content
def find_in_file(filename, search_term):
    try:
        with open(filename, "r") as file:
            for line_num, line in enumerate(file, 1):
                if search_term in line:
                    print(f"Found '{search_term}' at line {line_num}: {line.strip()}")
    except FileNotFoundError:
        print(f"File {filename} not found")

find_in_file("sample.txt", "Python")

# Pattern 3: Copy file content
def copy_file(source, destination):
    try:
        with open(source, "r") as src, open(destination, "w") as dst:
            dst.write(src.read())
        print(f"✓ Copied {source} to {destination}")
    except FileNotFoundError:
        print(f"❌ Source file {source} not found")

copy_file("sample.txt", "sample_copy.txt")

print("\n=== CLEANUP ===")
# Clean up created files
files_to_remove = ["sample.txt", "fruits.txt", "students.csv", "sample_copy.txt"]
for file in files_to_remove:
    try:
        os.remove(file)
        print(f"✓ Removed {file}")
    except FileNotFoundError:
        pass

print("\nFile I/O mastered! ✓")