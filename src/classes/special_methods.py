"""
Special methods (magic methods) demonstrations for Python 3.12.

This module demonstrates special methods including:
- String representation methods (__str__, __repr__)
- Comparison operators (__eq__, __lt__, etc.)
- Arithmetic operators (__add__, __sub__, etc.)
- Container methods (__len__, __getitem__, etc.)
- Context managers (__enter__, __exit__)
- Callable objects (__call__)
"""

from typing import Any, Iterator, Optional, Union


class Vector:
    """A 2D vector class demonstrating arithmetic operations."""

    def __init__(self, x: float, y: float) -> None:
        """Initialize vector with x and y components."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """String representation for end users."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        """String representation for developers."""
        return f"Vector(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        """Check equality between vectors."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Vector") -> "Vector":
        """Add two vectors."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        """Subtract two vectors."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: Union[int, float]) -> "Vector":
        """Multiply vector by scalar."""
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: Union[int, float]) -> "Vector":
        """Right multiplication (scalar * vector)."""
        return self.__mul__(scalar)

    def __truediv__(self, scalar: Union[int, float]) -> "Vector":
        """Divide vector by scalar."""
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(self.x / scalar, self.y / scalar)

    def __abs__(self) -> float:
        """Calculate magnitude of vector."""
        return (self.x**2 + self.y**2) ** 0.5

    def __neg__(self) -> "Vector":
        """Negate vector."""
        return Vector(-self.x, -self.y)

    def __bool__(self) -> bool:
        """Check if vector is non-zero."""
        return abs(self) != 0

    def dot(self, other: "Vector") -> float:
        """Calculate dot product."""
        return self.x * other.x + self.y * other.y


class Money:
    """A money class demonstrating comparison operators."""

    def __init__(self, amount: float, currency: str = "USD") -> None:
        """Initialize money with amount and currency."""
        self.amount = round(amount, 2)
        self.currency = currency

    def __str__(self) -> str:
        """String representation of money."""
        return f"{self.currency} {self.amount:.2f}"

    def __repr__(self) -> str:
        """Developer representation of money."""
        return f"Money({self.amount}, '{self.currency}')"

    def __eq__(self, other: object) -> bool:
        """Check equality."""
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other: "Money") -> bool:
        """Less than comparison."""
        self._check_currency(other)
        return self.amount < other.amount

    def __le__(self, other: "Money") -> bool:
        """Less than or equal comparison."""
        return self == other or self < other

    def __gt__(self, other: "Money") -> bool:
        """Greater than comparison."""
        self._check_currency(other)
        return self.amount > other.amount

    def __ge__(self, other: "Money") -> bool:
        """Greater than or equal comparison."""
        return self == other or self > other

    def __add__(self, other: "Money") -> "Money":
        """Add money amounts."""
        self._check_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: "Money") -> "Money":
        """Subtract money amounts."""
        self._check_currency(other)
        return Money(self.amount - other.amount, self.currency)

    def __hash__(self) -> int:
        """Make Money hashable for use in sets/dicts."""
        return hash((self.amount, self.currency))

    def _check_currency(self, other: "Money") -> None:
        """Check if currencies match."""
        if self.currency != other.currency:
            raise ValueError(f"Cannot operate on {self.currency} and {other.currency}")


class CustomList:
    """A custom list implementation demonstrating container methods."""

    def __init__(self, items: Optional[list] = None) -> None:
        """Initialize custom list."""
        self._items = items or []

    def __len__(self) -> int:
        """Return length of list."""
        return len(self._items)

    def __getitem__(self, index: int) -> Any:
        """Get item by index."""
        return self._items[index]

    def __setitem__(self, index: int, value: Any) -> None:
        """Set item by index."""
        self._items[index] = value

    def __delitem__(self, index: int) -> None:
        """Delete item by index."""
        del self._items[index]

    def __contains__(self, item: Any) -> bool:
        """Check if item is in list."""
        return item in self._items

    def __iter__(self) -> Iterator[Any]:
        """Return iterator over items."""
        return iter(self._items)

    def __str__(self) -> str:
        """String representation."""
        return f"CustomList({self._items})"

    def append(self, item: Any) -> None:
        """Add item to end of list."""
        self._items.append(item)

    def extend(self, items: list) -> None:
        """Extend list with multiple items."""
        self._items.extend(items)


class FileManager:
    """Context manager for file operations."""

    def __init__(self, filename: str, mode: str = "r") -> None:
        """Initialize file manager."""
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Enter context manager."""
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager."""
        if self.file:
            print(f"Closing file {self.filename}")
            self.file.close()

        # Return False to propagate exceptions
        return False


