"""
PYTHON EXAM PRACTICE QUESTIONS
==============================

This file contains solutions to the practice questions from the roadmap:
1. Function that sums arbitrary list of numbers using *args
2. List comprehension to convert lowercase to uppercase
3. File I/O: filter lines containing "ERROR" 
4. BankAccount class with deposit, withdraw, and __repr__
5. Generator for Fibonacci numbers up to 100
6. Extract email addresses using re.findall
7. Async function for concurrent URL fetching
"""

import re
import asyncio
import random

print("=== PRACTICE QUESTION 1: *ARGS FUNCTION ===")
print("Write a function that sums an arbitrary list of numbers using *args.")
# Note: *args collects variable positional arguments into a tuple

def sum_numbers(*args):
    """Sum any number of arguments"""
    return sum(args)

# Alternative with type checking
def sum_numbers_safe(*args):
    """Sum numbers with type checking"""
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(f"Warning: {num} is not a number, skipping")
    return total

# Test the functions
print(f"sum_numbers(1, 2, 3, 4, 5) = {sum_numbers(1, 2, 3, 4, 5)}")
print(f"sum_numbers(10, 20) = {sum_numbers(10, 20)}")
print(f"sum_numbers() = {sum_numbers()}")  # Empty args
print(f"sum_numbers_safe(1, 2, 'hello', 3) = {sum_numbers_safe(1, 2, 'hello', 3)}")

print("\n" + "="*60)
print("=== PRACTICE QUESTION 2: LIST COMPREHENSION ===")
print('Given data = ["a","b","c"], produce ["A","B","C"] with a comprehension.')
# Note: List comprehensions are concise way to transform lists

data = ["a", "b", "c"]
uppercase_data = [letter.upper() for letter in data]

print(f"Original: {data}")
print(f"Uppercase: {uppercase_data}")

# Alternative methods
uppercase_data2 = [item.upper() for item in data]
uppercase_data3 = list(map(str.upper, data))

print(f"Method 2: {uppercase_data2}")
print(f"Method 3 (map): {uppercase_data3}")

print("\n" + "="*60)
print("=== PRACTICE QUESTION 3: FILE I/O ===")
print('Read log.txt, filter lines containing "ERROR", and write them to errors.log.')
# Note: Use context managers for safe file operations

# Create sample log file
log_content = """2024-01-01 10:00:00 INFO Application started
2024-01-01 10:05:00 ERROR Database connection failed
2024-01-01 10:06:00 INFO Retrying database connection
2024-01-01 10:07:00 ERROR Authentication failed for user john
2024-01-01 10:10:00 INFO User logged in successfully
2024-01-01 10:15:00 ERROR File not found: config.xml
2024-01-01 10:20:00 INFO Processing completed"""

# Write sample log file
with open("log.txt", "w") as f:
    f.write(log_content)

# Solution
def filter_error_logs(input_file, output_file):
    """Filter ERROR lines from log file"""
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            error_lines = []
            for line in infile:
                if "ERROR" in line:
                    error_lines.append(line)
                    outfile.write(line)
            return len(error_lines)
    except FileNotFoundError:
        print(f"File {input_file} not found")
        return 0

# Execute the solution
error_count = filter_error_logs("log.txt", "errors.log")
print(f"Found and wrote {error_count} error lines to errors.log")

# Display the results
print("\nError lines found:")
with open("errors.log", "r") as f:
    for line in f:
        print(f"  {line.strip()}")

print("\n" + "="*60)
print("=== PRACTICE QUESTION 4: BANKACCOUNT CLASS ===")
print("Define a BankAccount class with deposit, withdraw, and a __repr__ that recreates the object.")
# Note: __repr__ should return a string that can recreate the object

class BankAccount:
    """Bank account with deposit, withdraw, and proper representation"""
    
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount}")
        return self.balance
    
    def __repr__(self):
        """Return string that can recreate the object"""
        return f"BankAccount('{self.account_holder}', {self.balance})"
    
    def __str__(self):
        """Human-readable string representation"""
        return f"BankAccount for {self.account_holder}: ${self.balance:.2f}"

