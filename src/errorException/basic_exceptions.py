"""
Basic exception handling demonstrations.

This module covers fundamental exception handling patterns that every
Python developer should know for real-world projects.
"""

import sys
from typing import Any, Optional


def demo_basic_exceptions() -> None:
    """Demonstrate basic exception handling patterns."""
    print("=== Basic Exception Handling ===\n")

    demo_try_except()
    demo_try_except_else()
    demo_try_except_finally()
    demo_multiple_exceptions()
    demo_exception_hierarchy()
    demo_raise_exceptions()
    demo_exception_context()


def demo_try_except() -> None:
    """Demonstrate basic try/except blocks."""
    print("1. Basic try/except:")

    try:
        result = 10 / 0
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    # Catching multiple specific exceptions
    try:
        value = int("not_a_number")
        print(f"Value: {value}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    print()


def demo_try_except_else() -> None:
    """Demonstrate try/except/else pattern."""
    print("2. try/except/else:")

    def safe_divide(a: float, b: float) -> Optional[float]:
        try:
            result = a / b  # Store result before returning
        except ZeroDivisionError:
            print("Error: Division by zero")
            return None
        else:
            # else clause executes when no exception occurs in try block
            print("Division successful")
            return result

    result1 = safe_divide(10, 2)
    print(f"10 / 2 = {result1}")

    result2 = safe_divide(10, 0)
    print(f"10 / 0 = {result2}")

    print()


def demo_try_except_finally() -> None:
    """Demonstrate try/except/finally pattern."""
    print("3. try/except/finally:")

    def process_file(filename: str) -> None:
        file_handle = None
        try:
            file_handle = open(filename, "r")
            content = file_handle.read()
            print(f"File content length: {len(content)}")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
        except PermissionError:
            print(f"Error: Permission denied for '{filename}'")
        finally:
            if file_handle:
                file_handle.close()
                print("File closed")
            else:
                print("No file to close")

    process_file("nonexistent_file.txt")
    print()


def demo_multiple_exceptions() -> None:
    """Demonstrate handling multiple exceptions."""
    print("4. Multiple exception handling:")

    def risky_operation(data: Any) -> None:
        try:
            # Multiple potential failure points
            first_item = data[0]
            numeric_value = int(first_item)
            result = 100 / numeric_value
            print(f"Result: {result}")
        except TypeError:
            print("Error: Data type not supported")
        except IndexError:
            print("Error: Data is empty")
        except ValueError:
            print("Error: Cannot convert to integer")
        except ZeroDivisionError:
            print("Error: Division by zero")
        except Exception as e:
            print(f"Unexpected error: {type(e).__name__}: {e}")

    risky_operation([])  # IndexError
    risky_operation(["0"])  # ZeroDivisionError
    risky_operation(["abc"])  # ValueError
    risky_operation(None)  # TypeError
    risky_operation(["5"])  # Success

    print()


def demo_exception_hierarchy() -> None:
    """Demonstrate Python's exception hierarchy."""
    print("5. Exception hierarchy:")

    def show_exception_info(exception: Exception) -> None:
        print(f"Exception: {exception}")
        print(f"Type: {type(exception).__name__}")
        # Print the Method Resolution Order (MRO) - shows inheritance chain
        # type(exception).__mro__ gets the class hierarchy from most specific to most general
        # We extract just the class names using a list comprehension
        print(f"MRO: {[cls.__name__ for cls in type(exception).__mro__]}")
        print()

    exceptions = [
        ValueError("Invalid value"),
        TypeError("Type mismatch"),
        FileNotFoundError("File not found"),
        KeyError("Key missing"),
        IndexError("Index out of range"),
    ]

    for exc in exceptions:
        show_exception_info(exc)


def demo_raise_exceptions() -> None:
    """Demonstrate raising exceptions."""
    print("6. Raising exceptions:")

    def validate_age(age: Any) -> None:
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age seems unrealistic")
        print(f"Valid age: {age}")

    test_ages = [25, -5, 200, "thirty", 45]

    for age in test_ages:
        try:
            validate_age(age)
        except (TypeError, ValueError) as e:
            print(f"Validation error for {age}: {e}")

    print()


def demo_exception_context() -> None:
    """Demonstrate exception context and traceback."""
    print("7. Exception context:")

    def inner_function() -> None:
        raise ValueError("Something went wrong in inner function")

    def middle_function() -> None:
        try:
            inner_function()
        except ValueError:
            print("Caught in middle function, re-raising...")
            raise

    def outer_function() -> None:
        try:
            middle_function()
        except ValueError as e:
            print(f"Caught in outer function: {e}")
            print(f"Exception info: {sys.exc_info()}")

    outer_function()
    print()


if __name__ == "__main__":
    demo_basic_exceptions()
