def demo_lambda():
    """Demo function for lambda examples."""
    print("demo_lambda - Lambda function examples")

    # Simple lambda (inline usage)
    print(f"Square of 5: {(lambda x: x**2)(5)}")

    # Lambda with map
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(f"Squared numbers: {squared}")

    # Lambda with filter
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
