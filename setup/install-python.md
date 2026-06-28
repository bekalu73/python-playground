# Installing Python

Python must be installed on your computer before you can write and run Python programs. This guide will walk you through the installation process for Windows, macOS, and Linux.

## Check if Python is Already Installed

Before installing, check if Python is already on your system:

### On Windows:
```cmd
python --version
```
or
```cmd
python3 --version
```

### On macOS/Linux:
```bash
python3 --version
```

If you see output like `Python 3.11.5` or similar, Python is already installed. If the version is **3.8 or higher**, you're good to go! If not, follow the installation steps below.

---

## Installing Python on Windows

### Step 1: Download Python

1. Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click the **"Download Python 3.x.x"** button (latest stable version)
3. The website automatically suggests the correct version for Windows

### Step 2: Run the Installer

1. **Important:** Check the box **"Add Python to PATH"** at the bottom of the installer
2. Click **"Install Now"** for standard installation
3. Wait for the installation to complete
4. Click **"Close"** when finished

### Step 3: Verify Installation

Open Command Prompt (Win + R, type `cmd`, press Enter) and run:

```cmd
python --version
```

You should see output like:
```
Python 3.11.5
```

Also verify pip (Python's package manager):
```cmd
pip --version
```

### Troubleshooting Windows

**Problem:** `python` command not recognized

**Solution:**
1. Reinstall Python and ensure "Add Python to PATH" is checked
2. Or manually add Python to PATH:
   - Search for "Environment Variables" in Windows
   - Edit "Path" under System Variables
   - Add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\`
   - Add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\Scripts\`

---

## Installing Python on macOS

macOS comes with Python 2.7 pre-installed, but you need Python 3.x for modern development.

### Method 1: Official Installer (Recommended for Beginners)

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest macOS installer
3. Open the `.pkg` file and follow the installation wizard
4. Complete the installation

### Method 2: Using Homebrew (Recommended for Developers)

If you have Homebrew installed:

```bash
brew install python3
```

If you don't have Homebrew, install it first:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Verify Installation

Open Terminal and run:

```bash
python3 --version
```

Output should be:
```
Python 3.11.5
```

Check pip:
```bash
pip3 --version
```

### Creating Aliases (Optional but Recommended)

Add to your `~/.zshrc` or `~/.bash_profile`:

```bash
alias python=python3
alias pip=pip3
```

Then reload:
```bash
source ~/.zshrc
```

Now you can use `python` instead of `python3`.

---

## Installing Python on Linux

Most Linux distributions come with Python 3 pre-installed. If not, follow these steps:

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Fedora

```bash
sudo dnf install python3 python3-pip
```

### Arch Linux

```bash
sudo pacman -S python python-pip
```

### Verify Installation

```bash
python3 --version
pip3 --version
```

---

## Understanding Python Versions

### Python 2 vs Python 3

- **Python 2**: End of life (January 2020) - **DO NOT USE**
- **Python 3**: Current version - **USE THIS**

### Recommended Versions

- **Minimum**: Python 3.8+
- **Recommended**: Python 3.10 or 3.11
- **Latest**: Check [python.org](https://www.python.org/downloads/)

### Version Compatibility

```python
# Check Python version in code
import sys
print(sys.version)
print(f"Python {sys.version_info.major}.{sys.version_info.minor}")
```

---

## Post-Installation Setup

### Upgrade pip

Always upgrade pip to the latest version:

```bash
# Windows
python -m pip install --upgrade pip

# macOS/Linux
python3 -m pip install --upgrade pip
```

### Install Essential Packages

```bash
# Virtual environment support (usually pre-installed)
pip install virtualenv

# Code formatting tool
pip install black

# Linter
pip install pylint
```

---

## Testing Your Installation

Create a test file to verify everything works:

### 1. Create a file named `test.py`:

```python
# test.py
print("Python is working! 🐍")
print(f"Python version: {__import__('sys').version}")

# Test basic functionality
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers]
print(f"Squared numbers: {squared}")
```

### 2. Run the file:

```bash
# Windows
python test.py

# macOS/Linux
python3 test.py
```

### Expected Output:

```
Python is working! 🐍
Python version: 3.11.5 (main, ...)
Squared numbers: [1, 4, 9, 16, 25]
```

---

## Common Installation Issues

### Issue 1: "Command not found"
**Cause:** Python not added to PATH
**Solution:** Reinstall and add to PATH, or add manually

### Issue 2: Multiple Python Versions
**Cause:** Having both Python 2 and 3 installed
**Solution:** Always use `python3` and `pip3` commands

### Issue 3: Permission Denied (Linux/macOS)
**Cause:** Trying to install system-wide without privileges
**Solution:** Use `pip install --user <package>` or virtual environments

### Issue 4: SSL Certificate Error
**Cause:** Outdated certificates
**Solution:** 
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package>
```

---

## Next Steps

Now that Python is installed, you're ready to set up your code editor!

📖 **[Installing Visual Studio Code →](install-vscode.md)**

---

## Quick Reference

### Check Python Version
```bash
python --version    # or python3 --version
```

### Check pip Version
```bash
pip --version       # or pip3 --version
```

### Upgrade pip
```bash
python -m pip install --upgrade pip
```

### Install Package
```bash
pip install package_name
```

### Run Python Script
```bash
python script.py
```

### Interactive Python Shell
```bash
python
>>> print("Hello")
>>> exit()
```

---

**Congratulations!** Python is now installed on your system. You're one step closer to becoming a Python developer! 🎉