class Calculator:
    """A callable class that acts like a function."""

    def __init__(self, operation: str = "add") -> None:
        """Initialize calculator with operation."""
        self.operation = operation
        self.history = []

    def __call__(self, a: float, b: float) -> float:
        """Make the object callable."""
        if self.operation == "add":
            result = a + b
        elif self.operation == "subtract":
            result = a - b
        elif self.operation == "multiply":
            result = a * b
        elif self.operation == "divide":
            if b == 0:
                raise ValueError("Cannot divide by zero")
            result = a / b
        else:
            raise ValueError(f"Unknown operation: {self.operation}")

        self.history.append(f"{a} {self.operation} {b} = {result}")
        return result

    def get_history(self) -> list:
        """Get calculation history."""
        return self.history.copy()


def demo_special_methods() -> None:
    """Demonstrate special methods and magic methods."""
    print("\n" + "=" * 50)
    print("SPECIAL METHODS DEMONSTRATION")
    print("=" * 50)

    demo_string_representation()
    demo_arithmetic_operators()
    demo_comparison_operators()
    demo_container_methods()
    demo_context_managers()
    demo_callable_objects()


def demo_string_representation() -> None:
    """Demonstrate __str__ and __repr__ methods."""
    print("\n1. String Representation Methods:")
    print("-" * 33)

    v1 = Vector(3.0, 4.0)
    print(f"str(v1): {str(v1)}")
    print(f"repr(v1): {repr(v1)}")

    # repr() is used in containers
    vectors = [Vector(1, 2), Vector(3, 4)]
    print(f"List of vectors: {vectors}")


def demo_arithmetic_operators() -> None:
    """Demonstrate arithmetic operator overloading."""
    print("\n2. Arithmetic Operators:")
    print("-" * 24)

    v1 = Vector(3.0, 4.0)
    v2 = Vector(1.0, 2.0)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v1 = {3 * v1}")
    print(f"v1 / 2 = {v1 / 2}")
    print(f"|v1| = {abs(v1)}")
    print(f"-v1 = {-v1}")
    print(f"bool(v1) = {bool(v1)}")
    print(f"bool(Vector(0, 0)) = {bool(Vector(0, 0))}")
    print(f"v1 · v2 = {v1.dot(v2)}")


def demo_comparison_operators() -> None:
    """Demonstrate comparison operator overloading."""
    print("\n3. Comparison Operators:")
    print("-" * 24)

    money1 = Money(100.50)
    money2 = Money(75.25)
    money3 = Money(100.50)

    print(f"money1 = {money1}")
    print(f"money2 = {money2}")
    print(f"money3 = {money3}")

    print(f"money1 == money3: {money1 == money3}")
    print(f"money1 > money2: {money1 > money2}")
    print(f"money2 < money1: {money2 < money1}")
    print(f"money1 >= money3: {money1 >= money3}")

    # Arithmetic with money
    print(f"money1 + money2 = {money1 + money2}")
    print(f"money1 - money2 = {money1 - money2}")

    # Using in sets (requires __hash__)
    money_set = {money1, money2, money3}
    print(f"Unique money values: {money_set}")


def demo_container_methods() -> None:
    """Demonstrate container protocol methods."""
    print("\n4. Container Methods:")
    print("-" * 19)

    custom_list = CustomList([1, 2, 3, 4, 5])

    print(f"custom_list = {custom_list}")
    print(f"len(custom_list) = {len(custom_list)}")
    print(f"custom_list[2] = {custom_list[2]}")
    print(f"3 in custom_list: {3 in custom_list}")
    print(f"10 in custom_list: {10 in custom_list}")

    # Modify list
    custom_list[0] = 100
    custom_list.append(6)
    print(f"After modifications: {custom_list}")

    # Iterate over list
    print("Iterating over custom_list:")
    for item in custom_list:
        print(f"  {item}")


def demo_context_managers() -> None:
    """Demonstrate context manager protocol."""
    print("\n5. Context Managers:")
    print("-" * 19)

    # Create a temporary file for demonstration
    import os
    import tempfile

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write("Hello, World!")
        temp_filename = temp_file.name

    try:
        # Use custom context manager
        print("Using custom FileManager context manager:")
        with FileManager(temp_filename, "r") as file:
            content = file.read()
            print(f"File content: {content}")

        print("File operations completed")

    finally:
        # Clean up temporary file
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)


def demo_callable_objects() -> None:
    """Demonstrate callable objects using __call__."""
    print("\n6. Callable Objects:")
    print("-" * 18)

    # Create calculator instances
    adder = Calculator("add")
    multiplier = Calculator("multiply")

    # Use them like functions
    print(f"adder(5, 3) = {adder(5, 3)}")
    print(f"adder(10, 7) = {adder(10, 7)}")
    print(f"multiplier(4, 6) = {multiplier(4, 6)}")

    # Check if objects are callable
    print(f"callable(adder): {callable(adder)}")
    print(f"callable(5): {callable(5)}")

    # Show calculation history
    print("Adder history:")
    for calculation in adder.get_history():
        print(f"  {calculation}")
