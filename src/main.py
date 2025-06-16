#!/usr/bin/env python3
"""
Main entry point for the Python Learning project.
"""

import os

from dotenv import load_dotenv

from flow import demo_flow
from function import demo_func
from lamb import demo_lambda
from list import demo_list
from text import demo_text

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
    demo_text()
    demo_list()
    demo_flow()
    print("demo_func")
    demo_func()
    demo_lambda()


if __name__ == "__main__":
    main()
