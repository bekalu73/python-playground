# Installing Visual Studio Code

A good code editor makes programming much easier and more enjoyable. This guide covers installing **Visual Studio Code (VS Code)**, the recommended editor for Python development.

## What is VS Code?

**Visual Studio Code** is a free, open-source code editor developed by Microsoft. Despite being lightweight, it's incredibly powerful and is one of the most popular editors among developers worldwide.

### Why VS Code for Python?

1. **Free and Open Source**
   - Completely free to use
   - No licensing fees
   - Regular updates

2. **Excellent Python Support**
   - IntelliSense (smart code completion)
   - Debugging tools
   - Integrated terminal
   - Jupyter notebook support

3. **Lightweight but Powerful**
   - Fast startup
   - Low resource usage
   - Extensible with thousands of extensions

4. **Cross-Platform**
   - Works on Windows, macOS, and Linux
   - Same experience across all platforms

5. **Built-in Features**
   - Integrated Git support
   - Built-in terminal
   - Code formatting
   - Syntax highlighting

### VS Code vs Other Editors

| Feature | VS Code | PyCharm | Sublime Text | IDLE |
|---------|---------|---------|--------------|------|
| Free | ✅ | Partial | Trial | ✅ |
| Lightweight | ✅ | ❌ | ✅ | ✅ |
| Extensions | ✅ | ✅ | ✅ | ❌ |
| Debugging | ✅ | ✅ | Limited | Basic |
| Beginner-Friendly | ✅ | Medium | Medium | ✅ |

---

## Downloading VS Code

### Step 1: Visit the Official Website

Go to: [https://code.visualstudio.com/](https://code.visualstudio.com/)

The website automatically detects your operating system and shows the appropriate download button.

### Step 2: Download

Click the big **"Download"** button for your operating system:
- **Windows**: Downloads a `.exe` installer
- **macOS**: Downloads a `.zip` file
- **Linux**: Downloads `.deb` or `.rpm` packages

---

## Installing on Windows

1. Run the downloaded `.exe` file
2. Accept the license agreement
3. Choose installation location (default is fine)
4. **Recommended:** Check these options:
   - ✅ "Add to PATH"
   - ✅ "Register Code as an editor for supported file types"
   - ✅ "Add 'Open with Code' action to Windows Explorer file context menu"
   - ✅ "Add 'Open with Code' action to Windows Explorer directory context menu"
5. Click **"Install"**
6. Click **"Finish"** when done

---

## Installing on macOS

1. Open the downloaded `.zip` file (it extracts automatically)
2. Drag **Visual Studio Code.app** to the **Applications** folder
3. Open VS Code from Applications
4. **Optional but recommended:** Add `code` command to PATH:
   - Open VS Code
   - Press `Cmd + Shift + P`
   - Type "Shell Command: Install 'code' command in PATH"
   - Press Enter

Now you can open VS Code from the terminal by typing `code .`

---

## Installing on Linux

### Ubuntu/Debian (.deb)

```bash
sudo apt install ./code_*.deb
```

Or via the official repository:
```bash
sudo snap install --classic code
```

### Fedora/RHEL (.rpm)

```bash
sudo rpm -i code-*.rpm
```

### Arch Linux

```bash
sudo pacman -S code
```

---

## First Launch

When you open VS Code for the first time, you'll see:

1. **Welcome Tab** - Quick start guide and recent files
2. **Activity Bar** (left side) - Icons for Explorer, Search, Git, Debug, Extensions
3. **Status Bar** (bottom) - Shows current settings and information

### VS Code Interface Overview

```
┌─────────────────────────────────────────────┐
│  File  Edit  View  ...           Menu Bar    │
├──┬──────────────────────────────────────────┤
│  │                                           │
│ A│                                           │
│ c│           Editor Area                     │
│ t│      (where you write code)               │
│ i│                                           │
│ v│                                           │
│ i├──────────────────────────────────────────┤
│ t│           Terminal                        │
│ y│      (integrated command line)            │
├──┴──────────────────────────────────────────┤
│           Status Bar                         │
└─────────────────────────────────────────────┘
```

### Key Areas Explained

- **Explorer** (`Ctrl+Shift+E`): Browse and manage your files
- **Search** (`Ctrl+Shift+F`): Search across all files
- **Source Control** (`Ctrl+Shift+G`): Git integration
- **Run and Debug** (`Ctrl+Shift+D`): Debugging tools
- **Extensions** (`Ctrl+Shift+X`): Install add-ons

---

## Essential Keyboard Shortcuts

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Open File | `Ctrl+P` | `Cmd+P` |
| Toggle Terminal | `` Ctrl+` `` | `` Cmd+` `` |
| Save File | `Ctrl+S` | `Cmd+S` |
| Comment Line | `Ctrl+/` | `Cmd+/` |
| Find | `Ctrl+F` | `Cmd+F` |
| Find and Replace | `Ctrl+H` | `Cmd+Option+F` |
| Format Document | `Shift+Alt+F` | `Shift+Option+F` |
| Run Python File | `Ctrl+F5` | `Ctrl+F5` |

> 💡 **Tip:** The Command Palette (`Ctrl+Shift+P`) is your best friend. You can access almost any VS Code feature from there!

---

## Opening a Project

### Method 1: From VS Code
1. **File → Open Folder**
2. Navigate to your project folder (e.g., `python-playground`)
3. Click **"Select Folder"**

### Method 2: From Terminal
```bash
cd python-playground
code .
```

The `.` means "current folder".

---

## Customizing VS Code (Optional)

### Change Theme
1. Press `Ctrl+K` then `Ctrl+T`
2. Choose from available themes
3. Popular choices: Dark+, Monokai, Solarized

### Adjust Font Size
1. Open Settings (`Ctrl+,`)
2. Search for "font size"
3. Adjust "Editor: Font Size"

---

## Next Steps

Now that VS Code is installed, you need to add Python-specific extensions to unlock its full potential!

📖 **[Required VS Code Extensions →](vscode-extensions.md)**

---

## Quick Reference

### Open VS Code from Terminal
```bash
code .              # Open current folder
code filename.py    # Open specific file
```

### Essential Shortcuts
- `Ctrl+Shift+P` - Command Palette
- `` Ctrl+` `` - Toggle Terminal
- `Ctrl+S` - Save
- `Ctrl+/` - Comment/Uncomment

---

**Great job!** You now have a professional code editor installed. Next, let's supercharge it with Python extensions! 🚀
