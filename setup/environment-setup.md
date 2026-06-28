# Environment Setup & Recommended Tools

Now that you have Python and VS Code installed, let's learn the essential tools and workflows every Python developer should know: using the terminal, creating virtual environments, managing packages, and running your code.

## Terminal Basics

The **terminal** (also called command line, shell, or console) lets you interact with your computer by typing commands. It's an essential tool for Python development.

### Opening the Terminal

**In VS Code:**
- Press `` Ctrl+` `` (backtick) or
- Menu: **Terminal → New Terminal**

**Standalone:**
- **Windows**: Command Prompt or PowerShell
- **macOS**: Terminal app
- **Linux**: Terminal app

### Essential Terminal Commands

| Command | Windows | macOS/Linux | Description |
|---------|---------|-------------|-------------|
| List files | `dir` | `ls` | Show files in current folder |
| Change directory | `cd folder` | `cd folder` | Move into a folder |
| Go up one level | `cd ..` | `cd ..` | Move to parent folder |
| Current location | `cd` | `pwd` | Show current path |
| Make directory | `mkdir name` | `mkdir name` | Create a new folder |
| Clear screen | `cls` | `clear` | Clear the terminal |
| Create file | `type nul > f.txt` | `touch f.txt` | Create empty file |

### Navigation Examples

```bash
# See where you are
pwd                    # macOS/Linux
cd                     # Windows

# List files
ls                     # macOS/Linux
dir                    # Windows

# Move into a folder
cd python-playground

# Move into a subfolder
cd basic

# Go back up
cd ..

# Go to home directory
cd ~                   # macOS/Linux
cd %USERPROFILE%       # Windows
```

> 💡 **Tip:** Use the `Tab` key to auto-complete file and folder names. Start typing and press Tab!

---

## Virtual Environments

A **virtual environment** is an isolated Python environment for a specific project. It keeps your project's dependencies separate from other projects and your system Python.

### Why Use Virtual Environments?

Imagine you have two projects:
- **Project A** needs `Django 3.2`
- **Project B** needs `Django 4.2`

Without virtual environments, these would conflict! Virtual environments solve this by giving each project its own isolated set of packages.

**Benefits:**
- ✅ Avoid version conflicts between projects
- ✅ Keep your system Python clean
- ✅ Easy to recreate environments
- ✅ Share exact dependencies with others

### Creating a Virtual Environment

Python comes with a built-in module called `venv`:

```bash
# Navigate to your project folder
cd python-playground

# Create a virtual environment named "venv"
python -m venv venv

# On macOS/Linux you may need:
python3 -m venv venv
```

This creates a `venv` folder containing an isolated Python installation.

### Activating the Virtual Environment

You must **activate** the environment before using it:

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

When activated, you'll see `(venv)` at the start of your terminal prompt:
```
(venv) user@computer:~/python-playground$
```

### Deactivating

When you're done working, deactivate the environment:

```bash
deactivate
```

### Important Notes

- Activate the environment **every time** you open a new terminal for the project
- Add `venv/` to your `.gitignore` file (don't commit it to Git)
- The folder name is conventionally `venv` or `.venv`

---

## Installing Packages with pip

**pip** is Python's package installer. It downloads and installs packages from the Python Package Index (PyPI).

### Basic pip Commands

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.28.0

# Install minimum version
pip install "requests>=2.28.0"

# Upgrade a package
pip install --upgrade requests

# Uninstall a package
pip uninstall requests

# List installed packages
pip list

# Show package details
pip show requests
```

### Managing Dependencies with requirements.txt

A `requirements.txt` file lists all your project's dependencies. This makes it easy to recreate the environment.

**Save your current packages:**
```bash
pip freeze > requirements.txt
```

**Example requirements.txt:**
```text
requests==2.28.0
flask==2.3.2
pandas>=1.5.0
```

**Install from requirements.txt:**
```bash
pip install -r requirements.txt
```

This is how teams share dependencies. When someone clones your project, they just run this command to install everything they need.

