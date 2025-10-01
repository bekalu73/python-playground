"""
MAGIC METHODS (__str__, __add__, __len__)
========================================

Key Points:
- Magic methods (dunder methods) define object behavior
- __str__ and __repr__ for string representation
- __len__ for length operations
- Arithmetic magic methods (__add__, __sub__, etc.)
- Comparison magic methods (__eq__, __lt__, etc.)
- Container magic methods (__getitem__, __setitem__)
"""

print("=== STRING REPRESENTATION METHODS ===")
# Note: __str__ for human-readable output, __repr__ for developer debugging

class Point:
    """Point class demonstrating string representation methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """Human-readable string representation"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer-friendly representation (should be unambiguous)"""
        return f"Point(x={self.x}, y={self.y})"

# Demonstrating __str__ and __repr__
point = Point(3, 4)
print(f"str(point): {str(point)}")      # Calls __str__
print(f"repr(point): {repr(point)}")    # Calls __repr__
print(f"print(point): {point}")         # Calls __str__ by default

# In interactive mode or lists, __repr__ is used
points = [Point(1, 2), Point(3, 4)]
print(f"List of points: {points}")      # Uses __repr__

print("\n=== ARITHMETIC MAGIC METHODS ===")
# Note: Magic methods enable operator overloading - make objects work with +, -, *, etc.

class Vector:
    """Vector class with arithmetic operations"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Addition: v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Subtraction: v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Scalar multiplication: v * scalar"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        """Right multiplication: scalar * v"""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """Division: v / scalar"""
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented
    
    def __neg__(self):
        """Negation: -v"""
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        """Absolute value (magnitude): abs(v)"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Using arithmetic magic methods
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"2 * v1 = {2 * v1}")
print(f"v1 / 2 = {v1 / 2}")
print(f"-v1 = {-v1}")
print(f"abs(v1) = {abs(v1)}")

print("\n=== COMPARISON MAGIC METHODS ===")
# Note: Comparison methods enable sorting and comparison operators like <, >, ==

class Student:
    """Student class with comparison methods"""
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __str__(self):
        return f"Student({self.name}, {self.grade})"
    
    def __eq__(self, other):
        """Equality: student1 == student2"""
        if isinstance(other, Student):
            return self.grade == other.grade
        return NotImplemented
    
    def __lt__(self, other):
        """Less than: student1 < student2"""
        if isinstance(other, Student):
            return self.grade < other.grade
        return NotImplemented
    
    def __le__(self, other):
        """Less than or equal: student1 <= student2"""
        if isinstance(other, Student):
            return self.grade <= other.grade
        return NotImplemented
    
    def __gt__(self, other):
        """Greater than: student1 > student2"""
        if isinstance(other, Student):
            return self.grade > other.grade
        return NotImplemented
    
    def __ge__(self, other):
        """Greater than or equal: student1 >= student2"""
        if isinstance(other, Student):
            return self.grade >= other.grade
        return NotImplemented
    
    def __ne__(self, other):
        """Not equal: student1 != student2"""
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

# Using comparison methods
alice = Student("Alice", 85)
bob = Student("Bob", 92)
charlie = Student("Charlie", 85)

print(f"Alice: {alice}")
print(f"Bob: {bob}")
print(f"Charlie: {charlie}")

print(f"Alice == Charlie: {alice == charlie}")  # Same grade
print(f"Alice < Bob: {alice < bob}")            # Lower grade
print(f"Bob > Alice: {bob > alice}")            # Higher grade
print(f"Alice != Bob: {alice != bob}")          # Different grades

# Sorting works automatically with comparison methods
students = [bob, alice, charlie]
students.sort()
print(f"Sorted students: {students}")

print("\n=== CONTAINER MAGIC METHODS ===")
# Note: Container methods make objects behave like lists/dicts - support indexing, iteration

class CustomList:
    """Custom list-like container"""
    
    def __init__(self):
        self._items = []
    
    def __len__(self):
        """Length: len(custom_list)"""
        return len(self._items)
    
    def __getitem__(self, index):
        """Get item: custom_list[index]"""
        return self._items[index]
    
    def __setitem__(self, index, value):
        """Set item: custom_list[index] = value"""
        self._items[index] = value
    
    def __delitem__(self, index):
        """Delete item: del custom_list[index]"""
        del self._items[index]
    
    def __contains__(self, item):
        """Membership: item in custom_list"""
        return item in self._items
    
    def __iter__(self):
        """Iteration: for item in custom_list"""
        return iter(self._items)
    
    def append(self, item):
        """Add item to end"""
        self._items.append(item)
    
    def __str__(self):
        return f"CustomList({self._items})"

