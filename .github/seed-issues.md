# Seed Issues — Copy & Paste to GitHub

Go to https://github.com/bekalu73/python-playground/issues/new and paste each issue below.

---

## Issue 1: Add a `.gitignore` file

**Title:** `Add .gitignore for Python projects`

**Labels:** `enhancement`, `good first issue`

**Body:**
```
The repo is missing a `.gitignore` file. This means compiled Python files (`.pyc`), virtual environments, and OS files (`.DS_Store`) can accidentally get committed.

Add a Python-focused `.gitignore` that excludes:

- `__pycache__/` and `*.pyc`
- `.env`, `venv/`, `.venv/`
- `.DS_Store`
- `*.egg-info/`
- `.mypy_cache/`, `.pytest_cache/`
```

---

## Issue 2: Add a topic on Decorators

**Title:** `[Feature] Add topic: Decorators`

**Labels:** `enhancement`

**Body:**
```
Decorators are a key Python concept that frequently appears in exams and interviews. We should add a new section covering:

- Function decorators (`@decorator` syntax)
- `functools.wraps`
- Decorators with arguments
- Common use cases (timing, logging, access control)

Files to create:
- `intermediate/17_decorators.md`
- `intermediate/17_decorators.py`
- Update README with the new entry
```

---

## Issue 3: Add a topic on Decorators

**Title:** `[Feature] Add topic: Exception Handling`

**Labels:** `enhancement`

**Body:**
```
Exception handling is a fundamental Python topic currently missing. We should add:

- try/except/else/finally
- Common built-in exceptions
- Raising exceptions
- Custom exception classes
- Best practices

Files to create:
- `intermediate/18_exceptions.md`
- `intermediate/18_exceptions.py`
- Update README
```

---

## Issue 4: Add type hints to code examples

**Title:** `[Improvement] Add type hints to Python examples`

**Labels:** `help wanted`, `enhancement`

**Body:**
```
The code examples would benefit from modern Python type hints. This helps readers understand expected types and matches current Python best practices.

Example:
```python
# Current
def sum_numbers(*args):
    return sum(args)

# Improved
def sum_numbers(*args: int | float) -> int | float:
    return sum(args)
```

Start with basic/ files and work upward.
```

---

## Issue 5: Add more practice questions

**Title:** `[Feature] Add more practice questions`

**Labels:** `enhancement`, `help wanted`

**Body:**
```
The practice set (practice/practice_questions.py) has 7 questions. We should expand it with:

- Questions on decorators
- Questions on exception handling
- Questions on context managers (custom)
- Questions on modules and imports
- A mock exam section with 20+ mixed questions

Each question should have both the problem statement and solution.
```

---

## Issue 6: Typo / formatting pass

**Title:** `[Improvement] Proofread all docs for typos and consistent formatting`

**Labels:** `documentation`, `good first issue`

**Body:**
```
Do a pass across all .md files to catch:

- Typos and grammatical errors
- Inconsistent code formatting (some docs use 2-space indent in examples)
- Missing language tags on fenced code blocks
- Broken internal links

This is a great first issue for new contributors.
```

---

## Issue 7: Add a topic on Modules and Packages

**Title:** `[Feature] Add topic: Modules and Packages`

**Labels:** `enhancement`

**Body:**
```
Python's module system is exam-relevant but currently missing. Cover:

- `import` vs `from ... import`
- `if __name__ == "__main__"`
- Creating packages with `__init__.py`
- Relative vs absolute imports
- `sys.path` and module search order

Files:
- `intermediate/19_modules_packages.md`
- `intermediate/19_modules_packages.py`
```

---

## Issue 8: Add unit tests

**Title:** `[Feature] Add unit tests for all code examples`

**Labels:** `enhancement`, `help wanted`

**Body:**
```
Add a `tests/` directory with pytest tests for all `.py` example files. This ensures:

- Examples stay correct as Python evolves
- Contributors can verify they haven't broken anything
- Readers see how testing works in practice

Start with `test_basic_concepts.py` covering basic/ examples.
```

---

## Issue 9: README improvements

**Title:** `[Improvement] Make README more visually structured`

**Labels:** `documentation`, `good first issue`

**Body:**
```
The README is content-rich but could be more scannable. Suggestions:

- Add a quick-start section at the top
- Use a simpler table format for the topic list
- Add badges (Python version, license, contributors)
- Link to a CONTRIBUTING guide
```

---

## Issue 10: Add contributing / community files

**Title:** `[Feature] Add community files (already created in .github/)`

**Labels:** `enhancement`

**Body:**
```
The .github/ directory now has templates and a CONTRIBUTING guide. Next steps:

- Add a `SECURITY.md` for reporting vulnerabilities
- Add a `FUNDING.yml` if applicable
- Enable GitHub Discussions in the repo settings
```
