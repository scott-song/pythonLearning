"""
Context managers for exception handling and resource management.

This module demonstrates how to use and create context managers for
proper resource cleanup and exception handling in Python 3.12.
"""

import contextlib
import logging
import tempfile
import time
from contextlib import ExitStack, contextmanager, suppress
from pathlib import Path
from typing import Any, Generator, Optional, Union


def demo_context_managers() -> None:
    """Demonstrate context manager usage for exception handling."""
    print("=== Context Managers ===\n")

    demo_file_context_managers()
    demo_exception_suppression()
    demo_custom_context_managers()
    demo_exit_stack()
    demo_contextlib_utilities()


def demo_file_context_managers() -> None:
    """Demonstrate file handling with context managers."""
    print("1. File context managers:")

    # Create a temporary file for demonstration
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write("Hello, World!\nThis is a test file.")
        temp_file_path = temp_file.name

    # Safe file reading with automatic cleanup
    try:
        with open(temp_file_path, "r") as file:
            content = file.read()
            print(f"File content: {content}")
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    finally:
        # Clean up temporary file
        Path(temp_file_path).unlink(missing_ok=True)

    # Demonstrate exception handling within context
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Handled exception: {e}")

    print()


def demo_exception_suppression() -> None:
    """Demonstrate exception suppression with contextlib.suppress."""
    print("2. Exception suppression:")

    # Suppress specific exceptions
    with suppress(FileNotFoundError):
        with open("missing_file.txt", "r") as file:
            content = file.read()
    print("FileNotFoundError was suppressed")

    # Suppress multiple exception types
    with suppress(ValueError, TypeError):
        result = int("not_a_number")
        print(f"Result: {result}")
    print("ValueError was suppressed")

    # Demonstrate what happens without suppression
    try:
        with suppress(KeyError):  # Wrong exception type
            result = int("not_a_number")  # This will raise ValueError
    except ValueError as e:
        print(f"ValueError not suppressed: {e}")

    print()


@contextmanager
def database_transaction() -> Generator[None, None, None]:
    """Custom context manager for database transaction simulation."""
    print("  Starting transaction...")
    try:
        yield
        print("  Committing transaction...")
    except Exception as e:
        print(f"  Rolling back transaction due to: {e}")
        raise
    finally:
        print("  Closing database connection...")


@contextmanager
def timing_context(operation_name: str) -> Generator[None, None, None]:
    """Context manager to time operations and handle exceptions."""
    start_time = time.time()
    print(f"Starting {operation_name}...")
    try:
        yield
    except Exception as e:
        print(f"{operation_name} failed with {type(e).__name__}: {e}")
        raise
    finally:
        end_time = time.time()
        duration = end_time - start_time
        print(f"{operation_name} completed in {duration:.3f} seconds")


def demo_custom_context_managers() -> None:
    """Demonstrate custom context managers."""
    print("3. Custom context managers:")

    # Successful transaction
    with database_transaction():
        print("  Performing database operations...")
        print("  Data inserted successfully")

    print()

    # Failed transaction
    try:
        with database_transaction():
            print("  Performing database operations...")
            raise ValueError("Database constraint violation")
    except ValueError:
        print("  Transaction was rolled back")

    print()

    # Timing successful operation
    with timing_context("Data processing"):
        time.sleep(0.1)  # Simulate work
        print("  Processing data...")

    print()

    # Timing failed operation
    try:
        with timing_context("Risky operation"):
            time.sleep(0.05)  # Simulate some work
            raise RuntimeError("Operation failed")
    except RuntimeError:
        print("  Operation was timed despite failure")

    print()


class ManagedResource:
    """Example resource that needs proper cleanup."""

    def __init__(self, name: str) -> None:
        """Initialize managed resource."""
        self.name = name
        self.is_open = False

    def open(self) -> None:
        """Open the resource."""
        print(f"Opening resource: {self.name}")
        self.is_open = True

    def close(self) -> None:
        """Close the resource."""
        print(f"Closing resource: {self.name}")
        self.is_open = False

    def use(self) -> str:
        """Use the resource."""
        if not self.is_open:
            raise RuntimeError(f"Resource {self.name} is not open")
        return f"Using {self.name}"


def demo_exit_stack() -> None:
    """Demonstrate ExitStack for managing multiple context managers."""
    print("4. ExitStack for multiple resources:")

    # Managing multiple resources with ExitStack
    try:
        with ExitStack() as stack:
            # Add multiple resources to the stack
            resource1 = stack.enter_context(ManagedResource("Database"))
            resource2 = stack.enter_context(ManagedResource("Cache"))
            resource3 = stack.enter_context(ManagedResource("FileSystem"))

            print(
                f"  Using resources: {resource1.name}, {resource2.name}, {resource3.name}"
            )

            # Simulate some work
            print("  Performing operations...")

            # Simulate an error
            raise ValueError("Something went wrong")

    except ValueError as e:
        print(f"  Caught exception: {e}")
        print("  All resources were properly cleaned up")

    print()


@contextmanager
def error_handler(
    error_message: str, reraise: bool = True, log_errors: bool = True
) -> Generator[None, None, None]:
    """Context manager for centralized error handling."""
    try:
        yield
    except Exception as e:
        if log_errors:
            print(f"  ERROR: {error_message} - {type(e).__name__}: {e}")

        if reraise:
            raise
        else:
            print(f"  Exception suppressed: {e}")


def demo_contextlib_utilities() -> None:
    """Demonstrate contextlib utilities."""
    print("5. Contextlib utilities:")

    # Closing context manager
    class CustomResource:
        def __init__(self, name: str) -> None:
            self.name = name
            print(f"  Created resource: {name}")

        def close(self) -> None:
            print(f"  Closed resource: {self.name}")

    with contextlib.closing(CustomResource("Network Connection")) as resource:
        print(f"  Using resource: {resource.name}")

    print()

    # Redirect stdout context manager
    import io
    from contextlib import redirect_stdout

    output_buffer = io.StringIO()
    with redirect_stdout(output_buffer):
        print("This goes to the buffer")
        print("So does this")

    captured_output = output_buffer.getvalue()
    print(f"Captured output: {repr(captured_output)}")

    print()

    # Error handling context manager
    with error_handler("Processing user data", reraise=False):
        data = {"name": "Alice"}
        age = data["age"]  # This will raise KeyError
        print(f"User age: {age}")

    print("Execution continued after suppressed exception")
    print()


@contextmanager
def temporary_state_change(
    obj: Any, attribute: str, new_value: Any
) -> Generator[Any, None, None]:
    """Context manager to temporarily change object state."""
    old_value = getattr(obj, attribute)
    setattr(obj, attribute, new_value)
    try:
        yield old_value
    finally:
        setattr(obj, attribute, old_value)


def demo_temporary_state() -> None:
    """Demonstrate temporary state changes with context managers."""
    print("6. Temporary state changes:")

    class Settings:
        def __init__(self) -> None:
            self.debug = False
            self.log_level = "INFO"

    settings = Settings()
    print(f"Initial debug mode: {settings.debug}")

    with temporary_state_change(settings, "debug", True):
        print(f"Temporary debug mode: {settings.debug}")
        # Simulate some debug operations
        print("  Running in debug mode...")

    print(f"Debug mode restored: {settings.debug}")
    print()


if __name__ == "__main__":
    demo_context_managers()
