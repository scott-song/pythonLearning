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
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def cheeseshop(kind: str, *arguments: str, **keywords: str) -> None:
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# unpack list to parameter
def demo_unpack() -> None:
    numbers = [1, 2, 3, 4, 5]
    print(numbers)
    print(*numbers)


def demo_unpack_dict() -> None:
    data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    print(data)
    for key, value in data.items():
        print(f"{key}: {value}")
