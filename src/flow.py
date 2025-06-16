from enum import Enum
from typing import List


def demo_flow() -> None:
    """Demo function for control flow examples."""
    print("demo_flow - Control flow examples")

    # If-else example
    x = 10
    if x > 5:
        print(f"{x} is greater than 5")
    else:
        print(f"{x} is not greater than 5")

    # For loop example
    for i in range(3):
        print(f"Loop iteration: {i}")

    demo_flow_if()
    demo_flow_for()
    demo_flow_range()
    print(http_error(401))
    Point(0, 0).where_is()
    Point(0, 1).where_is()
    Point(1, 0).where_is()
    Point(1, 1).where_is()
    Point(1, 2).where_is()
    Point(2, 1).where_is()
    print_color(Color.RED)
    print_color(Color.GREEN)
    print_color(Color.BLUE)
    fib(1000000)
    print(fib2(1000000))


def demo_flow_if() -> None:
    """Demo function for if statements and control flow."""
    print("demo_flow_if")
    x = -1
    if x < 0:
        x = 0
        print("Negative changed to zero")
    elif x == 0:
        print("Zero")
    elif x == 1:
        print("Single")
    else:
        print("More")


def demo_flow_for() -> None:
    """Demo function for for loops."""
    print("demo_flow_for")
    words = ["cat", "window", "defenestrate"]
    for w in words:
        print(w, len(w))


def demo_flow_range() -> None:
    """Demo function for range() usage."""
    print("demo_flow_range")
    _demo_basic_ranges()
    _demo_range_with_lists()
    _demo_break_continue()


def _demo_basic_ranges() -> None:
    """Demonstrate basic range usage patterns."""
    # Basic range - from 0 to 4
    print("\nBasic range(5):")
    for i in range(5):
        print(i, end=" ")
    print()

    # Range with start and stop - from 2 to 7
    print("\nRange with start and stop - range(2, 8):")
    for i in range(2, 8):
        print(i, end=" ")
    print()

    # Range with step - from 0 to 9 with step 2
    print("\nRange with step - range(0, 10, 2):")
    for i in range(0, 10, 2):
        print(i, end=" ")
    print()

    # Negative step - countdown from 10 to 1
    print("\nNegative step - range(10, 0, -1):")
    for i in range(10, 0, -1):
        print(i, end=" ")
    print()


def _demo_range_with_lists() -> None:
    """Demonstrate range usage with lists."""
    # Converting range to list
    print("\nConverting range to list:")
    numbers = list(range(3, 15, 3))
    print(numbers)

    # Using range with len() for indexing
    print("\nUsing range with len() for indexing:")
    fruits = ["apple", "banana", "cherry", "date"]
    for i in range(len(fruits)):
        print(f"Index {i}: {fruits[i]}")


def _demo_break_continue() -> None:
    """Demonstrate break and continue in loops."""
    # for break
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(f"{n} equals {x} * {n // x}")
                break
        else:
            print(f"{n} is a prime number")

    # for continue
    for n in range(2, 10):
        if n % 2 == 0:
            print(f"{n} is even")
            continue
        print(f"{n} is odd")


# HTTP error handling with if-elif
def http_error(status: int) -> str:
    """Handle HTTP error status codes."""
    if status == 400:
        return "bad request"
    elif status == 404:
        return "not found"
    elif status == 418:
        return "I'm a teapot"
    elif status in (401, 403):
        return "not allowed"
    else:
        return "something's wrong with the internet"


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other: "Point") -> "Point":
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: "Point") -> "Point":
        return Point(self.x / other.x, self.y / other.y)

    def where_is(self) -> None:
        """Determine where the point is located."""
        if self.x == 0 and self.y == 0:
            print("origin")
        elif self.x == 0:
            print(f"Y={self.y}")
        elif self.y == 0:
            print(f"X={self.x}")
        elif self.x == self.y:
            print(f"X={self.x}, Y={self.y} is on the line x=y")
        else:
            print(f"X={self.x}, Y={self.y}")


class Color(Enum):
    """Enum for colors."""

    RED = "red"
    GREEN = "green"
    BLUE = "blue"


def print_color(color: Color) -> None:
    """Print the color."""
    print(color)


def fib(n: int) -> None:
    """Fibonacci sequence generator."""
    print("Fibonacci sequence:")
    a, b = 0, 1
    while a < n:
        print(a, end="   ")
        a, b = b, a + b
    print()


def fib2(n: int) -> List[int]:
    """Fibonacci sequence generator."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
