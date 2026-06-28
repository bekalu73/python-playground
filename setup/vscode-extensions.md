# Required VS Code Extensions

Extensions add extra features to VS Code. For Python development, certain extensions are essential while others are nice-to-have. This guide covers the recommended extensions for the best Python coding experience.

## How to Install Extensions

There are two easy ways to install extensions:

### Method 1: Using the Extensions Panel
1. Click the **Extensions** icon in the Activity Bar (or press `Ctrl+Shift+X`)
2. Type the extension name in the search box
3. Click **"Install"** on the extension you want

### Method 2: Using the Command Palette
1. Press `Ctrl+Shift+P`
2. Type "Extensions: Install Extensions"
3. Search and install

---

## Essential Extensions (Must Have)

### 1. Python (by Microsoft)

**Extension ID:** `ms-python.python`

This is the **most important** extension for Python development. It provides core Python language support.

**Why You Need It:**
- IntelliSense (smart code completion)
- Linting (error detection)
- Debugging support
- Code navigation
- Running and testing Python files
- Jupyter notebook support
- Virtual environment detection

**How to Install:**
1. Open Extensions (`Ctrl+Shift+X`)
2. Search for "Python"
3. Install the one by **Microsoft** (it has millions of downloads)

> ⚠️ **Important:** Make sure you install the official Microsoft extension, not a third-party one.

---

### 2. Pylance (by Microsoft)

**Extension ID:** `ms-python.vscode-pylance`

Pylance is a powerful language server that provides fast, feature-rich Python support. It's usually installed automatically with the Python extension.

**Why You Need It:**
- Lightning-fast IntelliSense
- Type checking and hints
- Auto-imports
- Better code navigation
- Detailed function signatures
- Detects errors as you type

**How to Install:**
- Usually installed automatically with the Python extension
- If not, search "Pylance" in Extensions and install

**Example of what Pylance does:**
```python
# Pylance suggests completions as you type
import datetime
datetime.  # <- Pylance shows all available methods

# Pylance shows type hints
def greet(name: str) -> str:
    return f"Hello, {name}"

greet(123)  # <- Pylance warns: expected str, got int
```

---

## Recommended Extensions (Optional but Helpful)

### 3. Jupyter (by Microsoft)

**Extension ID:** `ms-toolsai.jupyter`

Allows you to create and run Jupyter notebooks directly in VS Code.

**Why It's Useful:**
- Interactive coding with cells
- Great for data science and experimentation
- See output immediately
- Mix code, text, and visualizations
- Perfect for learning and testing snippets

**When to Use:**
- Data analysis projects
- Machine learning experiments
- Quick code testing
- Creating tutorials

**How to Install:**
- Search "Jupyter" in Extensions
- Install the Microsoft version

---

### 4. Error Lens

**Extension ID:** `usernamehw.errorlens`

Makes errors and warnings much more visible by displaying them inline.

**Why It's Useful:**
- Shows errors right next to the code (not just underlined)
- Highlights the entire line with the error
- Helps you spot mistakes faster
- Great for beginners learning to debug

**Before Error Lens:**
```python
x = 10
print(y)  # Error only shown when you hover
```

**With Error Lens:**
```python
x = 10
print(y)  # "y" is not defined  <- shown inline in red
```

**How to Install:**
- Search "Error Lens" in Extensions
- Install the one by Alexander

---

### 5. Material Icon Theme

**Extension ID:** `pkief.material-icon-theme`

Adds beautiful, colorful icons to files and folders in the Explorer.

**Why It's Useful:**
- Easier to identify file types at a glance
- Makes the file explorer more visually appealing
- Python files get a distinct icon
- Folders have meaningful icons

**How to Install:**
1. Search "Material Icon Theme" in Extensions
2. Install
3. Activate: `Ctrl+Shift+P` → "File Icon Theme" → "Material Icon Theme"

---

## Bonus Extensions (Nice to Have)

### autoDocstring
**Extension ID:** `njpwerner.autodocstring`
- Automatically generates docstring templates
- Type `"""` and press Enter to generate a template

### Code Spell Checker
**Extension ID:** `streetsidesoftware.code-spell-checker`
- Catches spelling mistakes in comments and strings
- Helpful for clean documentation

### indent-rainbow
**Extension ID:** `oderwat.indent-rainbow`
- Colorizes indentation levels
- Helps visualize Python's indentation-based structure

### GitLens
**Extension ID:** `eamodio.gitlens`
- Enhanced Git capabilities
- See who changed each line and when

---

## Extension Summary Table

| Extension | Required? | Purpose |
|-----------|-----------|---------|
| Python | ✅ Essential | Core Python support |
| Pylance | ✅ Essential | Fast IntelliSense & type checking |
| Jupyter | Optional | Interactive notebooks |
| Error Lens | Optional | Inline error display |
| Material Icon Theme | Optional | Better file icons |
| autoDocstring | Bonus | Docstring generation |
| Code Spell Checker | Bonus | Spelling in comments |
| indent-rainbow | Bonus | Visualize indentation |

---

## Configuring Python Extension

After installing the Python extension, you may need to select your Python interpreter:

1. Press `Ctrl+Shift+P`
2. Type "Python: Select Interpreter"
3. Choose your Python installation (or virtual environment)

You'll see the selected interpreter in the bottom status bar.

### Setting Up Code Formatting

To automatically format your code:

1. Open Settings (`Ctrl+,`)
2. Search for "format on save"
3. Enable "Editor: Format On Save"
4. Set a formatter (e.g., install `black` and set it as default)

```json
// settings.json
{
    "editor.formatOnSave": true,
    "python.formatting.provider": "black"
}
```

---

## Verifying Your Setup

Create a test file `hello.py`:

```python
# hello.py
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

message = greet("Python Developer")
print(message)
```

**Check that:**
- ✅ Syntax highlighting works (colored code)
- ✅ IntelliSense shows suggestions as you type
- ✅ You can run the file (click the ▶️ play button or `Ctrl+F5`)
- ✅ The output appears in the terminal

---

## Next Steps

With your extensions installed, you're almost ready to start coding! The final step is learning about the development environment and tools.

📖 **[Environment Setup & Tools →](environment-setup.md)**

---

## Quick Reference

### Install Extension
- `Ctrl+Shift+X` → Search → Install

### Select Python Interpreter
- `Ctrl+Shift+P` → "Python: Select Interpreter"

### Set File Icon Theme
- `Ctrl+Shift+P` → "File Icon Theme"

---

**Excellent!** Your VS Code is now a powerful Python development environment. Let's learn about the essential tools next! 🛠️
