"""
LISTS & DICTIONARIES
====================

Key Points:
- Lists: ordered, mutable, allow duplicates
- List methods: append, extend, insert, remove, pop
- List comprehensions
- Dictionaries: key-value pairs, mutable, unique keys
- Dictionary methods: get, keys, values, items
- Dictionary comprehensions
"""

print("=== LISTS BASICS ===")
# Note: Lists are ordered, mutable collections that allow duplicates

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# Accessing elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

print("\n=== LIST METHODS ===")
# Note: Lists have many built-in methods for adding, removing, and organizing elements

# Adding elements
fruits.append("orange")        # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "grape")      # Insert at index
print(f"After insert: {fruits}")

fruits.extend(["mango", "kiwi"])  # Add multiple
print(f"After extend: {fruits}")

# Removing elements
fruits.remove("grape")         # Remove by value
print(f"After remove: {fruits}")

popped = fruits.pop()          # Remove and return last
print(f"Popped: {popped}, List: {fruits}")

popped_index = fruits.pop(1)   # Remove at index
print(f"Popped at index 1: {popped_index}, List: {fruits}")

# Other useful methods
print(f"Count of 'apple': {fruits.count('apple')}")
print(f"Index of 'cherry': {fruits.index('cherry')}")

# Sorting
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(f"Sorted numbers: {numbers}")

numbers.reverse()
print(f"Reversed: {numbers}")

print("\n=== LIST COMPREHENSIONS ===")
# Note: List comprehensions create new lists in a concise, readable way

# Basic list comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# With condition
evens = [n for n in range(10) if n % 2 == 0]
print(f"Even numbers: {evens}")

# More complex example
words = ["hello", "world", "python", "programming"]
lengths = [len(word) for word in words]
print(f"Word lengths: {lengths}")

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

print("\n=== DICTIONARIES BASICS ===")
# Note: Dictionaries store key-value pairs - keys must be unique and immutable

# Creating dictionaries
student = {"name": "Alice", "age": 20, "grade": "A"}
empty_dict = {}
dict_from_pairs = dict([("a", 1), ("b", 2)])

print(f"Student: {student}")
print(f"Dict from pairs: {dict_from_pairs}")

# Accessing values
print(f"Student name: {student['name']}")
print(f"Student age: {student.get('age')}")
print(f"Student city: {student.get('city', 'Not specified')}")  # Default value

print("\n=== DICTIONARY METHODS ===")
# Note: Dictionaries have methods for accessing keys, values, and items safely

# Adding/updating
student["city"] = "New York"
student.update({"major": "Computer Science", "year": 2})
print(f"Updated student: {student}")

# Getting keys, values, items
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Removing
removed_grade = student.pop("grade")
print(f"Removed grade: {removed_grade}")
print(f"After pop: {student}")

# Copy dictionary
student_copy = student.copy()
print(f"Copy: {student_copy}")

print("\n=== DICTIONARY COMPREHENSIONS ===")
# Note: Dictionary comprehensions create new dictionaries with {key: value} syntax

# Basic dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From existing data
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths dict: {word_lengths}")

print("\n=== NESTED STRUCTURES ===")
# Note: You can nest lists and dictionaries to create complex data structures

# List of dictionaries
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

print("Students:")
for student in students:
    print(f"  {student['name']}: {student['grade']}")

# Dictionary of lists
grades = {
    "math": [85, 90, 78],
    "science": [92, 88, 85],
    "english": [78, 85, 90]
}

print(f"Math grades: {grades['math']}")

print("\n=== EXAM FOCUS: COMMON OPERATIONS ===")

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2  # Or use {**dict1, **dict2}
print(f"Merged: {merged}")

# List to dictionary
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = dict(zip(keys, values))
print(f"Person: {person}")

# Finding max/min in dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
best_student = max(scores, key=scores.get)
print(f"Best student: {best_student} with {scores[best_student]}")

print("\nLists and dictionaries mastered! ✓")