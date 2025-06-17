"""
Error and Exception handling demonstrations for Python 3.12.

This package contains modules demonstrating various aspects of Python
exception handling that are essential for real-world projects.
"""

from .basic_exceptions import demo_basic_exceptions
from .best_practices import demo_best_practices
from .context_managers import demo_context_managers
from .custom_exceptions import demo_custom_exceptions
from .exception_chaining import demo_exception_chaining
from .logging_exceptions import demo_logging_exceptions

__all__ = [
    "demo_error_exception",
    "demo_basic_exceptions",
    "demo_custom_exceptions",
    "demo_exception_chaining",
    "demo_context_managers",
    "demo_logging_exceptions",
    "demo_best_practices",
]


def demo_error_exception() -> None:
    """
    Comprehensive demonstration of exception handling in Python 3.12.

    This function runs all exception handling demos in sequence,
    covering basic patterns, custom exceptions, chaining, context
    managers, logging, and best practices.
    """
    print("=" * 60)
    print("EXCEPTION HANDLING DEMONSTRATIONS")
    print("=" * 60)

    # Run all demos with separators
    demo_basic_exceptions()
    print("\n" + "-" * 60 + "\n")

    demo_custom_exceptions()
    print("\n" + "-" * 60 + "\n")

    demo_exception_chaining()
    print("\n" + "-" * 60 + "\n")

    demo_context_managers()
    print("\n" + "-" * 60 + "\n")

    demo_logging_exceptions()
    print("\n" + "-" * 60 + "\n")

    demo_best_practices()
    print("\n" + "=" * 60)


__version__ = "1.0.0"
