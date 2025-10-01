"""
OOP PRINCIPLES (inheritance, encapsulation)
==========================================

Key Points:
- Inheritance: creating classes based on existing classes
- Method overriding and super()
- Encapsulation: data hiding with private/protected attributes
- Polymorphism: same interface, different implementations
- Multiple inheritance and Method Resolution Order (MRO)
"""

print("=== INHERITANCE BASICS ===")
# Note: Inheritance allows classes to inherit attributes and methods from parent classes

# Base class (Parent class)
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
    def make_sound(self):
        return f"{self.name} makes a sound"

# Derived class (Child class)
class Dog(Animal):
    """Dog class inherits from Animal"""
    
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Canine")
        self.breed = breed
    
    def make_sound(self):  # Method overriding
        return f"{self.name} barks: Woof!"
    
    def fetch(self):  # New method specific to Dog
        return f"{self.name} fetches the ball"

class Cat(Animal):
    """Cat class inherits from Animal"""
    
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color
    
    def make_sound(self):  # Method overriding
        return f"{self.name} meows: Meow!"
    
    def climb(self):  # New method specific to Cat
        return f"{self.name} climbs the tree"

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(f"Dog: {dog.name}, Species: {dog.species}, Breed: {dog.breed}")
print(f"Cat: {cat.name}, Species: {cat.species}, Color: {cat.color}")

# Inherited methods
print(dog.eat())
print(cat.sleep())

# Overridden methods
print(dog.make_sound())
print(cat.make_sound())

# Specific methods
print(dog.fetch())
print(cat.climb())

print("\n=== ENCAPSULATION ===")
# Note: Encapsulation hides internal data - use _ for protected, __ for private attributes

class BankAccount:
    """Demonstrates encapsulation with private attributes"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number  # Public
        self._balance = initial_balance       # Protected (convention)
        self.__pin = "1234"                  # Private (name mangling)
        self.__transaction_count = 0         # Private
    
    # Public method to access private data
    def get_balance(self):
        """Get account balance (controlled access)"""
        return self._balance
    
    def deposit(self, amount):
        """Deposit money with validation"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self.__transaction_count += 1
        return f"Deposited ${amount}. New balance: ${self._balance}"
    
    def withdraw(self, amount, pin):
        """Withdraw money with PIN validation"""
        if pin != self.__pin:
            return "Invalid PIN"
        
        if amount <= 0:
            return "Withdrawal amount must be positive"
        
        if amount > self._balance:
            return "Insufficient funds"
        
        self._balance -= amount
        self.__transaction_count += 1
        return f"Withdrew ${amount}. New balance: ${self._balance}"
    
    def change_pin(self, old_pin, new_pin):
        """Change PIN with validation"""
        if old_pin != self.__pin:
            return "Invalid current PIN"
        
        self.__pin = new_pin
        return "PIN changed successfully"
    
    def get_transaction_count(self):
        """Get number of transactions (controlled access)"""
        return self.__transaction_count

# Demonstrating encapsulation
account = BankAccount("12345", 1000)

print(f"Account number: {account.account_number}")  # Public access
print(f"Balance: ${account.get_balance()}")         # Controlled access

# These work fine
print(account.deposit(500))
print(account.withdraw(200, "1234"))

# Direct access to protected/private attributes
print(f"Protected balance: {account._balance}")     # Works but not recommended

# Private attributes are name-mangled
try:
    print(account.__pin)  # This will cause AttributeError
except AttributeError:
    print("Cannot access private __pin directly")

# But can access through name mangling (not recommended)
print(f"Private PIN (name mangled): {account._BankAccount__pin}")

print("\n=== POLYMORPHISM ===")
# Note: Polymorphism allows different classes to implement the same interface differently

class Shape:
    """Base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Calculate area - to be overridden"""
        raise NotImplementedError("Subclass must implement area method")
    
    def perimeter(self):
        """Calculate perimeter - to be overridden"""
        raise NotImplementedError("Subclass must implement perimeter method")