# Using container methods
custom_list = CustomList()
custom_list.append("apple")
custom_list.append("banana")
custom_list.append("cherry")

print(f"Custom list: {custom_list}")
print(f"Length: {len(custom_list)}")
print(f"First item: {custom_list[0]}")
print(f"'banana' in list: {'banana' in custom_list}")

# Iteration works
print("Items in custom list:")
for item in custom_list:
    print(f"  {item}")

# Modify items
custom_list[1] = "blueberry"
print(f"After modification: {custom_list}")

print("\n=== CALLABLE OBJECTS ===")
# Note: __call__ makes objects callable like functions - useful for stateful functions

class Multiplier:
    """Callable object that multiplies by a factor"""
    
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        """Make object callable: multiplier(value)"""
        return value * self.factor
    
    def __str__(self):
        return f"Multiplier(factor={self.factor})"

# Using callable objects
double = Multiplier(2)
triple = Multiplier(3)

print(f"Doubler: {double}")
print(f"double(5) = {double(5)}")
print(f"triple(4) = {triple(4)}")

# Check if object is callable
print(f"Is double callable? {callable(double)}")

print("\n=== CONTEXT MANAGER METHODS ===")
# Note: Context managers work with 'with' statement - __enter__ and __exit__ methods

class FileManager:
    """Custom context manager for file operations"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Enter context: with FileManager(...) as f:"""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit context: automatically called when leaving with block"""
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        
        # Return False to propagate exceptions
        return False

# Using context manager
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
    f.write("\nThis is a test file.")

# File is automatically closed
print("File operations completed")

print("\n=== COMPREHENSIVE EXAMPLE ===")
# Note: Combining multiple magic methods creates powerful, intuitive objects

class Matrix:
    """Matrix class with multiple magic methods"""
    
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data:
            self.data = data
        else:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def __str__(self):
        """String representation"""
        result = []
        for row in self.data:
            result.append("[" + " ".join(f"{x:3}" for x in row) + "]")
        return "\n".join(result)
    
    def __getitem__(self, key):
        """Get item: matrix[row, col] or matrix[row]"""
        if isinstance(key, tuple):
            row, col = key
            return self.data[row][col]
        else:
            return self.data[key]
    
    def __setitem__(self, key, value):
        """Set item: matrix[row, col] = value"""
        if isinstance(key, tuple):
            row, col = key
            self.data[row][col] = value
        else:
            self.data[key] = value
    
    def __add__(self, other):
        """Matrix addition"""
        if not isinstance(other, Matrix):
            return NotImplemented
        
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have same dimensions")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i, j] = self[i, j] + other[i, j]
        
        return result
    
    def __len__(self):
        """Length (number of elements)"""
        return self.rows * self.cols
    
    def __eq__(self, other):
        """Equality comparison"""
        if not isinstance(other, Matrix):
            return False
        
        return (self.rows == other.rows and 
                self.cols == other.cols and 
                self.data == other.data)

# Using the Matrix class
matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
matrix2 = Matrix(2, 2, [[5, 6], [7, 8]])

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

print(f"\nMatrix 1 + Matrix 2:")
result = matrix1 + matrix2
print(result)

print(f"\nMatrix element [0, 1]: {matrix1[0, 1]}")
print(f"Matrix length: {len(matrix1)}")

print("\n=== EXAM FOCUS: COMMON MAGIC METHODS ===")

exam_methods = """
Essential magic methods for exams:

1. String representation:
   __str__(self): Human-readable (print, str())
   __repr__(self): Developer-friendly (repr(), interactive)

2. Arithmetic operations:
   __add__(self, other): +
   __sub__(self, other): -
   __mul__(self, other): *
   __truediv__(self, other): /
   __neg__(self): unary -
   __abs__(self): abs()

3. Comparison operations:
   __eq__(self, other): ==
   __lt__(self, other): <
   __le__(self, other): <=
   __gt__(self, other): >
   __ge__(self, other): >=
   __ne__(self, other): !=

4. Container operations:
   __len__(self): len()
   __getitem__(self, key): obj[key]
   __setitem__(self, key, value): obj[key] = value
   __contains__(self, item): item in obj
   __iter__(self): for item in obj

5. Other useful methods:
   __call__(self, ...): obj()
   __bool__(self): bool(obj), if obj:
"""

print(exam_methods)

# Clean up test file
import os
try:
    os.remove("test.txt")
except:
    pass

print("\nMagic methods mastered! ✓")