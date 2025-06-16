def demo_func():
    """A demo function to show basic Python functionality."""
    print("demo_function")
    parrot(1000)
    parrot(voltage=1000)
    parrot(voltage=1000000, action="VOOOOOM")
    parrot(action="VOOOOOM", voltage=1000000)
    parrot("a million", "bereft of life", "jump")
    parrot("a thousand", state="pushing up the daisies")
    cheeseshop(
        "Limburger",
        "It's very runny, sir.",
        "It's really very, VERY runny, sir.",
        shopkeeper="Michael Palin",
        client="John Cleese",
        sketch="Cheese Shop Sketch",
    )
    demo_unpack()
    demo_unpack_dict()


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
