"""
Iterators and generators demonstrations for Python 3.12.

This module demonstrates:
- Custom iterators with __iter__ and __next__
- Generators with yield
- Generator expressions
- Iterator protocol
- Built-in itertools usage
"""

import itertools
from typing import Generator, Iterator


class CountDown:
    """Custom iterator that counts down from a number."""

    def __init__(self, start: int) -> None:
        """Initialize countdown with starting number."""
        self.start = start

    def __iter__(self) -> Iterator[int]:
        """Return iterator object."""
        return self

    def __next__(self) -> int:
        """Return next value in countdown."""
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1


class NumberRange:
    """Custom range iterator."""

    def __init__(self, start: int, end: int, step: int = 1) -> None:
        """Initialize range with start, end, and step."""
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self) -> Iterator[int]:
        """Return iterator object."""
        return self

    def __next__(self) -> int:
        """Return next value in range."""
        if (self.step > 0 and self.current >= self.end) or (
            self.step < 0 and self.current <= self.end
        ):
            raise StopIteration

        value = self.current
        self.current += self.step
        return value


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """Generate Fibonacci sequence up to n numbers."""
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def infinite_counter(start: int = 0) -> Generator[int, None, None]:
    """Generate infinite sequence of numbers."""
    current = start
    while True:
        yield current
        current += 1


def squares_generator(n: int) -> Generator[int, None, None]:
    """Generate squares of numbers from 0 to n-1."""
    for i in range(n):
        yield i * i


def demo_iterators_generators() -> None:
    """Demonstrate iterators and generators."""
    print("\n" + "=" * 50)
    print("ITERATORS AND GENERATORS DEMONSTRATION")
    print("=" * 50)

    demo_custom_iterators()
    demo_generators()
    demo_generator_expressions()
    demo_itertools_usage()


def demo_custom_iterators() -> None:
    """Demonstrate custom iterator classes."""
    print("\n1. Custom Iterators:")
    print("-" * 19)

    # CountDown iterator
    print("CountDown from 5:")
    countdown = CountDown(5)
    for num in countdown:
        print(f"  {num}")

    # NumberRange iterator
    print("\nNumberRange(1, 10, 2):")
    for num in NumberRange(1, 10, 2):
        print(f"  {num}")

    # Manual iteration
    print("\nManual iteration:")
    range_iter = NumberRange(0, 5)
    iterator = iter(range_iter)

    try:
        while True:
            value = next(iterator)
            print(f"  Next value: {value}")
    except StopIteration:
        print("  Iterator exhausted")


def demo_generators() -> None:
    """Demonstrate generator functions."""
    print("\n2. Generator Functions:")
    print("-" * 21)

    # Fibonacci generator
    print("Fibonacci sequence (first 10):")
    fib_gen = fibonacci_generator(10)
    for num in fib_gen:
        print(f"  {num}")

    # Squares generator
    print("\nSquares of 0-6:")
    for square in squares_generator(7):
        print(f"  {square}")

    # Infinite counter (limited output)
    print("\nInfinite counter (first 5):")
    counter = infinite_counter(10)
    for i, num in enumerate(counter):
        if i >= 5:
            break
        print(f"  {num}")


def demo_generator_expressions() -> None:
    """Demonstrate generator expressions."""
    print("\n3. Generator Expressions:")
    print("-" * 23)

    # Basic generator expression
    squares = (x**2 for x in range(10))
    print("Squares generator expression:")
    print(f"  First 5 squares: {list(itertools.islice(squares, 5))}")

    # Generator with condition
    even_squares = (x**2 for x in range(10) if x % 2 == 0)
    print(f"  Even squares: {list(even_squares)}")

    # Memory efficiency demonstration
    data = list(range(1000000))

    # List comprehension (uses more memory)
    print("\nMemory efficiency:")
    print("  List comprehension creates full list in memory")

    # Generator expression (memory efficient)
    large_gen = (x * 2 for x in data if x % 1000 == 0)
    print("  Generator expression: lazy evaluation")
    print(f"  First 3 values: {list(itertools.islice(large_gen, 3))}")


def demo_itertools_usage() -> None:
    """Demonstrate itertools module."""
    print("\n4. Itertools Usage:")
    print("-" * 17)

    # count() - infinite counter
    print("itertools.count(10, 3) - first 5:")
    counter = itertools.count(10, 3)
    print(f"  {list(itertools.islice(counter, 5))}")

    # cycle() - infinite cycle
    print("\nitertools.cycle(['A', 'B', 'C']) - first 8:")
    cycler = itertools.cycle(["A", "B", "C"])
    print(f"  {list(itertools.islice(cycler, 8))}")

    # chain() - flatten iterables
    print("\nitertools.chain([1,2], [3,4], [5,6]):")
    chained = itertools.chain([1, 2], [3, 4], [5, 6])
    print(f"  {list(chained)}")

    # combinations() - combinations
    print("\nitertools.combinations('ABCD', 2):")
    combos = itertools.combinations("ABCD", 2)
    print(f"  {list(combos)}")

    # permutations() - permutations
    print("\nitertools.permutations('ABC', 2):")
    perms = itertools.permutations("ABC", 2)
    print(f"  {list(perms)}")

    # groupby() - group consecutive elements
    print("\nitertools.groupby([1,1,2,2,2,3,1,1]):")
    data = [1, 1, 2, 2, 2, 3, 1, 1]
    for key, group in itertools.groupby(data):
        print(f"  {key}: {list(group)}")
