"""
OOP FUNDAMENTALS (classes, __init__)
===================================

Key Points:
- Class definition with class keyword
- Constructor method __init__
- Instance variables vs class variables
- Instance methods vs class methods vs static methods
- self parameter
- Creating and using objects
"""

print("=== BASIC CLASS DEFINITION ===")
# Note: Classes are blueprints for objects - define attributes and methods

class Dog:
    """A simple Dog class"""
    
    # Class variable (shared by all instances)
    species = "Canis lupus"
    
    def __init__(self, name, age, breed):
        """Constructor method - called when creating new instance"""
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self.breed = breed
        self.is_sleeping = False
    
    def bark(self):
        """Instance method - operates on instance data"""
        return f"{self.name} says Woof!"
    
    def sleep(self):
        """Change instance state"""
        self.is_sleeping = True
        return f"{self.name} is now sleeping"
    
    def wake_up(self):
        """Change instance state"""
        self.is_sleeping = False
        return f"{self.name} is now awake"

# Creating instances (objects)
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "German Shepherd")

print(f"Dog 1: {dog1.name}, {dog1.age} years old, {dog1.breed}")
print(f"Dog 2: {dog2.name}, {dog2.age} years old, {dog2.breed}")
print(f"Both dogs are {Dog.species}")

# Calling methods
print(dog1.bark())
print(dog1.sleep())
print(dog2.bark())

print("\n=== INSTANCE VS CLASS VARIABLES ===")
# Note: Instance variables are unique per object, class variables are shared by all instances

class Counter:
    """Demonstrates instance vs class variables"""
    
    # Class variable - shared by all instances
    total_counters = 0
    
    def __init__(self, name):
        # Instance variable - unique to each instance
        self.name = name
        self.count = 0
        
        # Modify class variable
        Counter.total_counters += 1
    
    def increment(self):
        """Increment this counter's count"""
        self.count += 1
    
    def get_info(self):
        """Get counter information"""
        return f"{self.name}: {self.count} (Total counters: {Counter.total_counters})"

# Create multiple counters
counter1 = Counter("Counter A")
counter2 = Counter("Counter B")
counter3 = Counter("Counter C")

counter1.increment()
counter1.increment()
counter2.increment()

print(counter1.get_info())  # Counter A: 2 (Total counters: 3)
print(counter2.get_info())  # Counter B: 1 (Total counters: 3)
print(counter3.get_info())  # Counter C: 0 (Total counters: 3)

print("\n=== METHODS TYPES ===")
# Note: Instance methods need 'self', class methods use 'cls', static methods are independent

class MathUtils:
    """Demonstrates different types of methods"""
    
    pi = 3.14159  # Class variable
    
    def __init__(self, precision=2):
        """Instance method - requires instance"""
        self.precision = precision
    
    def round_number(self, number):
        """Instance method - uses instance data"""
        return round(number, self.precision)
    
    @classmethod
    def get_pi(cls):
        """Class method - operates on class, not instance"""
        return cls.pi
    
    @staticmethod
    def add_numbers(a, b):
        """Static method - independent utility function"""
        return a + b

# Using different method types
math_util = MathUtils(3)

# Instance method
print(f"Rounded: {math_util.round_number(3.14159)}")

# Class method (can call on class or instance)
print(f"Pi from class: {MathUtils.get_pi()}")
print(f"Pi from instance: {math_util.get_pi()}")

# Static method (can call on class or instance)
print(f"Add numbers: {MathUtils.add_numbers(5, 3)}")
print(f"Add numbers: {math_util.add_numbers(5, 3)}")

print("\n=== PRACTICAL EXAMPLE: BANK ACCOUNT ===")
# Note: Real-world classes combine data (attributes) and behavior (methods) logically

