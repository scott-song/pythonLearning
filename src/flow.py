from enum import Enum


def demo_flow():
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


def demo_flow_if():
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


def demo_flow_for():
    """Demo function for for loops."""
    print("demo_flow_for")
    words = ["cat", "window", "defenestrate"]
    for w in words:
        print(w, len(w))


def demo_flow_range():
    """Demo function for range() usage."""
    print("demo_flow_range")

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

    # Converting range to list
    print("\nConverting range to list:")
    numbers = list(range(3, 15, 3))
    print(numbers)

    # Using range with len() for indexing
    print("\nUsing range with len() for indexing:")
    fruits = ["apple", "banana", "cherry", "date"]
    for i in range(len(fruits)):
        print(f"Index {i}: {fruits[i]}")
    # for break
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(f"{n} equals {x} * {n//x}")
                break
        else:
            print(f"{n} is a prime number")

    # for continue
    for n in range(2, 10):
        if n % 2 == 0:
            print(f"{n} is even")
            continue
        print(f"{n} is odd")


# match test
def http_error(status):
    match status:
        case 400:
            return "bad request"
        case 400:
            return "not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "not allowed"
        case _:
            return "something's wrong with the internet"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def where_is(self):
        match self:
            case Point(x=0, y=0):
                print("origin")
            case Point(x=0, y=y):
                print(f"Y={y}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point(x=x, y=y) if x == y:
                print(f"X={x}, Y={y} is on the line x=y")
            case Point(x=x, y=y):
                print(f"X={x}, Y={y}")
            case _:
                raise ValueError("Not a point!!")


class Color(Enum):
    """Enum for colors."""
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


def print_color(color: Color):
    """Print the color."""
    print(color)


def fib(n):
    """Fibonacci sequence generator."""
    print("Fibonacci sequence:")
    a, b = 0, 1
    while a < n:
        print(a, end="   ")
        a, b = b, a + b
    print()


def fib2(n):
    """Fibonacci sequence generator."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
