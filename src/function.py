def demo_func():
    """Demo function for function examples."""
    print("demo_func - Function examples")

    def greet(name):
        return f"Hello, {name}!"

    print(greet("World"))

    # Function with default parameter
    def power(base, exponent=2):
        return base**exponent

    print(f"2^3 = {power(2, 3)}")
    print(f"5^2 = {power(5)}")


def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# unpack list to parameter
def demo_unpack():
    numbers = [1, 2, 3, 4, 5]
    print(numbers)
    print(*numbers)


def demo_unpack_dict():
    data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    print(data)
    for key, value in data.items():
        print(f"{key}: {value}")
