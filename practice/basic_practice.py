"""
BASIC LEVEL PRACTICE QUESTIONS
==============================

Covers: data types, operators, control flow, functions, strings, lists, dicts, file I/O

Instructions:
- Each question has a description and a function stub for you to implement.
- Run the file to test your solutions automatically.
"""

# ---------------------------------------------------------------------------
# QUESTION 1: DATA TYPES
# ---------------------------------------------------------------------------
"""
Write a function that takes a value and returns its type as a string.
Example: get_type(42) -> "int"
         get_type("hello") -> "str"
"""
def get_type(value):
    return type(value).__name__

# Tests
assert get_type(42) == "int"
assert get_type(3.14) == "float"
assert get_type("hello") == "str"
assert get_type([1, 2]) == "list"
assert get_type(True) == "bool"
assert get_type({"a": 1}) == "dict"
assert get_type(None) == "NoneType"
print("Q1 PASSED: get_type")


# ---------------------------------------------------------------------------
# QUESTION 2: OPERATORS
# ---------------------------------------------------------------------------
"""
Write a function that takes two numbers and returns a dictionary with:
- sum, difference, product, quotient (float), floor_division, remainder, power
Example: calculate(10, 3) -> {"sum": 13, "difference": 7, ...}
"""
def calculate(a, b):
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": a / b,
        "floor_division": a // b,
        "remainder": a % b,
        "power": a ** b,
    }

# Tests
result = calculate(10, 3)
assert result["sum"] == 13
assert result["difference"] == 7
assert result["product"] == 30
assert result["quotient"] == 10 / 3
assert result["floor_division"] == 3
assert result["remainder"] == 1
assert result["power"] == 1000
print("Q2 PASSED: calculate")


# ---------------------------------------------------------------------------
# QUESTION 3: EVEN OR ODD
# ---------------------------------------------------------------------------
"""
Write a function that returns "even" if the number is even, "odd" if odd.
Example: even_or_odd(4) -> "even"
         even_or_odd(7) -> "odd"
"""
def even_or_odd(n):
    return "even" if n % 2 == 0 else "odd"

# Tests
assert even_or_odd(4) == "even"
assert even_or_odd(7) == "odd"
assert even_or_odd(0) == "even"
assert even_or_odd(-3) == "odd"
print("Q3 PASSED: even_or_odd")


# ---------------------------------------------------------------------------
# QUESTION 4: FIZZBUZZ
# ---------------------------------------------------------------------------
"""
Write a function that returns "Fizz" if divisible by 3, "Buzz" if by 5,
"FizzBuzz" if by both, otherwise the number as a string.
Example: fizzbuzz(3) -> "Fizz"
         fizzbuzz(5) -> "Buzz"
         fizzbuzz(15) -> "FizzBuzz"
         fizzbuzz(7) -> "7"
"""
def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

# Tests
assert fizzbuzz(3) == "Fizz"
assert fizzbuzz(5) == "Buzz"
assert fizzbuzz(15) == "FizzBuzz"
assert fizzbuzz(7) == "7"
assert fizzbuzz(30) == "FizzBuzz"
assert fizzbuzz(9) == "Fizz"
assert fizzbuzz(10) == "Buzz"
print("Q4 PASSED: fizzbuzz")


# ---------------------------------------------------------------------------
# QUESTION 5: FACTORIAL (LOOP)
# ---------------------------------------------------------------------------
"""
Write a function that returns the factorial of n using a loop.
Example: factorial(5) -> 120
"""
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Tests
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(7) == 5040
print("Q5 PASSED: factorial")


# ---------------------------------------------------------------------------
# QUESTION 6: COUNT VOWELS
# ---------------------------------------------------------------------------
"""
Write a function that counts vowels (a, e, i, o, u) in a string (case-insensitive).
Example: count_vowels("Hello World") -> 3
"""
def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

# Tests
assert count_vowels("Hello World") == 3
assert count_vowels("Python") == 1
assert count_vowels("AEIOU") == 5
assert count_vowels("xyz") == 0
assert count_vowels("") == 0
print("Q6 PASSED: count_vowels")


# ---------------------------------------------------------------------------
# QUESTION 7: REVERSE STRING
# ---------------------------------------------------------------------------
"""
Write a function that reverses a string.
Example: reverse_string("python") -> "nohtyp"
"""
def reverse_string(s):
    return s[::-1]

