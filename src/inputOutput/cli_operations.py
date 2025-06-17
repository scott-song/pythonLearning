"""Command line interface operations and argument parsing."""

import sys


def demo_command_line_args() -> None:
    """Demonstrate command line argument handling."""
    print("\n--- Command Line Arguments ---")

    # Print the name of the script (first argument in sys.argv)
    # sys.argv[0] contains the script name if arguments exist, otherwise use 'N/A'
    print(f"Script name: {sys.argv[0] if sys.argv else 'N/A'}")
    print(f"Number of arguments: {len(sys.argv) - 1}")
    print(f"Arguments: {sys.argv[1:] if len(sys.argv) > 1 else 'None'}")

    # Demonstrate basic argument parsing
    if len(sys.argv) > 1:
        print("Processing arguments:")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"  Argument {i}: {arg}")
    else:
        print("No arguments provided")

    # Example of simple flag handling
    print("Example flag handling:")
    print("  --verbose: Enable verbose output")
    print("  --help: Show help message")
    print("  --version: Show version information")

    # Simulate processing some common flags
    if "--verbose" in sys.argv:
        print("Verbose mode enabled")
    if "--help" in sys.argv:
        print("Help requested")
    if "--version" in sys.argv:
        print("Version 1.0.0")
