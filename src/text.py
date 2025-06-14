"""
Text utilities for the Python Learning project.
"""


def demo_text():
    """Demo function to show text processing."""
    print("This is a demo text function!")

    # Example: Working with strings
    message = "Hello, Python Learning!"
    print(f"Message: {message}")
    print(f"Message length: {len(message)}")
    print(f"Uppercase: {message.upper()}")
    print(f"Words: {message.split()}")

    test = "it does'nt"
    print(test)
    test = "first line. \nSecond line. \nThird line."
    print(test)
    print(r"C:\some\name")
    print(
        """\
        Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
        """
    )

    print("Py" + "thon")
    print("Py" * 3)
    print("Py" + "thon")
    print("Py" * 3)
