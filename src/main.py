#!/usr/bin/env python3
"""Main entry point for the Python Learning project."""

import os
import sys

from dotenv import load_dotenv

from classes import demo_classes
from concurrency import demo_concurrency
from errorException import demo_error_exception

# Load environment variables
load_dotenv()


def main() -> None:
    """Run the main application."""
    print("Welcome to your Python Learning Project!")
    print("=" * 40)

    # Example: Using environment variables
    debug_mode = os.getenv("DEBUG", "False").lower() == "true"
    environment = os.getenv("ENVIRONMENT", "development")

    print(f"Debug mode: {debug_mode}")
    print(f"Environment: {environment}")
    print()

    # Add your code here
    demo_function()


def demo_function() -> None:
    """Demonstrate various Python features."""
    # Demonstrate exception handling
    demo_error_exception()

    # Demonstrate class features
    # demo_classes()

    # Demonstrate concurrency features
    demo_concurrency()


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("SYSTEM INFORMATION")
    print("=" * 50)
    print(f"Built-in modules: {len(sys.builtin_module_names)} modules")
    print(f"Python path entries: {len(sys.path)} paths")
    print(f"Python version: {sys.version}")
    main()
