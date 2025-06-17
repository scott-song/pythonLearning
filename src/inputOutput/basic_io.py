"""Basic input/output operations and string formatting."""


def demo_basic_input() -> None:
    """Demonstrate basic input operations."""
    print("\n--- Basic Input Operations ---")

    # Simulated input for demonstration (normally you'd use input())
    print("Demo: Getting user input")
    print("# name = input('Enter your name: ')")
    print("# age = int(input('Enter your age: '))")

    # Example with validation
    print("\nDemo: Input validation")
    print("# while True:")
    print("#     try:")
    print("#         age = int(input('Enter a valid age: '))")
    print("#         break")
    print("#     except ValueError:")
    print("#         print('Please enter a valid number')")


def demo_string_formatting() -> None:
    """Demonstrate various string formatting techniques."""
    print("\n--- String Formatting ---")

    name = "Alice"
    age = 30
    height = 5.6

    # Old-style formatting
    print("Old style: Hello, my name is %s and I'm %d years old" % (name, age))

    # str.format() method
    print("str.format(): Hello, my name is {} and I'm {} years old".format(name, age))
    print(
        "Named placeholders: Hello, {name}! You are {age} years old".format(
            name=name, age=age
        )
    )

    # f-strings (Python 3.6+)
    print(f"f-string: Hello, my name is {name} and I'm {age} years old")
    print(f"With formatting: Height is {height:.1f} feet")
    print(f"With expressions: Next year I'll be {age + 1}")
