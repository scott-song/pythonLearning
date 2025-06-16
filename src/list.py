def demo_list() -> None:
    """Demo function for list examples."""
    print("demo_list - List examples")

    # Basic list operations
    fruits = ["apple", "banana", "cherry"]
    print(f"Fruits: {fruits}")

    # List methods
    fruits.append("date")
    print(f"After append: {fruits}")

    # List comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(f"Squares: {squares}")


def demo_list_number() -> None:
    squares = [1, 4, 9, 16, 25]
    print(squares)
    print(squares[0])
    print(squares[-1])
    print(squares[1:3])
    print(squares[:2])
    print(squares[2:])
    print(squares[-2:])
    print(squares[:-2])
    print(squares[::2])
    print(squares + [36, 49, 64, 81, 100])
    print(squares * 2)
    print(squares)
    squares.append(100)
    print(squares)
    squares.remove(100)
    print(squares)
    squares.pop()
    print(squares)
    squares.pop(0)
    print(squares)
    squares.clear()
    print(squares)


def demo_list_str() -> None:
    rgb = ["red", "green", "blue"]
    rgba = rgb.copy()
    print(rgba)
    rgba.remove("green")
    print(rgb)
    print(rgba)
    sliced_rgb = rgb[:]
    print(f"sliced_rgb is {sliced_rgb}")
    sliced_rgb.append("black")
    print(f"sliced_rgb is {sliced_rgb}")
    print(f"rgb is {rgb}")
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    print(f"letters is {letters}")
    print(f"letters[2:5] is {letters[2:5]}")
    print(f"letters[:4] is {letters[:4]}")
    print(f"letters[2:] is {letters[2:]}")
    print(f"letters[-2:] is {letters[-2:]}")
    print(f"letters[:-2] is {letters[:-2]}")
    print(f"letters[::2] is {letters[::2]}")
    letters[2:5] = []
    print(letters)
