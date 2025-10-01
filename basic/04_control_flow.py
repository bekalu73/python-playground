"""
CONTROL FLOW (if/else, loops, loop-else)
========================================

Key Points:
- if/elif/else statements
- for and while loops
- loop-else clause (runs if loop completes without break)
- break and continue statements
- range() function for loops
"""

print("=== IF/ELIF/ELSE STATEMENTS ===")

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

test_numbers = [5, -3, 0, 10]
for num in test_numbers:
    print(f"{num} is {check_number(num)}")

print("\n=== FOR LOOPS ===")

# Basic for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with range
print("\nCounting with range:")
for i in range(5):  # 0 to 4
    print(f"Count: {i}")

# Range with start, stop, step
print("\nEven numbers from 2 to 10:")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Enumerate for index and value
print("\nWith enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("\n=== WHILE LOOPS ===")

# Basic while loop
count = 0
while count < 3:
    print(f"While count: {count}")
    count += 1

print("\n=== LOOP-ELSE CLAUSE ===")
# This is a unique Python feature!

# Example 1: Loop completes normally
print("Loop that completes:")
for i in range(3):
    print(f"Loop iteration: {i}")
else:
    print("Loop completed normally!")  # This executes

# Example 2: Loop with break
print("\nLoop with break:")
for i in range(5):
    if i == 2:
        print("Breaking the loop!")
        break
    print(f"Loop iteration: {i}")
else:
    print("This won't execute because of break")

# Example 3: Practical use - searching
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found {target}!")
            break
    else:
        print(f"{target} not found in the list")

items = ["apple", "banana", "cherry"]
find_item(items, "banana")  # Found
find_item(items, "grape")   # Not found

print("\n=== BREAK AND CONTINUE ===")

# Continue example
print("Skip even numbers:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")
print()

# Break example
print("\nStop at first negative:")
numbers = [1, 3, -2, 5, 7]
for num in numbers:
    if num < 0:
        print(f"Stopped at {num}")
        break
    print(num, end=" ")
print()

print("\n=== NESTED LOOPS ===")

# Multiplication table
print("3x3 multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()  # New line after each row

print("\n=== EXAM FOCUS: LOOP-ELSE ===")
# This is commonly tested!

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True  # Loop completed without finding divisor

print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 15 prime? {is_prime(15)}")

print("\nControl flow mastered! ✓")