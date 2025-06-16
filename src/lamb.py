def demo_lambda():
    """A demo function to show basic Python functionality."""
    print("demo_lambdaaaaabbb")

    f = make_incrementor(42)
    print(f(0))
    print(f(1))

    def add(x, y):
        return x + y

    print(add(1, 2))

    # Proper lambda usage - inline with higher-order functions
    pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
    pairs.sort(key=lambda pair: pair[1])
    print(pairs)

    # More lambda examples
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)

    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)


def make_incrementor(n):
    return lambda x: x + n
