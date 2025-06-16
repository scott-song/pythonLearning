from math import pi


def demo_data_struct():
    print("demo_data_struct")
    demo_list()
    demo_stack()
    demo_queue()
    demo_list_comprehension()
    demo_list_nested_comprehension()
    demo_tuple()
    demo_set()
    demo_dict()


# demo list
def demo_list():
    print("demo_list")
    fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banan"]
    print(fruits)
    apple_count = fruits.count("apple")
    print(f"Number of apples: {apple_count}")
    fruits.reverse()
    print(f"reversed: {fruits}")
    fruits.sort()
    print(f"sorted: {fruits}")
    # demo pop() codes
    print(f"pop: {fruits.pop()}")
    print(f"pop: {fruits.pop()}")


# demo stack using Lists
def demo_stack():
    print("demo_stack")
    stack = [3, 4, 5]
    stack.append(6)
    print(stack)
    print(f"pop: {stack.pop()}")
    print(f"pop: {stack.pop()}")
    print(stack)


# demo queue using Lists
def demo_queue():
    print("demo_queue")
    queue = [3, 4, 5]
    queue.append(6)
    print(queue)
    print(f"pop: {queue.pop(0)}")
    print(f"pop: {queue.pop(0)}")
    print(queue)


# demo dict
def demo_dict():
    print("demo_dictsss")
    data_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    print(data_dict)
    print(data_dict["a"])
    print(data_dict["b"])
    print(data_dict["c"])
    print(data_dict["d"])
    print(data_dict["e"])
    print(data_dict.keys())
    print(data_dict.values())
    print(sorted(data_dict.keys()))


def demo_list_comprehension():
    squares = list(map(lambda x: x * x, range(10)))
    print(f"squares: {squares}")
    squares = [x**3 for x in range(10)]
    print(f"squares: {squares}")
    print([str(round(pi, i)) for i in range(1, 6)])


def demo_list_nested_comprehension():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print(matrix)
    print([[row[i] for row in matrix] for i in range(4)])
    print(*list(zip(*matrix)))


def demo_tuple():
    print("demo_tuple")
    t = 12345, 54321, "hello!"
    print(t)
    print(t[0])
    print(t)
    u = t, (1, 2, 3, 4, 5)
    print(u)
    v = ([1, 2, 3], [3, 2, 1])
    print(v)
    v[0][0] = 8
    print(v)


def demo_set():
    print("demo_set")
    # Intentionally showing duplicates to demonstrate set behavior
    basket = {"apple", "orange", "pear", "banana"}  # noqa: B033
    print(basket)
    print("orange" in basket)
    print("crabgrass" in basket)
    a = set("abracadabra")
    b = set("alacazam")
    print(a)
    print(b)
    print(a - b)
    print(a | b)
    print(a & b)
    print(a ^ b)
