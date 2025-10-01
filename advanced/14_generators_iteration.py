"""
GENERATORS & ITERATION (yield, generator expressions)
====================================================

Key Points:
- Generators create iterators using yield
- Memory efficient - values generated on demand
- Generator expressions (genexps)
- Iterator protocol (__iter__ and __next__)
- yield from for generator delegation
- Practical applications and benefits
"""

print("=== BASIC GENERATORS ===")

def simple_generator():
    """Simple generator that yields three values"""
    print("Starting generator")
    yield 1
    print("After first yield")
    yield 2
    print("After second yield")
    yield 3
    print("Generator finished")

# Using the generator
print("Creating generator:")
gen = simple_generator()
print(f"Generator object: {gen}")

print("\nIterating through generator:")
for value in gen:
    print(f"Received: {value}")

print("\n=== GENERATOR VS REGULAR FUNCTION ===")

def regular_function():
    """Regular function returns all values at once"""
    result = []
    for i in range(5):
        result.append(i ** 2)
    return result

def generator_function():
    """Generator yields values one at a time"""
    for i in range(5):
        yield i ** 2

# Compare memory usage and behavior
print("Regular function:")
regular_result = regular_function()
print(f"Type: {type(regular_result)}")
print(f"Values: {regular_result}")

print("\nGenerator function:")
gen_result = generator_function()
print(f"Type: {type(gen_result)}")
print("Values:", end=" ")
for value in gen_result:
    print(value, end=" ")
print()

print("\n=== PRACTICAL GENERATOR EXAMPLES ===")

def fibonacci_generator(n):
    """Generate Fibonacci numbers up to n"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("Fibonacci sequence (first 10 numbers):")
for num in fibonacci_generator(10):
    print(num, end=" ")
print()

def count_up(start, end):
    """Count from start to end"""
    current = start
    while current <= end:
        yield current
        current += 1

print(f"\nCounting from 5 to 8:")
for num in count_up(5, 8):
    print(num, end=" ")
print()

def file_reader(filename):
    """Generator to read file line by line"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        yield "File not found"

