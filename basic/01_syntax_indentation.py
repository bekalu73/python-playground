"""
PYTHON SYNTAX & INDENTATION
============================

Key Points:
- Python uses indentation (4 spaces) to define code blocks
- No curly braces {} like other languages
- Consistent indentation is mandatory
- IndentationError occurs with inconsistent spacing
"""

# ✅ CORRECT INDENTATION
if True:
    print("Correctly indented")
    if 5 > 3:
        print("Nested indentation")
        
# ❌ INCORRECT - Would cause IndentationError
# if True:
# print("Missing indentation")

# PRACTICAL EXAMPLES
def check_grade(score):
    if score >= 90:
        print("A grade")
    elif score >= 80:
        print("B grade")
    else:
        print("Need improvement")

# Function calls
check_grade(95)
check_grade(75)

# LOOPS WITH PROPER INDENTATION
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# EXAM TIP: Always use 4 spaces, not tabs
print("Syntax and indentation mastered! ✓")