# Test the BankAccount class
account = BankAccount("Alice Johnson", 1000.0)
print(f"Created account: {account}")
print(f"repr(account): {repr(account)}")

# Test deposit and withdraw
print(f"After deposit of $500: ${account.deposit(500)}")
print(f"After withdrawal of $200: ${account.withdraw(200)}")
print(f"Final account: {account}")

# Test that repr can recreate object
account_copy = eval(repr(account))  # Note: eval is dangerous in real code
print(f"Recreated account: {account_copy}")

print("\n" + "="*60)
print("=== PRACTICE QUESTION 5: FIBONACCI GENERATOR ===")
print("Create a generator for Fibonacci numbers up to 100.")
# Note: Generators use yield to produce values on-demand

def fibonacci_generator(max_value):
    """Generate Fibonacci numbers up to max_value"""
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b

# Test the generator
print("Fibonacci numbers up to 100:")
fib_numbers = list(fibonacci_generator(100))
print(fib_numbers)

# Alternative: Generator that yields n Fibonacci numbers
def fibonacci_n_numbers(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print(f"\nFirst 10 Fibonacci numbers:")
first_10_fib = list(fibonacci_n_numbers(10))
print(first_10_fib)

# Using the generator in a loop
print("\nFibonacci numbers up to 50 (using generator):")
for num in fibonacci_generator(50):
    print(num, end=" ")
print()

print("\n" + "="*60)
print("=== PRACTICE QUESTION 6: REGULAR EXPRESSIONS ===")
print("Extract all email addresses from a multi-line string using re.findall.")
# Note: Regular expressions find patterns in text using special syntax

# Sample multi-line text with emails
email_text = """
Contact Information:
For support, email us at support@example.com
Sales inquiries: sales@company.org
Technical issues: tech.support@domain.co.uk
Invalid email: not-an-email
Another contact: info@test-site.net
Personal: john.doe+tag@gmail.com
"""

def extract_emails(text):
    """Extract email addresses from text using regex"""
    # Email pattern: word characters, dots, hyphens, plus signs @ domain . extension
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

# Alternative simpler pattern (from roadmap example)
def extract_emails_simple(text):
    """Extract emails using simpler pattern"""
    email_pattern = r'\S+@\S+\.\S+'
    return re.findall(email_pattern, text)

# Test both methods
emails_complex = extract_emails(email_text)
emails_simple = extract_emails_simple(email_text)

print("Email addresses found (complex pattern):")
for email in emails_complex:
    print(f"  {email}")

print("\nEmail addresses found (simple pattern):")
for email in emails_simple:
    print(f"  {email}")

# Validate extracted emails
def validate_email(email):
    """Basic email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

print("\nEmail validation:")
for email in emails_complex:
    is_valid = validate_email(email)
    print(f"  {email:30} - {'Valid' if is_valid else 'Invalid'}")

print("\n" + "="*60)
print("=== PRACTICE QUESTION 7: ASYNC FUNCTION ===")
print("Write an async function that concurrently fetches (mock) URLs and awaits their completion.")
# Note: Async functions enable concurrent execution of I/O operations

async def fetch_url(url, delay=None):
    """Mock URL fetching with random delay"""
    if delay is None:
        delay = random.uniform(0.5, 2.0)
    
    print(f"Starting to fetch: {url}")
    await asyncio.sleep(delay)  # Simulate network request
    
    # Simulate different response scenarios
    if "error" in url.lower():
        raise Exception(f"Failed to fetch {url}")
    
    response_size = random.randint(1000, 10000)
    print(f"Completed fetching: {url} ({response_size} bytes)")
    
    return {
        "url": url,
        "status": "success",
        "size": response_size,
        "delay": delay
    }

async def fetch_multiple_urls(urls):
    """Fetch multiple URLs concurrently"""
    print(f"Fetching {len(urls)} URLs concurrently...")
    start_time = asyncio.get_event_loop().time()
    
    # Create tasks for all URLs
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    
    # Wait for all tasks to complete (with error handling)
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    end_time = asyncio.get_event_loop().time()
    total_time = end_time - start_time
    
    # Process results
    successful = []
    failed = []
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            failed.append({"url": urls[i], "error": str(result)})
        else:
            successful.append(result)
    
    return {
        "successful": successful,
        "failed": failed,
        "total_time": total_time,
        "total_urls": len(urls)
    }

async def async_demo():
    """Demonstrate async URL fetching"""
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/posts", 
        "https://api.example.com/error",  # This will fail
        "https://api.example.com/comments",
        "https://api.example.com/photos"
    ]
    
    results = await fetch_multiple_urls(urls)
    
    print(f"\n--- RESULTS ---")
    print(f"Total time: {results['total_time']:.2f} seconds")
    print(f"Successful: {len(results['successful'])}")
    print(f"Failed: {len(results['failed'])}")
    
    print("\nSuccessful fetches:")
    for result in results['successful']:
        print(f"  {result['url']} - {result['size']} bytes in {result['delay']:.2f}s")
    
    print("\nFailed fetches:")
    for failure in results['failed']:
        print(f"  {failure['url']} - {failure['error']}")

# Run the async demo
print("Running async URL fetching demo:")
asyncio.run(async_demo())

print("\n" + "="*60)
print("=== BONUS: COMPREHENSIVE EXAMPLE ===")
print("Combining multiple concepts in one example")
# Note: Real projects combine multiple Python concepts together

class DataProcessor:
    """Class that combines multiple Python concepts"""
    
    def __init__(self, name):
        self.name = name
        self.processed_count = 0
    
    def process_numbers(self, *numbers):
        """Process numbers using *args"""
        valid_numbers = [n for n in numbers if isinstance(n, (int, float))]
        self.processed_count += len(valid_numbers)
        return sum(valid_numbers)
    
    def process_text_data(self, text):
        """Extract and process text data"""
        # Extract emails
        emails = re.findall(r'\S+@\S+\.\S+', text)
        
        # Extract numbers
        numbers = [float(match) for match in re.findall(r'-?\d+\.?\d*', text)]
        
        return {
            "emails": emails,
            "numbers": numbers,
            "total": sum(numbers) if numbers else 0
        }
    
    def fibonacci_up_to(self, max_val):
        """Generate Fibonacci numbers using generator"""
        a, b = 0, 1
        while a <= max_val:
            yield a
            a, b = b, a + b
    
    async def async_process(self, data_list):
        """Process data asynchronously"""
        async def process_item(item):
            await asyncio.sleep(0.1)  # Simulate processing time
            return item.upper() if isinstance(item, str) else item * 2
        
        tasks = [asyncio.create_task(process_item(item)) for item in data_list]
        return await asyncio.gather(*tasks)
    
    def __repr__(self):
        return f"DataProcessor('{self.name}', processed={self.processed_count})"

# Test the comprehensive example
async def comprehensive_demo():
    processor = DataProcessor("ExamProcessor")
    
    # Test *args function
    total = processor.process_numbers(1, 2, 3, "invalid", 4.5)
    print(f"Sum of numbers: {total}")
    
    # Test text processing with regex
    sample_text = "Contact: admin@test.com, sales@company.org. Values: 10.5, 20, -5.2"
    text_result = processor.process_text_data(sample_text)
    print(f"Text processing result: {text_result}")
    
    # Test generator
    fib_numbers = list(processor.fibonacci_up_to(20))
    print(f"Fibonacci up to 20: {fib_numbers}")
    
    # Test async processing
    data = ["hello", "world", 5, 10]
    async_result = await processor.async_process(data)
    print(f"Async processing result: {async_result}")
    
    print(f"Final processor state: {processor}")

# Run comprehensive demo
print("Running comprehensive demo:")
asyncio.run(comprehensive_demo())

print("\n=== CLEANUP ===")
import os
try:
    os.remove("log.txt")
    os.remove("errors.log")
    print("✓ Cleaned up temporary files")
except:
    pass

print("\n" + "="*60)
print("🎉 ALL PRACTICE QUESTIONS COMPLETED! 🎉")
print("You've successfully implemented:")
print("✓ Functions with *args")
print("✓ List comprehensions")
print("✓ File I/O operations")
print("✓ Object-oriented programming")
print("✓ Generators")
print("✓ Regular expressions")
print("✓ Asynchronous programming")
print("\nYou're ready for your Python exam! 🐍")