# Create a test file
with open("test_file.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

print("\nReading file with generator:")
for line in file_reader("test_file.txt"):
    print(f"  {line}")

print("\n=== GENERATOR EXPRESSIONS ===")

# Generator expression (similar to list comprehension but with parentheses)
squares_gen = (x**2 for x in range(5))
print(f"Generator expression: {squares_gen}")
print("Squares:", list(squares_gen))

# Generator expression with condition
even_squares = (x**2 for x in range(10) if x % 2 == 0)
print("Even squares:", list(even_squares))

# Memory comparison
import sys

# List comprehension (creates all values in memory)
list_comp = [x**2 for x in range(1000)]
print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")

# Generator expression (creates generator object)
gen_exp = (x**2 for x in range(1000))
print(f"Generator expression size: {sys.getsizeof(gen_exp)} bytes")

print("\n=== ITERATOR PROTOCOL ===")

class CountDown:
    """Custom iterator using iterator protocol"""
    
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        """Return iterator object (self)"""
        return self
    
    def __next__(self):
        """Return next value or raise StopIteration"""
        if self.start <= 0:
            raise StopIteration
        
        self.start -= 1
        return self.start + 1

# Using custom iterator
print("Custom countdown iterator:")
countdown = CountDown(5)
for num in countdown:
    print(num, end=" ")
print()

# Manual iteration
print("\nManual iteration:")
countdown2 = CountDown(3)
iterator = iter(countdown2)
try:
    while True:
        print(next(iterator), end=" ")
except StopIteration:
    print("\nIteration complete")

print("\n=== GENERATOR WITH SEND AND CLOSE ===")

def advanced_generator():
    """Generator that can receive values"""
    print("Generator started")
    value = None
    
    while True:
        received = yield value
        if received is not None:
            print(f"Received: {received}")
            value = received * 2
        else:
            value = "No input"

# Using send method
print("Generator with send:")
gen = advanced_generator()
next(gen)  # Prime the generator

print(gen.send(5))    # Send 5, get 10
print(gen.send(3))    # Send 3, get 6
print(gen.send(None)) # Send None, get "No input"

gen.close()  # Close the generator

print("\n=== YIELD FROM ===")

def sub_generator():
    """Sub-generator"""
    yield "A"
    yield "B"
    yield "C"

def main_generator():
    """Main generator using yield from"""
    yield "Start"
    yield from sub_generator()  # Delegate to sub-generator
    yield from [1, 2, 3]        # Can also yield from iterables
    yield "End"

print("Using yield from:")
for item in main_generator():
    print(item, end=" ")
print()

print("\n=== PRACTICAL APPLICATIONS ===")

def batch_processor(data, batch_size):
    """Process data in batches"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Process large dataset in batches
large_data = list(range(20))
print("Processing data in batches of 5:")
for batch_num, batch in enumerate(batch_processor(large_data, 5), 1):
    print(f"Batch {batch_num}: {batch}")

def infinite_sequence():
    """Generate infinite sequence"""
    num = 0
    while True:
        yield num
        num += 1

# Use infinite generator (be careful!)
print("\nFirst 10 numbers from infinite sequence:")
infinite_gen = infinite_sequence()
for _ in range(10):
    print(next(infinite_gen), end=" ")
print()

def prime_generator():
    """Generate prime numbers"""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

print("\nFirst 10 prime numbers:")
prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen), end=" ")
print()

print("\n=== GENERATOR PIPELINE ===")

def numbers():
    """Generate numbers"""
    for i in range(10):
        yield i

def squares(nums):
    """Square the numbers"""
    for num in nums:
        yield num ** 2

def evens(nums):
    """Filter even numbers"""
    for num in nums:
        if num % 2 == 0:
            yield num

# Chain generators together
print("Generator pipeline (numbers -> squares -> evens):")
pipeline = evens(squares(numbers()))
result = list(pipeline)
print(result)

print("\n=== MEMORY EFFICIENCY DEMONSTRATION ===")

def memory_efficient_processing(filename):
    """Process large file without loading all into memory"""
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, 1):
            # Process line by line
            processed_line = line.strip().upper()
            yield f"Line {line_num}: {processed_line}"

# Create a test file
with open("large_file.txt", "w") as f:
    for i in range(5):
        f.write(f"This is line {i+1}\n")

print("Memory-efficient file processing:")
for processed_line in memory_efficient_processing("large_file.txt"):
    print(processed_line)

print("\n=== EXAM FOCUS: KEY CONCEPTS ===")

exam_concepts = """
Essential generator concepts for exams:

1. Generator function:
   - Uses 'yield' instead of 'return'
   - Returns generator object, not values directly
   - Maintains state between calls

2. Generator expression:
   - (expression for item in iterable)
   - Memory efficient alternative to list comprehension
   - Creates generator object

3. Iterator protocol:
   - __iter__(): returns iterator object
   - __next__(): returns next value or raises StopIteration
   - iter() and next() built-in functions

4. Benefits:
   - Memory efficient (lazy evaluation)
   - Can represent infinite sequences
   - Good for large datasets

5. Methods:
   - next(generator): get next value
   - generator.send(value): send value to generator
   - generator.close(): close generator
   - yield from: delegate to another generator/iterable

6. Common patterns:
   - File processing line by line
   - Infinite sequences
   - Data pipelines
   - Batch processing
"""

print(exam_concepts)

# Quick exam example
def exam_generator(n):
    """Generate squares of numbers from 1 to n"""
    for i in range(1, n + 1):
        yield i ** 2

print(f"\nExam example - squares from 1 to 5:")
squares = exam_generator(5)
print(f"Generator: {squares}")
print(f"Values: {list(squares)}")

# Generator expression example
cubes = (x**3 for x in range(1, 6))
print(f"Cubes: {list(cubes)}")

print("\n=== CLEANUP ===")
import os
try:
    os.remove("test_file.txt")
    os.remove("large_file.txt")
except:
    pass

print("\nGenerators and iteration mastered! ✓")