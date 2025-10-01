"""
OPERATORS (ARITHMETIC, LOGICAL, MEMBERSHIP)
==========================================

Key Points:
- Arithmetic: +, -, *, /, //, %, **
- Logical: and, or, not
- Comparison: ==, !=, <, >, <=, >=
- Membership: in, not in
- Identity: is, is not
"""

print("=== ARITHMETIC OPERATORS ===")
a, b = 17, 5

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")  # Integer division
print(f"Modulus: {a} % {b} = {a % b}")           # Remainder
print(f"Exponentiation: {a} ** {b} = {a ** b}")

print("\n=== LOGICAL OPERATORS ===")
x, y = True, False
print(f"x = {x}, y = {y}")
print(f"x and y = {x and y}")
print(f"x or y = {x or y}")
print(f"not x = {not x}")

# Practical example
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")

print("\n=== COMPARISON OPERATORS ===")
num1, num2 = 10, 20
print(f"num1 = {num1}, num2 = {num2}")
print(f"Equal: {num1 == num2}")
print(f"Not equal: {num1 != num2}")
print(f"Less than: {num1 < num2}")
print(f"Greater than: {num1 > num2}")
print(f"Less or equal: {num1 <= num2}")
print(f"Greater or equal: {num1 >= num2}")

print("\n=== MEMBERSHIP OPERATORS ===")
fruits = ["apple", "banana", "orange"]
print(f"Fruits: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# String membership
text = "Python Programming"
print(f"'Python' in text: {'Python' in text}")

print("\n=== IDENTITY OPERATORS ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2: {list1 is list2}")  # False - different objects
print(f"list1 is list3: {list1 is list3}")  # True - same object
print(f"list1 == list2: {list1 == list2}")  # True - same content

# EXAM TRICK: Floor division vs regular division
print(f"\n=== EXAM FOCUS ===")
print(f"7 / 3 = {7 / 3}")    # 2.333...
print(f"7 // 3 = {7 // 3}")  # 2 (floor division)
print(f"7 % 3 = {7 % 3}")    # 1 (remainder)

# Complex logical expressions
print(f"(5 > 3) and (2 < 1) = {(5 > 3) and (2 < 1)}")  # False

print("\nOperators mastered! ✓")