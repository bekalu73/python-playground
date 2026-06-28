# Magic Methods

> 📄 **Related code file:** [`13_magic_methods.py`](13_magic_methods.py)

## Overview

**Magic methods** (also called **dunder methods**, for "double underscore") are special methods Python calls automatically in response to language operations. They let your objects work with built-in syntax like `+`, `==`, `len()`, `print()`, indexing, and the `with` statement. This is the foundation of **operator overloading**.

## String Representation

Two methods control how your object appears as text:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):              # Human-readable (print, str())
        return f"Point({self.x}, {self.y})"

    def __repr__(self):             # Developer-friendly (repr, debugging, lists)
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)
print(p)         # Point(3, 4)        → uses __str__
print(repr(p))   # Point(x=3, y=4)    → uses __repr__
print([p])       # [Point(x=3, y=4)]  → containers use __repr__
```

> 💡 Rule of thumb: `__str__` for users, `__repr__` for developers. If you only write one, write `__repr__`.

## Arithmetic Operators

Overload math operators so your objects work with `+`, `-`, `*`, etc.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):       # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):       # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):      # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):     # 3 * v  (reflected)
        return self.__mul__(scalar)

    def __abs__(self):              # abs(v) — magnitude
        return (self.x**2 + self.y**2) ** 0.5
```

| Method | Operator |
|--------|----------|
| `__add__` | `+` |
| `__sub__` | `-` |
| `__mul__` | `*` |
| `__truediv__` | `/` |
| `__neg__` | unary `-` |
| `__abs__` | `abs()` |

> Return `NotImplemented` (not `None`) when an operation isn't supported, so Python can try the reflected operation.

## Comparison Operators

```python
class Student:
    def __init__(self, name, grade):
        self.name, self.grade = name, grade

    def __eq__(self, other):    # ==
        return self.grade == other.grade

    def __lt__(self, other):    # <
        return self.grade < other.grade

# Once defined, sorting just works:
students = [Student("Bob", 92), Student("Alice", 85)]
students.sort()   # uses __lt__
```

| Method | Operator |
|--------|----------|
| `__eq__` | `==` |
| `__ne__` | `!=` |
| `__lt__` | `<` |
| `__le__` | `<=` |
| `__gt__` | `>` |
| `__ge__` | `>=` |

> 💡 Use `@functools.total_ordering` to auto-generate the rest from `__eq__` and one ordering method.

## Container Operators

Make objects behave like lists or dictionaries:

```python
class CustomList:
    def __init__(self):
        self._items = []

    def __len__(self):              # len(obj)
        return len(self._items)

    def __getitem__(self, index):   # obj[index]
        return self._items[index]

    def __setitem__(self, index, value):  # obj[index] = value
        self._items[index] = value

    def __contains__(self, item):   # item in obj
        return item in self._items

    def __iter__(self):             # for item in obj
        return iter(self._items)
```

## Callable Objects

`__call__` makes an instance behave like a function:

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
double(5)         # 10 — called like a function!
callable(double)  # True
```

## Context Managers

`__enter__` and `__exit__` let objects work with the `with` statement:

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename, self.mode = filename, mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return False    # False propagates any exception

with FileManager("test.txt", "w") as f:
    f.write("Hello")
# File automatically closed
```

## Common Mistakes

❌ **Returning `None` instead of a new object** from arithmetic methods:
```python
def __add__(self, other):
    self.x += other.x    # Wrong — mutates and returns None
    # Right: return a new Vector(...)
```

❌ **Defining `__eq__` but not `__hash__`** — makes objects unhashable (can't use in sets/dict keys). Define both or use `@dataclass`.

❌ **Forgetting `isinstance` checks** — operating on incompatible types raises confusing errors.

❌ **Overusing operator overloading** — only overload when the operator's meaning is intuitive.

## Best Practices

✅ Always implement `__repr__`; add `__str__` if you need a friendly form.
✅ Return `NotImplemented` for unsupported operand types.
✅ Keep overloaded operators intuitive (`+` should "add", not do something surprising).
✅ Use `@dataclass` (or `@total_ordering`) to reduce boilerplate.
✅ Implement `__eq__` and `__hash__` together.

## Exercises

1. **Money class:** Create a `Money` class with `__add__`, `__str__`, and `__eq__` so you can add amounts and compare them.

2. **Temperature:** Make a `Temperature` class supporting `<`, `==`, and `>` comparisons by Celsius value.

3. **Stack container:** Build a `Stack` supporting `len()`, `in`, and iteration via magic methods.

4. **Timer context manager:** Create a context manager that prints how long the `with` block took (use `__enter__`/`__exit__`).

<details>
<summary>💡 Solution hints</summary>

```python
class Money:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return Money(self.amount + other.amount)
    def __eq__(self, other):
        return self.amount == other.amount
    def __str__(self):
        return f"${self.amount:.2f}"
```
</details>

## Key Takeaways

- Magic (dunder) methods hook into Python's built-in syntax.
- `__str__`/`__repr__` for representation, `__add__` etc. for arithmetic, `__eq__`/`__lt__` for comparison.
- `__len__`, `__getitem__`, `__iter__`, `__contains__` make container-like objects.
- `__call__` makes objects callable; `__enter__`/`__exit__` make context managers.

---

▶️ **Run the examples:** `python advanced/13_magic_methods.py`
⏮️ **Previous:** [OOP Principles](12_oop_principles.md) | ⏭️ **Next:** [Generators & Iteration →](14_generators_iteration.md)
