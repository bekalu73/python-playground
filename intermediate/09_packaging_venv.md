# Packaging & Virtual Environments

> 📄 **Related code file:** [`09_packaging_venv.py`](09_packaging_venv.py)

## Overview

As your projects grow, you'll need to manage **dependencies** (external packages) and organize your code into reusable **packages**. Virtual environments isolate each project's dependencies, and `pip` installs packages from the Python Package Index (PyPI).

> 💡 If you completed the [Setup section](../setup/environment-setup.md), you've already seen virtual environments and pip. This lesson goes deeper into packaging your own code.

## Virtual Environments

A **virtual environment** is an isolated Python environment with its own packages, separate from your system Python and other projects.

### Why?
- Different projects need different package versions
- Keeps your global Python clean
- Makes dependencies reproducible

### Commands
```bash
# Create
python -m venv myenv

# Activate
myenv\Scripts\activate        # Windows
source myenv/bin/activate     # macOS/Linux

# Deactivate
deactivate
```

### Checking if you're in a virtual environment
```python
import sys
in_venv = sys.prefix != sys.base_prefix
print(f"In virtual environment: {in_venv}")
print(f"Python executable: {sys.executable}")
```

## pip — Package Management

`pip` installs and manages packages.

```bash
pip install requests              # install latest
pip install requests==2.28.0      # specific version
pip install "requests>=2.28.0"    # minimum version
pip install --upgrade requests    # upgrade
pip uninstall requests            # remove
pip list                          # list installed
pip show requests                 # package details
pip freeze                        # output in requirements format
```

## requirements.txt

This file lists your project's dependencies so anyone can recreate the environment.

```text
# Web framework
Flask==2.3.2

# Data science
numpy>=1.21.0
pandas>=1.3.0

# Testing
pytest>=7.0.0
```

```bash
# Save current packages
pip freeze > requirements.txt

# Install from the file
pip install -r requirements.txt
```

## Package Structure

A **package** is a directory of Python modules. The key is the `__init__.py` file, which marks a directory as a package.

```text
my_package/
├── setup.py              # Package configuration
├── README.md             # Documentation
├── requirements.txt      # Dependencies
├── my_package/           # The actual package
│   ├── __init__.py      # Makes it a package
│   ├── calculator.py    # A module
│   └── utils.py         # Another module
└── tests/               # Tests
    ├── __init__.py
    └── test_calculator.py
```

### The `__init__.py` file
```python
"""My Sample Package."""

__version__ = "0.1.0"
__author__ = "Your Name"

from .calculator import Calculator
from .utils import greet

__all__ = ["Calculator", "greet"]   # what `from package import *` exposes
```

### A module inside the package
```python
# calculator.py
class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
```

### Using the package
```python
from my_sample_package import Calculator, greet

calc = Calculator()
print(calc.add(5, 3))          # 8
print(greet("Developer"))      # Hello, Developer!
```

## setup.py — Distributing Your Package

To share your package (e.g., on PyPI), you describe it in `setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="my-sample-package",
    version="0.1.0",
    author="Your Name",
    description="A simple example package",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=["requests>=2.25.0"],
)
```

## Common Mistakes

❌ **Installing packages globally** instead of in a virtual environment — leads to conflicts.

❌ **Forgetting to activate the venv** before installing — packages go to the wrong place.

❌ **Committing the `venv/` folder to Git** — add it to `.gitignore` instead.

❌ **Forgetting `__init__.py`** — the directory won't be recognized as a package (though namespace packages exist, explicit is clearer).

## Best Practices

✅ Use a virtual environment for **every** project.
✅ Pin exact versions in `requirements.txt` for production reproducibility.
✅ Use semantic versioning (`MAJOR.MINOR.PATCH`).
✅ Add a `.gitignore` excluding `venv/`, `__pycache__/`, `.env`.
✅ Keep a separate `requirements-dev.txt` for development-only tools.
✅ Document installation steps in your README.

## Exercises

1. **Create a venv:** Make a virtual environment, activate it, install `requests`, and run `pip freeze`.

2. **Requirements file:** Save the output of `pip freeze` to `requirements.txt`, then describe how a teammate would use it.

3. **Build a mini package:** Create a folder `mathtools/` with `__init__.py` and a module `operations.py` containing an `add` and `multiply` function. Import and use it.

4. **Version pinning:** Explain the difference between `requests==2.28.0` and `requests>=2.28.0`.

<details>
<summary>💡 Solution hints</summary>

```bash
# Exercise 1
python -m venv venv
source venv/bin/activate
pip install requests
pip freeze
```

```python
# Exercise 3 — mathtools/operations.py
def add(a, b): return a + b
def multiply(a, b): return a * b

# mathtools/__init__.py
from .operations import add, multiply
```
</details>

## Key Takeaways

- Virtual environments isolate project dependencies (`python -m venv`).
- `pip` installs packages; `requirements.txt` makes dependencies reproducible.
- A directory becomes a package with an `__init__.py` file.
- `setup.py` describes a package for distribution.

---

▶️ **Run the examples:** `python intermediate/09_packaging_venv.py`
⏮️ **Previous:** [Basic: File I/O](../basic/08_file_io.md) | ⏭️ **Next:** [PEP 8 & Code Style →](10_pep8_code_style.md)