class BankAccount:
    """A practical bank account class"""
    
    # Class variable to track all accounts
    total_accounts = 0
    bank_name = "Python Bank"
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize a new bank account"""
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        
        # Generate account number
        BankAccount.total_accounts += 1
        self.account_number = f"ACC{BankAccount.total_accounts:04d}"
        
        # Record initial deposit if any
        if initial_balance > 0:
            self.transaction_history.append(f"Initial deposit: ${initial_balance}")
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount <= 0:
            return "Deposit amount must be positive"
        
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= 0:
            return "Withdrawal amount must be positive"
        
        if amount > self.balance:
            return "Insufficient funds"
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount}")
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def get_balance(self):
        """Get current balance"""
        return self.balance
    
    def get_statement(self):
        """Get account statement"""
        statement = f"\n--- {BankAccount.bank_name} Statement ---"
        statement += f"\nAccount: {self.account_number}"
        statement += f"\nHolder: {self.account_holder}"
        statement += f"\nCurrent Balance: ${self.balance}"
        statement += f"\n\nTransaction History:"
        
        for transaction in self.transaction_history:
            statement += f"\n  {transaction}"
        
        return statement
    
    @classmethod
    def get_total_accounts(cls):
        """Get total number of accounts created"""
        return cls.total_accounts
    
    @staticmethod
    def calculate_interest(principal, rate, time):
        """Calculate simple interest"""
        return principal * rate * time

# Using the BankAccount class
print(f"Total accounts before: {BankAccount.get_total_accounts()}")

# Create accounts
alice_account = BankAccount("Alice Johnson", 1000)
bob_account = BankAccount("Bob Smith", 500)

print(f"Total accounts after: {BankAccount.get_total_accounts()}")

# Perform transactions
print(alice_account.deposit(250))
print(alice_account.withdraw(100))
print(bob_account.deposit(300))

# Get statements
print(alice_account.get_statement())
print(bob_account.get_statement())

# Use static method
interest = BankAccount.calculate_interest(1000, 0.05, 2)
print(f"\nInterest calculation: ${interest}")

print("\n=== OBJECT IDENTITY AND EQUALITY ===")
# Note: 'is' checks if same object in memory, '==' checks if values are equal

class Person:
    """Simple person class for identity demonstration"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """String representation"""
        return f"Person(name='{self.name}', age={self.age})"

# Create person objects
person1 = Person("Alice", 25)
person2 = Person("Alice", 25)
person3 = person1  # Same object reference

print(f"person1: {person1}")
print(f"person2: {person2}")
print(f"person3: {person3}")

# Identity checks
print(f"person1 is person2: {person1 is person2}")  # False - different objects
print(f"person1 is person3: {person1 is person3}")  # True - same object

# Object IDs
print(f"person1 id: {id(person1)}")
print(f"person2 id: {id(person2)}")
print(f"person3 id: {id(person3)}")

print("\n=== EXAM FOCUS: KEY CONCEPTS ===")

exam_concepts = """
Essential OOP concepts for exams:

1. __init__ method:
   - Constructor method
   - Called automatically when creating instance
   - Must have 'self' as first parameter

2. self parameter:
   - Refers to the instance being operated on
   - Must be first parameter in instance methods
   - Used to access instance variables and methods

3. Instance vs Class variables:
   - Instance variables: unique to each object (self.variable)
   - Class variables: shared by all instances (ClassName.variable)

4. Method types:
   - Instance methods: operate on instance data (def method(self):)
   - Class methods: operate on class (@classmethod, def method(cls):)
   - Static methods: utility functions (@staticmethod, def method():)

5. Object creation:
   - obj = ClassName(arguments)
   - Calls __init__ automatically
"""

print(exam_concepts)

# Quick exam-style example
class Student:
    school_name = "Python Academy"  # Class variable
    
    def __init__(self, name, grade):
        self.name = name            # Instance variable
        self.grade = grade          # Instance variable
    
    def study(self, subject):
        return f"{self.name} is studying {subject}"

# Test the class
student = Student("Emma", "A")
print(f"Student: {student.name}, Grade: {student.grade}")
print(f"School: {Student.school_name}")
print(student.study("Python"))

print("\nOOP Fundamentals mastered! ✓")