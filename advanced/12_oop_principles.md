# OOP Principles

> 📄 **Related code file:** [`12_oop_principles.py`](12_oop_principles.py)

## Overview

Building on [OOP Fundamentals](../intermediate/11_oop_fundamentals.md), this lesson covers the three pillars of object-oriented programming: **inheritance**, **encapsulation**, and **polymorphism** — plus multiple inheritance and the Method Resolution Order (MRO).

## Inheritance

**Inheritance** lets a class (child/subclass) reuse the attributes and methods of another class (parent/base class).

```python
class Animal:                       # Base class
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        return f"{self.name} is eating"

    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):                  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name, "Canine")   # Call parent constructor
        self.breed = breed

    def make_sound(self):           # Override the parent method
        return f"{self.name} barks: Woof!"

    def fetch(self):                # New method specific to Dog
        return f"{self.name} fetches the ball"
```

### Key concepts
- **`super()`** calls the parent class's methods (essential in `__init__`).
- **Method overriding** — a child redefines a parent method to change behavior.
- Children inherit all parent methods they don't override (`dog.eat()` works).

## Encapsulation

**Encapsulation** bundles data with the methods that operate on it, and controls access to internal details.

| Convention | Syntax | Meaning |
|------------|--------|---------|
| Public | `self.name` | Accessible everywhere |
| Protected | `self._balance` | "Internal" by convention (still accessible) |
| Private | `self.__pin` | Name-mangled to discourage access |

```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number  # Public
        self._balance = initial_balance       # Protected (convention)
        self.__pin = "1234"                   # Private (name mangling)

    def get_balance(self):                    # Controlled access
        return self._balance

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Invalid PIN"
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
        return f"Withdrew ${amount}"
```

> 🔒 Private attributes (`__pin`) are **name-mangled** to `_ClassName__pin`. This isn't true security — it just prevents accidental access and name clashes.

## Polymorphism

**Polymorphism** ("many forms") means different classes can share the same interface, so the same code works with different objects.

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14159 * self.r ** 2

# The same loop handles every shape type
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")
```

This is also called **duck typing**: "If it walks like a duck and quacks like a duck, it's a duck." Python cares that an object *has* the method, not what its class is.

## Multiple Inheritance & MRO

A class can inherit from more than one parent. **Mixins** are small classes that add a specific ability.

```python
class Flyable:
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming"

class Duck(Animal, Flyable, Swimmable):
    def make_sound(self):
        return f"{self.name} quacks: Quack!"

duck = Duck("Donald", "Avian")
duck.fly()    # from Flyable
duck.swim()   # from Swimmable
duck.eat()    # from Animal
```

### Method Resolution Order (MRO)
When multiple parents define the same method, Python uses the **MRO** to decide which runs first (left-to-right, depth considered):

```python
print(Duck.__mro__)
# Shows the order Python searches for methods
```

## Common Mistakes

❌ **Forgetting `super().__init__()`** — the parent's attributes never get set.

❌ **Thinking private (`__`) means secure** — it's only name-mangling.

❌ **Deep inheritance hierarchies** — favor composition for complex relationships.

❌ **Overriding without keeping the interface consistent** (different return types confuse callers).

## Best Practices

✅ Use `super()` to call parent methods (don't hard-code the parent name).
✅ Prefer **composition over inheritance** when "has-a" fits better than "is-a".
✅ Use mixins for reusable, optional abilities.
✅ Keep the public interface consistent across subclasses (so polymorphism works).
✅ Use `_protected` for internal attributes; reserve `__private` for avoiding name clashes.

## Exercises

1. **Vehicle hierarchy:** Create a base `Vehicle` with `start()` and `stop()`. Make `Car` and `Motorcycle` subclasses that override `start()` with a custom message.

2. **Encapsulated counter:** Build a class with a private `__count` that can only be changed through `increment()` and read through `get_count()`.

3. **Polymorphic shapes:** Add a `Triangle` to the `Shape` example and compute the total area of a list of mixed shapes.

4. **Mixin:** Create a `Loggable` mixin with a `log(message)` method and add it to one of your classes.

<details>
<summary>💡 Solution hints</summary>

```python
class Vehicle:
    def __init__(self, name):
        self.name = name
    def start(self):
        return f"{self.name} starting"

class Car(Vehicle):
    def start(self):
        return f"{self.name}: vroom (engine)"

class Motorcycle(Vehicle):
    def start(self):
        return f"{self.name}: braaap"
```
</details>

## Key Takeaways

- **Inheritance** reuses parent code; `super()` calls parent methods.
- **Encapsulation** controls access (`public`, `_protected`, `__private`).
- **Polymorphism** lets one interface work with many types (duck typing).
- **Multiple inheritance** uses the **MRO** (`__mro__`) to resolve methods.

---

▶️ **Run the examples:** `python advanced/12_oop_principles.py`
⏮️ **Previous:** [Intermediate: OOP Fundamentals](../intermediate/11_oop_fundamentals.md) | ⏭️ **Next:** [Magic Methods →](13_magic_methods.md)