# Tests
assert reverse_string("python") == "nohtyp"
assert reverse_string("hello") == "olleh"
assert reverse_string("a") == "a"
assert reverse_string("") == ""
assert reverse_string("racecar") == "racecar"
print("Q7 PASSED: reverse_string")


# ---------------------------------------------------------------------------
# QUESTION 8: PALINDROME CHECK
# ---------------------------------------------------------------------------
"""
Write a function that checks if a string is a palindrome (case-insensitive).
Example: is_palindrome("Racecar") -> True
         is_palindrome("hello") -> False
"""
def is_palindrome(s):
    cleaned = s.lower()
    return cleaned == cleaned[::-1]

# Tests
assert is_palindrome("Racecar") is True
assert is_palindrome("hello") is False
assert is_palindrome("madam") is True
assert is_palindrome("") is True
assert is_palindrome("A man a plan a canal Panama".replace(" ", "")) is True
print("Q8 PASSED: is_palindrome")


# ---------------------------------------------------------------------------
# QUESTION 9: LIST OPERATIONS
# ---------------------------------------------------------------------------
"""
Write a function that takes a list of numbers and returns a dictionary with:
- "min": minimum value
- "max": maximum value
- "sum": sum of all numbers
- "average": average (float)
- "length": number of elements
- "sorted": sorted copy of the list
Example: analyze_numbers([3, 1, 4, 1, 5])
"""
def analyze_numbers(numbers):
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "length": len(numbers),
        "sorted": sorted(numbers),
    }

# Tests
result = analyze_numbers([3, 1, 4, 1, 5])
assert result["min"] == 1
assert result["max"] == 5
assert result["sum"] == 14
assert result["average"] == 2.8
assert result["length"] == 5
assert result["sorted"] == [1, 1, 3, 4, 5]
print("Q9 PASSED: analyze_numbers")


# ---------------------------------------------------------------------------
# QUESTION 10: LIST COMPREHENSION - SQUARES
# ---------------------------------------------------------------------------
"""
Write a function that returns a list of squares for numbers 1 through n.
Example: squares(5) -> [1, 4, 9, 16, 25]
"""
def squares(n):
    return [i**2 for i in range(1, n + 1)]

# Tests
assert squares(5) == [1, 4, 9, 16, 25]
assert squares(1) == [1]
assert squares(0) == []
assert squares(3) == [1, 4, 9]
print("Q10 PASSED: squares")


# ---------------------------------------------------------------------------
# QUESTION 11: LIST COMPREHENSION - FILTER EVENS
# ---------------------------------------------------------------------------
"""
Write a function that filters out only the even numbers from a list.
Example: filter_evens([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
"""
def filter_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

# Tests
assert filter_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
assert filter_evens([1, 3, 5]) == []
assert filter_evens([]) == []
assert filter_evens([2, 4, 6]) == [2, 4, 6]
print("Q11 PASSED: filter_evens")


# ---------------------------------------------------------------------------
# QUESTION 12: DICTIONARY OPERATIONS
# ---------------------------------------------------------------------------
"""
Write a function that takes two lists (keys and values) and returns a dictionary.
If the lists differ in length, ignore extra elements from the longer list.
Example: lists_to_dict(["a", "b", "c"], [1, 2, 3]) -> {"a": 1, "b": 2, "c": 3}
"""
def lists_to_dict(keys, values):
    return {keys[i]: values[i] for i in range(min(len(keys), len(values)))}

# Tests
assert lists_to_dict(["a", "b", "c"], [1, 2, 3]) == {"a": 1, "b": 2, "c": 3}
assert lists_to_dict(["x", "y"], [10, 20, 30]) == {"x": 10, "y": 20}
assert lists_to_dict([], []) == {}
assert lists_to_dict(["a"], [1]) == {"a": 1}
print("Q12 PASSED: lists_to_dict")


# ---------------------------------------------------------------------------
# QUESTION 13: WORD FREQUENCY
# ---------------------------------------------------------------------------
"""
Write a function that counts word frequency in a sentence.
Example: word_frequency("the cat and the dog") -> {"the": 2, "cat": 1, "and": 1, "dog": 1}
"""
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Tests
assert word_frequency("the cat and the dog") == {"the": 2, "cat": 1, "and": 1, "dog": 1}
assert word_frequency("hello world") == {"hello": 1, "world": 1}
assert word_frequency("") == {}
print("Q13 PASSED: word_frequency")