class Rectangle(Shape):
    """Rectangle implementation"""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle implementation"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    """Triangle implementation"""
    
    def __init__(self, side1, side2, side3):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Polymorphism in action
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(3, 4, 5)
]

print("Polymorphism demonstration:")
for shape in shapes:
    print(f"{shape.name}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

print("\n=== MULTIPLE INHERITANCE ===")
# Note: Multiple inheritance allows inheriting from multiple classes - use mixins for abilities

class Flyable:
    """Mixin class for flying ability"""
    
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    """Mixin class for swimming ability"""
    
    def swim(self):
        return f"{self.name} is swimming"

class Bird(Animal, Flyable):
    """Bird class with multiple inheritance"""
    
    def __init__(self, name, wingspan):
        super().__init__(name, "Avian")
        self.wingspan = wingspan
    
    def make_sound(self):
        return f"{self.name} chirps: Tweet!"

class Duck(Bird, Swimmable):
    """Duck can both fly and swim"""
    
    def __init__(self, name):
        super().__init__(name, 24)  # Average duck wingspan in inches
    
    def make_sound(self):
        return f"{self.name} quacks: Quack!"

# Using multiple inheritance
duck = Duck("Donald")
print(duck.make_sound())  # From Duck/Bird
print(duck.eat())         # From Animal
print(duck.fly())         # From Flyable
print(duck.swim())        # From Swimmable

# Method Resolution Order (MRO)
print(f"Duck MRO: {Duck.__mro__}")

print("\n=== ADVANCED INHERITANCE EXAMPLE ===")
# Note: Real-world inheritance creates hierarchies that model relationships naturally

class Employee:
    """Base employee class"""
    
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def get_info(self):
        return f"Employee: {self.name} (ID: {self.employee_id})"
    
    def calculate_pay(self):
        return self.salary

class Manager(Employee):
    """Manager with bonus"""
    
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id, salary)
        self.bonus = bonus
        self.team = []
    
    def add_team_member(self, employee):
        self.team.append(employee)
    
    def calculate_pay(self):
        return self.salary + self.bonus
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - Manager (Team size: {len(self.team)})"

class Developer(Employee):
    """Developer with overtime"""
    
    def __init__(self, name, employee_id, salary, programming_languages):
        super().__init__(name, employee_id, salary)
        self.programming_languages = programming_languages
        self.overtime_hours = 0
    
    def add_overtime(self, hours):
        self.overtime_hours += hours
    
    def calculate_pay(self):
        overtime_pay = self.overtime_hours * (self.salary / 2080) * 1.5  # 1.5x rate
        return self.salary + overtime_pay
    
    def get_info(self):
        base_info = super().get_info()
        languages = ", ".join(self.programming_languages)
        return f"{base_info} - Developer (Languages: {languages})"

# Using the employee hierarchy
manager = Manager("Alice Johnson", "M001", 80000, 10000)
developer1 = Developer("Bob Smith", "D001", 70000, ["Python", "JavaScript"])
developer2 = Developer("Carol Davis", "D002", 75000, ["Java", "C++"])

# Build team
manager.add_team_member(developer1)
manager.add_team_member(developer2)

# Add overtime
developer1.add_overtime(20)
developer2.add_overtime(15)

# Display information
employees = [manager, developer1, developer2]
for emp in employees:
    print(emp.get_info())
    print(f"  Annual pay: ${emp.calculate_pay():,.2f}")

print("\n=== EXAM FOCUS: KEY CONCEPTS ===")

exam_concepts = """
Essential OOP principles for exams:

1. Inheritance:
   - class Child(Parent): creates inheritance
   - super() calls parent class methods
   - Method overriding: redefine parent methods in child

2. Encapsulation:
   - Public: normal attributes (self.attribute)
   - Protected: single underscore (self._attribute) - convention only
   - Private: double underscore (self.__attribute) - name mangling

3. Polymorphism:
   - Same method name, different implementations
   - Duck typing: "If it walks like a duck and quacks like a duck..."

4. Multiple Inheritance:
   - class Child(Parent1, Parent2):
   - Method Resolution Order (MRO): Child.__mro__
   - Diamond problem and how Python resolves it

5. super() function:
   - Calls parent class methods
   - Important in __init__ methods
   - Follows MRO in multiple inheritance
"""

print(exam_concepts)

print("\nOOP Principles mastered! ✓")