### Typical Workflow

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux

# 2. Install packages you need
pip install requests flask

# 3. Save dependencies
pip freeze > requirements.txt

# 4. Work on your project...

# 5. Deactivate when done
deactivate
```

---

## Running Python Files

There are several ways to run Python code.

### Method 1: From the Terminal

This is the most common way:

```bash
# Run a Python file
python script.py

# On macOS/Linux you may need:
python3 script.py

# Run a file in a subfolder
python basic/01_syntax_indentation.py
```

### Method 2: From VS Code

**Option A: Run Button**
- Open a Python file
- Click the ▶️ **Run** button in the top-right corner
- Output appears in the integrated terminal

**Option B: Keyboard Shortcut**
- Press `Ctrl+F5` to run without debugging
- Press `F5` to run with debugging

**Option C: Right-Click**
- Right-click in the editor
- Select "Run Python File in Terminal"

### Method 3: Interactive Python Shell

For quick experiments:

```bash
# Start the Python shell
python

# Now you can type code interactively
>>> 2 + 2
4
>>> print("Hello")
Hello
>>> exit()    # Exit the shell
```

---

## Recommended Project Structure

Organizing your project well makes it easier to maintain:

```text
my-project/
├── venv/                  # Virtual environment (don't commit)
├── src/                   # Your source code
│   ├── __init__.py
│   └── main.py
├── tests/                 # Test files
│   └── test_main.py
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── .gitignore             # Files Git should ignore
```

### Example .gitignore for Python

```text
# Virtual environment
venv/
.venv/

# Python cache
__pycache__/
*.pyc

# Environment variables
.env

# IDE settings
.vscode/
.idea/
```

---

## Complete Setup Checklist

Before starting to code, verify you have everything:

- [ ] Python installed (`python --version` shows 3.8+)
- [ ] pip working (`pip --version`)
- [ ] VS Code installed
- [ ] Python extension installed in VS Code
- [ ] Pylance extension installed
- [ ] Know how to open the terminal
- [ ] Know how to create a virtual environment
- [ ] Know how to activate/deactivate venv
- [ ] Know how to install packages with pip
- [ ] Know how to run a Python file

---

## Common Workflow Summary

Here's the typical workflow for starting a new Python project:

```bash
# 1. Create project folder
mkdir my-project
cd my-project

# 2. Open in VS Code
code .

# 3. Create virtual environment
python -m venv venv

# 4. Activate it
source venv/bin/activate        # macOS/Linux
# OR
venv\Scripts\activate           # Windows

# 5. Install packages
pip install <package-names>

# 6. Save dependencies
pip freeze > requirements.txt

# 7. Write and run your code
python main.py
```

---

## Troubleshooting

### "python: command not found"
- Python isn't in your PATH. Try `python3` instead, or reinstall Python with "Add to PATH" checked.

### "pip: command not found"
- Try `python -m pip` instead of `pip`.

### PowerShell won't activate venv
- Run as administrator: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Wrong Python being used
- In VS Code: `Ctrl+Shift+P` → "Python: Select Interpreter" → choose your venv.

---

## Next Steps

🎉 **Congratulations!** Your development environment is fully set up. You now have everything you need to start learning Python.

### Ready to Start Coding?

Head to the **Basic Python** section to begin your journey:

📖 **[Start with Basic Python: Syntax & Indentation →](../basic/01_syntax_indentation.md)**

---

## Quick Reference Card

### Virtual Environment
```bash
python -m venv venv              # Create
source venv/bin/activate         # Activate (macOS/Linux)
venv\Scripts\activate            # Activate (Windows)
deactivate                       # Deactivate
```

### Package Management
```bash
pip install package              # Install
pip freeze > requirements.txt    # Save dependencies
pip install -r requirements.txt  # Install dependencies
pip list                         # List installed
```

### Running Code
```bash
python script.py                 # Run file
python                           # Interactive shell
```

---

**You're all set!** Time to write some Python. Happy coding! 🐍✨
