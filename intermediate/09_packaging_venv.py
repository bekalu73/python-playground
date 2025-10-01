"""
PACKAGING (pip, virtual environments)
====================================

Key Points:
- Virtual environments with venv
- Installing packages with pip
- requirements.txt file
- Package management best practices
- Creating and distributing packages
"""

import subprocess
import sys
import os

print("=== VIRTUAL ENVIRONMENTS ===")

print("""
Virtual Environment Commands:

1. Create virtual environment:
   python -m venv myenv

2. Activate virtual environment:
   Windows: myenv\\Scripts\\activate
   macOS/Linux: source myenv/bin/activate

3. Deactivate:
   deactivate

4. Remove virtual environment:
   Simply delete the folder
""")

# Check if we're in a virtual environment
def check_virtual_env():
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        return True
    return False

print(f"Currently in virtual environment: {check_virtual_env()}")
print(f"Python executable: {sys.executable}")
print(f"Python path: {sys.path[0]}")

print("\n=== PIP PACKAGE MANAGEMENT ===")

print("""
Common pip commands:

1. Install package:
   pip install package_name
   pip install package_name==1.2.3  # specific version
   pip install package_name>=1.2.0  # minimum version

2. Install from requirements:
   pip install -r requirements.txt

3. List installed packages:
   pip list
   pip freeze  # for requirements.txt format

4. Show package info:
   pip show package_name

5. Uninstall package:
   pip uninstall package_name

6. Upgrade package:
   pip install --upgrade package_name

7. Search packages:
   pip search package_name  # deprecated in newer versions
""")

# Demonstrate pip freeze (show current packages)
try:
    result = subprocess.run([sys.executable, "-m", "pip", "freeze"], 
                          capture_output=True, text=True)
    print("Currently installed packages:")
    if result.stdout:
        for line in result.stdout.split('\n')[:10]:  # Show first 10
            if line.strip():
                print(f"  {line}")
        if len(result.stdout.split('\n')) > 10:
            print("  ... (and more)")
    else:
        print("  No packages installed or pip not available")
except Exception as e:
    print(f"Could not run pip freeze: {e}")

print("\n=== REQUIREMENTS.TXT ===")

# Example requirements.txt content
requirements_content = """# Web framework
Flask==2.3.2
Django>=4.2.0

# Data science
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0

# Testing
pytest>=7.0.0
pytest-cov>=4.0.0

# Development tools
black>=22.0.0
flake8>=5.0.0

# Utilities
requests>=2.28.0
python-dotenv>=0.19.0
"""

print("Example requirements.txt:")
print(requirements_content)

# Create a sample requirements.txt
with open("requirements.txt", "w") as f:
    f.write(requirements_content)
print("✓ Created sample requirements.txt")

print("\n=== PACKAGE STRUCTURE ===")

print("""
Typical Python package structure:

my_package/
├── setup.py              # Package configuration
├── README.md             # Documentation
├── requirements.txt      # Dependencies
├── my_package/           # Main package directory
│   ├── __init__.py      # Makes it a package
│   ├── module1.py       # Package modules
│   └── module2.py
├── tests/               # Test directory
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
└── docs/                # Documentation
    └── index.md
""")

print("\n=== CREATING A SIMPLE PACKAGE ===")

# Create a simple package structure
os.makedirs("my_sample_package", exist_ok=True)

# __init__.py file
init_content = '''"""
My Sample Package
A simple example package for learning.
"""

__version__ = "0.1.0"
__author__ = "Your Name"

from .calculator import Calculator
from .utils import greet

__all__ = ["Calculator", "greet"]
'''

with open("my_sample_package/__init__.py", "w") as f:
    f.write(init_content)

# calculator.py module
calculator_content = '''"""
Simple calculator module
"""

class Calculator:
    """A simple calculator class"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
'''

with open("my_sample_package/calculator.py", "w") as f:
    f.write(calculator_content)

# utils.py module
utils_content = '''"""
Utility functions
"""

def greet(name="World"):
    """Greet someone"""
    return f"Hello, {name}!"

def format_number(num, decimals=2):
    """Format a number with specified decimal places"""
    return f"{num:.{decimals}f}"
'''

with open("my_sample_package/utils.py", "w") as f:
    f.write(utils_content)

print("✓ Created sample package structure")

print("\n=== USING THE PACKAGE ===")

# Add current directory to Python path to import our package
sys.path.insert(0, '.')

try:
    from my_sample_package import Calculator, greet
    
    # Use the calculator
    calc = Calculator()
    print(f"Calculator: 5 + 3 = {calc.add(5, 3)}")
    print(f"Calculator: 10 - 4 = {calc.subtract(10, 4)}")
    
    # Use the utility function
    print(f"Greeting: {greet('Python Developer')}")
    
except ImportError as e:
    print(f"Could not import package: {e}")

print("\n=== SETUP.PY EXAMPLE ===")

setup_content = '''from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my-sample-package",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my-sample-package",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
)
'''

print("Example setup.py:")
print(setup_content[:500] + "...")

print("\n=== BEST PRACTICES ===")

best_practices = """
1. Always use virtual environments for projects
2. Pin exact versions in requirements.txt for production
3. Use semantic versioning (MAJOR.MINOR.PATCH)
4. Include a README.md with installation instructions
5. Add a .gitignore file to exclude __pycache__, .env, etc.
6. Use requirements-dev.txt for development dependencies
7. Test your package before publishing
8. Use meaningful package and module names
9. Document your code with docstrings
10. Follow PEP 8 style guidelines
"""

print(best_practices)

print("\n=== EXAM FOCUS: KEY COMMANDS ===")

exam_commands = """
Essential commands to remember:

1. python -m venv venv          # Create virtual environment
2. venv\\Scripts\\activate       # Activate (Windows)
3. source venv/bin/activate     # Activate (macOS/Linux)
4. pip install package_name     # Install package
5. pip freeze > requirements.txt # Save current packages
6. pip install -r requirements.txt # Install from requirements
7. pip list                     # List installed packages
8. pip show package_name        # Show package details
9. deactivate                   # Deactivate virtual environment
"""

print(exam_commands)

print("\n=== CLEANUP ===")
# Clean up created files
import shutil
try:
    os.remove("requirements.txt")
    shutil.rmtree("my_sample_package")
    print("✓ Cleaned up sample files")
except:
    pass

print("\nPackaging and virtual environments mastered! ✓")