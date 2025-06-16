"""Text utilities for the Python Learning project."""


def demo_text() -> None:
    """Demo function for text/string examples."""
    print("demo_text - String examples")

    # String operations
    text = "Hello, World!"
    print(f"Original: {text}")
    print(f"Upper: {text.upper()}")
    print(f"Lower: {text.lower()}")

    # String formatting
    name = "Python"
    version = 3.12
    print(f"Welcome to {name} {version}!")

    # String methods
    words = text.split(", ")
    print(f"Split words: {words}")

    # Example: Working with strings
    message = "Hello, Python Learning!"
    print(f"Message: {message}")
    print(f"Message length: {len(message)}")
    print(f"Uppercase: {message.upper()}")
    print(f"Words: {message.split()}")

    text = "it does'nt"
    print(text)
    text = "first line. \nSecond line. \nThird line."
    print(text)
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
    text = "python"
    print(f"text: {text}")
    print(f"text[0]: {text[0]}")
    print(f"text[2:5]: {text[2:5]}")
    print(f"text[:2]: {text[:2]}")
    print(f"text[2:]: {text[2:]}")
    print(f"text[-2:]: {text[-2:]}")
    print(f"text[:-2]: {text[:-2]}")
    print(f"text[::2]: {text[::2]}")
    print(f"text[::-1]: {text[::-1]}")
    print(text.upper())
    # replace it to create a new str, not modify the original one
    print(text.replace("python", "java"))
    name = "John"
    age = 30
    print(f"name: {name}, age: {age}")
    print("hello, {}".format(name))
    print(f"hello, {name}, you are {age} years old".format(name=name, age=age))
