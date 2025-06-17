#!/usr/bin/env python3
"""Main entry point for the Python Learning project."""

import os
import sys

from dotenv import load_dotenv

from inputOutput import demo_input_output

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
    """Show basic Python functionality."""
    demo_input_output()


if __name__ == "__main__":
    main()
    print(sys.builtin_module_names)
    print(sys.path)
