#!/usr/bin/env python3
"""
Main entry point for the Python Learning project.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def main():
    """Main function to run the application."""
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


def demo_function():
    """A demo function to show basic Python functionality."""
    print("This is a demo function!")

    # Example: Working with lists
    fruits = ["apple", "banana", "orange", "grape"]
    print(f"Fruits: {fruits}")

    # Example: List comprehension
    fruit_lengths = [len(fruit) for fruit in fruits]
    print(f"Fruit lengths: {fruit_lengths}")

    # Example: Dictionary
    fruit_info = {fruit: len(fruit) for fruit in fruits}
    print(f"Fruit info: {fruit_info}")


if __name__ == "__main__":
    main()
