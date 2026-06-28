# Python Exam Preparation - Complete Study Guide

## 📚 Overview

This comprehensive Python study guide covers all essential concepts from basic to advanced levels, designed to help you master Python for your exam and become a proficient Python developer.

Every topic now comes in **two formats** so you can learn however suits you best:

- 📖 **Markdown docs (`.md`)** — read the concept, syntax, examples, common mistakes, best practices, and exercises.
- ▶️ **Python files (`.py`)** — run the live, commented code examples.

## 🗂️ Study Structure

### 📁 Setup (Start Here!)

New to Python? Set up your development environment first.

0. **Setup Guides**
   - **[Introduction](setup/introduction.md)** — What Python is and how to use this playground
   - **[Installing Python](setup/install-python.md)** — Windows, macOS & Linux + verifying the install
   - **[Installing VS Code](setup/install-vscode.md)** — Download, install, and tour the editor
   - **[VS Code Extensions](setup/vscode-extensions.md)** — Python, Pylance, Jupyter, Error Lens, and more
   - **[Environment Setup & Tools](setup/environment-setup.md)** — Terminal, virtual environments, pip, running code

### 📁 Basic Concepts (Foundation Level)

1. **Syntax & Indentation** — 📖 [docs](basic/01_syntax_indentation.md) · ▶️ [code](basic/01_syntax_indentation.py)

   - Python indentation rules
   - Code block structure
   - Common indentation errors

2. **Data Types & Dynamic Typing** — 📖 [docs](basic/02_data_types.md) · ▶️ [code](basic/02_data_types.py)

   - Built-in data types (int, float, str, bool, list, dict, tuple, set)
   - Dynamic typing concepts
   - Type checking and conversion