# ---------------------------------------------------------------------------
# QUESTION 14: TEMPERATURE CONVERSION
# ---------------------------------------------------------------------------
"""
Write functions to convert between Celsius and Fahrenheit.
- celsius_to_fahrenheit(c) -> (c * 9/5) + 32
- fahrenheit_to_celsius(f) -> (f - 32) * 5/9
"""
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Tests
assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
assert round(fahrenheit_to_celsius(32), 1) == 0.0
assert round(fahrenheit_to_celsius(212), 1) == 100.0
assert celsius_to_fahrenheit(-40) == -40
print("Q14 PASSED: temperature conversion")


# ---------------------------------------------------------------------------
# QUESTION 15: PRIME CHECK
# ---------------------------------------------------------------------------
"""
Write a function that returns True if n is prime, False otherwise.
Example: is_prime(7) -> True
         is_prime(10) -> False
"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tests
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(7) is True
assert is_prime(10) is False
assert is_prime(1) is False
assert is_prime(0) is False
assert is_prime(97) is True
print("Q15 PASSED: is_prime")


# ---------------------------------------------------------------------------
# QUESTION 16: FIND MAX WITHOUT BUILT-IN
# ---------------------------------------------------------------------------
"""
Write a function that finds the maximum value in a list without using max().
Example: find_max([3, 7, 2, 9, 1]) -> 9
"""
def find_max(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum

# Tests
assert find_max([3, 7, 2, 9, 1]) == 9
assert find_max([-5, -2, -10]) == -2
assert find_max([42]) == 42
assert find_max([]) is None
print("Q16 PASSED: find_max")


# ---------------------------------------------------------------------------
# QUESTION 17: REMOVE DUPLICATES
# ---------------------------------------------------------------------------
"""
Write a function that removes duplicates from a list while preserving order.
Example: remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
"""
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Tests
assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
assert remove_duplicates([]) == []
assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]
print("Q17 PASSED: remove_duplicates")


# ---------------------------------------------------------------------------
# QUESTION 18: STRING FORMATTING
# ---------------------------------------------------------------------------
"""
Write a function that takes a name, age, and city, and returns a formatted string:
"My name is {name}, I am {age} years old, and I live in {city}."
Use f-strings.
"""
def introduce(name, age, city):
    return f"My name is {name}, I am {age} years old, and I live in {city}."

# Tests
assert introduce("Alice", 25, "New York") == "My name is Alice, I am 25 years old, and I live in New York."
assert introduce("Bob", 30, "London") == "My name is Bob, I am 30 years old, and I live in London."
print("Q18 PASSED: introduce")


# ---------------------------------------------------------------------------
# QUESTION 19: NESTED LOOP - MULTIPLICATION TABLE
# ---------------------------------------------------------------------------
"""
Write a function that returns an n x n multiplication table as a list of lists.
Example: multiplication_table(3) -> [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
"""
def multiplication_table(n):
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

# Tests
assert multiplication_table(1) == [[1]]
assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
table_4 = multiplication_table(4)
assert table_4[0] == [1, 2, 3, 4]
assert table_4[3] == [4, 8, 12, 16]
print("Q19 PASSED: multiplication_table")


# ---------------------------------------------------------------------------
# QUESTION 20: ANAGRAM CHECK
# ---------------------------------------------------------------------------
"""
Write a function that checks if two strings are anagrams (same letters, different order).
Example: are_anagrams("listen", "silent") -> True
         are_anagrams("hello", "world") -> False
"""
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

# Tests
assert are_anagrams("listen", "silent") is True
assert are_anagrams("hello", "world") is False
assert are_anagrams("Dormitory", "Dirtyroom") is True
assert are_anagrams("abc", "abcd") is False
assert are_anagrams("", "") is True
print("Q20 PASSED: are_anagrams")


# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------
print()
print("=" * 50)
print("ALL BASIC PRACTICE QUESTIONS PASSED!")
print("=" * 50)
print()
print("Topics covered:")
print("  - Data types & type checking")
print("  - Arithmetic operators")
print("  - Conditionals (if/else)")
print("  - Loops (for, while)")
print("  - String manipulation")
print("  - List operations & comprehensions")
print("  - Dictionary operations")
print("  - Nested loops")
print("  - Functions")
print("  - F-strings")
