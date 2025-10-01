"""
FUNCTIONS & SCOPE (def, *args, **kwargs)
=======================================

Key Points:
- Function definition with def
- Parameters vs arguments
- Default parameters
- *args for variable positional arguments
- **kwargs for variable keyword arguments
- Local vs global scope
- return statement
"""

print("=== BASIC FUNCTIONS ===")

def greet(name="World"):
    """Function with default parameter"""
    return f"Hello, {name}!"

print(greet())          # Hello, World!
print(greet("Alice"))   # Hello, Alice!

print("\n=== MULTIPLE PARAMETERS ===")

def calculate_area(length, width, unit="sq meters"):
    """Function with multiple parameters"""
    area = length * width
    return f"Area: {area} {unit}"

print(calculate_area(5, 3))
print(calculate_area(5, 3, "sq feet"))

print("\n=== *ARGS - VARIABLE POSITIONAL ARGUMENTS ===")

def sum_numbers(*args):
    """Accept any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_numbers(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_numbers(1, 2, 3, 4, 5)}")

def print_info(name, *subjects):
    """Mix regular parameter with *args"""
    print(f"Student: {name}")
    print("Subjects:", end=" ")
    for subject in subjects:
        print(subject, end=" ")
    print()

print_info("Bob", "Math", "Science", "English")

print("\n=== **KWARGS - VARIABLE KEYWORD ARGUMENTS ===")

def create_profile(**kwargs):
    """Accept any number of keyword arguments"""
    print("Profile created:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

create_profile(name="Alice", age=25, city="New York", job="Engineer")

print("\n=== COMBINING ALL PARAMETER TYPES ===")

def flexible_function(required, default="default", *args, **kwargs):
    """Function with all parameter types"""
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_function("must_have", "custom", 1, 2, 3, name="Bob", age=30)

print("\n=== SCOPE EXAMPLES ===")

# Global variable
global_var = "I'm global"

def scope_demo():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause NameError

# Modifying global variable
counter = 0

def increment():
    global counter
    counter += 1
    return counter

print(f"Counter: {increment()}")  # 1
print(f"Counter: {increment()}")  # 2

print("\n=== NESTED FUNCTIONS & CLOSURES ===")

def outer_function(x):
    def inner_function(y):
        return x + y  # Access outer function's variable
    return inner_function

add_10 = outer_function(10)
print(f"Add 10 to 5: {add_10(5)}")  # 15

print("\n=== LAMBDA FUNCTIONS ===")

# Lambda (anonymous) functions
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(f"3 * 4 = {multiply(3, 4)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

print("\n=== EXAM FOCUS: FUNCTION FEATURES ===")

def exam_function(*args, **kwargs):
    """Common exam pattern"""
    print(f"Positional args: {len(args)}")
    print(f"Keyword args: {len(kwargs)}")
    return sum(args) if args else 0

result = exam_function(1, 2, 3, name="test", value=42)
print(f"Result: {result}")

# Function as first-class objects
def say_hello():
    return "Hello!"

# Assign function to variable
greeting_func = say_hello
print(greeting_func())

print("\nFunctions and scope mastered! ✓")