3. **Operators** — 📖 [docs](basic/03_operators.md) · ▶️ [code](basic/03_operators.py)

   - Arithmetic operators (+, -, \*, /, //, %, \*\*)
   - Logical operators (and, or, not)
   - Comparison operators (==, !=, <, >, <=, >=)
   - Membership operators (in, not in)
   - Identity operators (is, is not)

4. **Control Flow** — 📖 [docs](basic/04_control_flow.md) · ▶️ [code](basic/04_control_flow.py)

   - if/elif/else statements
   - for and while loops
   - Loop-else clause (unique Python feature!)
   - break and continue statements

5. **Functions & Scope** — 📖 [docs](basic/05_functions_scope.md) · ▶️ [code](basic/05_functions_scope.py)

   - Function definition and calling
   - Parameters vs arguments
   - \*args and \*\*kwargs
   - Local vs global scope
   - Lambda functions

6. **Lists & Dictionaries** — 📖 [docs](basic/06_lists_dictionaries.md) · ▶️ [code](basic/06_lists_dictionaries.py)

   - List operations and methods
   - List comprehensions
   - Dictionary operations and methods
   - Dictionary comprehensions
   - Nested structures

7. **Strings & Formatting** — 📖 [docs](basic/07_strings_formatting.md) · ▶️ [code](basic/07_strings_formatting.py)

   - String methods and operations
   - String formatting (f-strings, .format(), % formatting)
   - String validation and manipulation
   - Escape characters and raw strings

8. **File I/O** — 📖 [docs](basic/08_file_io.md) · ▶️ [code](basic/08_file_io.py)
   - Opening and closing files
   - Reading and writing operations
   - Context managers (with statement)
   - File modes and error handling

### 📁 Intermediate Concepts

9. **Packaging & Virtual Environments** — 📖 [docs](intermediate/09_packaging_venv.md) · ▶️ [code](intermediate/09_packaging_venv.py)

   - Virtual environments with venv
   - Package management with pip
   - requirements.txt
   - Package structure and distribution

10. **PEP 8 & Code Style** — 📖 [docs](intermediate/10_pep8_code_style.md) · ▶️ [code](intermediate/10_pep8_code_style.py)

    - Official Python style guide
    - Naming conventions
    - Code layout and formatting
    - Import organization
    - Tools for style checking

11. **OOP Fundamentals** — 📖 [docs](intermediate/11_oop_fundamentals.md) · ▶️ [code](intermediate/11_oop_fundamentals.py)
    - Class definition and instantiation
    - Constructor method (**init**)
    - Instance vs class variables
    - Instance, class, and static methods
    - Object identity and equality

### 📁 Advanced Concepts

12. **OOP Principles** — 📖 [docs](advanced/12_oop_principles.md) · ▶️ [code](advanced/12_oop_principles.py)

    - Inheritance and method overriding
    - Encapsulation (public, protected, private)
    - Polymorphism
    - Multiple inheritance and MRO
    - Abstract classes and interfaces

13. **Magic Methods** — 📖 [docs](advanced/13_magic_methods.md) · ▶️ [code](advanced/13_magic_methods.py)

    - String representation (**str**, **repr**)
    - Arithmetic operations (**add**, **sub**, etc.)
    - Comparison operations (**eq**, **lt**, etc.)
    - Container operations (**len**, **getitem**, etc.)
    - Context managers (**enter**, **exit**)

14. **Generators & Iteration** — 📖 [docs](advanced/14_generators_iteration.md) · ▶️ [code](advanced/14_generators_iteration.py)

    - Generator functions with yield
    - Generator expressions
    - Iterator protocol (**iter**, **next**)
    - Memory efficiency and lazy evaluation
    - yield from and generator delegation

15. **Regular Expressions** — 📖 [docs](advanced/15_regular_expressions.md) · ▶️ [code](advanced/15_regular_expressions.py)

    - Pattern matching with re module
    - Common regex patterns and metacharacters
    - Groups and capturing
    - Text validation and extraction
    - Practical applications

16. **Asynchronous I/O** — 📖 [docs](advanced/16_async_io.md) · ▶️ [code](advanced/16_async_io.py)
    - async/await syntax
    - Event loop and coroutines
    - Concurrent vs parallel execution
    - Error handling in async code
    - Practical async patterns

### 📁 Practice Questions

17. **[Complete Practice Set](practice/practice_questions.py)**
    - All roadmap practice questions with solutions
    - Comprehensive examples combining multiple concepts
    - Real-world applications

## 🎯 How to Use This Study Guide

### 1. **Sequential Learning Path**

```
Setup → Basic (1-8) → Intermediate (9-11) → Advanced (12-16) → Practice (17)
```

> 📖 **Tip:** For each topic, read the `.md` doc first to learn the concept, then run the `.py` file to see it in action — and try the exercises at the end of each doc.

### 2. **Daily Study Plan**

- **Week 1**: Basic concepts (1-4)
- **Week 2**: Basic concepts (5-8)
- **Week 3**: Intermediate concepts (9-11)
- **Week 4**: Advanced concepts (12-16)
- **Week 5**: Practice questions and review

### 3. **Running the Code**

Each file is executable and contains:

- Concept explanations
- Practical examples
- Common exam patterns
- Key points summary

```bash
# Run any concept file
python basic/01_syntax_indentation.py
python intermediate/09_packaging_venv.py
python advanced/13_magic_methods.py
python practice/practice_questions.py
```

## 🔑 Key Exam Topics

### **Must-Know Concepts**

- ✅ Python syntax and indentation rules
- ✅ Data types and dynamic typing
- ✅ Control flow (especially loop-else)
- ✅ Functions with \*args/\*\*kwargs
- ✅ List and dictionary comprehensions
- ✅ String formatting (f-strings)
- ✅ File I/O with context managers
- ✅ OOP fundamentals (classes, inheritance)
- ✅ Magic methods (**str**, **len**, etc.)
- ✅ Generators and yield
- ✅ Regular expressions basics
- ✅ Basic async/await

### **Common Exam Patterns**

1. **Loop-else clause** - unique Python feature
2. **Generator vs list comprehension** - memory efficiency
3. **\*args and **kwargs\*\* - flexible function parameters
4. **Magic methods** - operator overloading
5. **Context managers** - resource management
6. **Inheritance and MRO** - object-oriented design

## 📖 Quick Reference

### **Essential Built-in Functions**

```python
len(), range(), enumerate(), zip(), map(), filter()
isinstance(), type(), hasattr(), getattr()
min(), max(), sum(), sorted(), reversed()
open(), print(), input(), format()
```

### **Important Modules**

```python
import re          # Regular expressions
import os          # Operating system interface
import sys         # System-specific parameters
import asyncio     # Asynchronous I/O
import datetime    # Date and time handling
import json        # JSON encoder/decoder
```

### **PEP 8 Quick Rules**

- Use 4 spaces for indentation
- Lines ≤ 79 characters
- snake_case for variables/functions
- PascalCase for classes
- UPPER_SNAKE_CASE for constants

## 🚀 Exam Success Tips

1. **Practice Coding by Hand** - Many exams require writing code without IDE
2. **Understand Error Messages** - Know common exceptions and their causes
3. **Master List/Dict Comprehensions** - Very commonly tested
4. **Know the Difference** - Generator vs list, is vs ==, \*args vs \*\*kwargs
5. **Practice Time Management** - Code efficiently under time pressure

## 🎓 After the Exam

Continue your Python journey with:

- **Web Development**: Django, Flask, FastAPI
- **Data Science**: NumPy, Pandas, Matplotlib
- **Machine Learning**: Scikit-learn, TensorFlow, PyTorch
- **Automation**: Selenium, Beautiful Soup, Requests
- **Desktop Apps**: Tkinter, PyQt, Kivy

## 📞 Need Help?

If you encounter any issues or have questions:

1. Check the comments in each file for explanations
2. Run the code to see examples in action
3. Practice the concepts with your own variations
4. Review the "Exam Focus" sections in each file

---

**Good luck with your Python exam! 🐍✨**

_Remember: The best way to learn Python is by writing Python code. Practice regularly and don't just read - code along!_
