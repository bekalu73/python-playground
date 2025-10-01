"""
BUILT-IN DATA TYPES & DYNAMIC TYPING
====================================

Key Points:
- Python is dynamically typed (no need to declare variable types)
- Variables can change type at runtime
- Main types: int, float, str, bool, list, dict, tuple, set
"""

# DYNAMIC TYPING EXAMPLES
x = 42           # int
print(f"x = {x}, type: {type(x)}")

x = "forty-two"  # now str
print(f"x = {x}, type: {type(x)}")

x = 3.14         # now float
print(f"x = {x}, type: {type(x)}")

x = True         # now bool
print(f"x = {x}, type: {type(x)}")

# BUILT-IN DATA TYPES
print("\n=== BUILT-IN DATA TYPES ===")

# Numbers
integer_num = 100
float_num = 3.14159
complex_num = 3 + 4j
print(f"Integer: {integer_num}")
print(f"Float: {float_num}")
print(f"Complex: {complex_num}")

# Strings
text = "Python Programming"
multiline = """This is a
multiline string"""
print(f"String: {text}")

# Boolean
is_python_fun = True
is_difficult = False
print(f"Boolean: {is_python_fun}")

# Collections
my_list = [1, 2, 3, "mixed", True]
my_tuple = (1, 2, 3)  # immutable
my_dict = {"name": "Alice", "age": 25}
my_set = {1, 2, 3, 3}  # unique elements only

print(f"List: {my_list}")
print(f"Tuple: {my_tuple}")
print(f"Dictionary: {my_dict}")
print(f"Set: {my_set}")

# TYPE CHECKING
def check_type(value):
    if isinstance(value, int):
        return "Integer"
    elif isinstance(value, str):
        return "String"
    elif isinstance(value, list):
        return "List"
    else:
        return "Other type"

# Test type checking
test_values = [42, "hello", [1, 2, 3], 3.14]
for val in test_values:
    print(f"{val} is a {check_type(val)}")

print("\nData types mastered! ✓")