"""Function demonstrations and examples."""


def demo_func() -> None:
    """Demo function for function examples."""
    print("demo_func - Function examples")

    def greet(name: str) -> str:
        return f"Hello, {name}!"

    print(greet("World"))

    # Function with default parameter
    def power(base: int, exponent: int = 2) -> int:
        return int(base**exponent)

    print(f"2^3 = {power(2, 3)}")
    print(f"5^2 = {power(5)}")


def parrot(
    voltage: int,
    state: str = "a stiff",
    action: str = "voom",
    type: str = "Norwegian Blue",
) -> None:
    """Demonstrate function with multiple parameters and defaults."""
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def cheeseshop(kind: str, *arguments: str, **keywords: str) -> None:
    """Demonstrate function with *args and **kwargs."""
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


def demo_unpack() -> None:
    """Demonstrate unpacking list to parameters."""
    numbers = [1, 2, 3, 4, 5]
    print(numbers)
    print(*numbers)


def demo_unpack_dict() -> None:
    """Demonstrate unpacking dictionary to parameters."""
    data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    print(data)
    for key, value in data.items():
        print(f"{key}: {value}")


def demo_func_default_args(name: str = "World", greeting: str = "Hello") -> None:
    """Demonstrate function with default arguments."""
    print(f"{greeting}, {name}!")


def demo_func_keyword_args(name: str, age: int, city: str = "Unknown") -> None:
    """Demonstrate function with keyword arguments."""
    print(f"Name: {name}, Age: {age}, City: {city}")


def demo_func_variable_args(*args: str, **kwargs: str) -> None:
    """Demonstrate function with variable arguments."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
