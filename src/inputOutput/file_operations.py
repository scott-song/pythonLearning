"""File operations and advanced I/O demonstrations."""

import os


def demo_file_operations() -> None:
    """Demonstrate file reading and writing operations."""
    print("\n--- File Operations ---")

    # Create a sample file
    sample_file = "demo_file.txt"
    sample_content = [
        "Hello, World!\n",
        "This is a demo file.\n",
        "Python I/O is powerful.\n",
    ]

    try:
        # Writing to file
        print(f"Writing to {sample_file}")
        with open(sample_file, "w", encoding="utf-8") as file:
            file.writelines(sample_content)

        # Reading entire file
        print("Reading entire file:")
        with open(sample_file, "r", encoding="utf-8") as file:
            content = file.read()
            print(repr(content))

        # Reading line by line
        print("Reading line by line:")
        with open(sample_file, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, 1):
                print(f"Line {line_num}: {line.strip()}")

        # Appending to file
        print("Appending to file")
        with open(sample_file, "a", encoding="utf-8") as file:
            file.write("This line was appended.\n")

        # Reading after append
        print("Content after append:")
        with open(sample_file, "r", encoding="utf-8") as file:
            print(file.read())

    except FileNotFoundError:
        print(f"File {sample_file} not found!")
    except PermissionError:
        print(f"Permission denied to access {sample_file}")
    finally:
        # Clean up
        if os.path.exists(sample_file):
            os.remove(sample_file)
            print(f"Cleaned up {sample_file}")


def demo_advanced_io() -> None:
    """Demonstrate advanced I/O operations."""
    print("\n--- Advanced I/O Operations ---")

    # Binary file operations
    print("Binary file operations:")
    binary_data = b"Hello, binary world!"
    binary_file = "demo_binary.bin"

    try:
        with open(binary_file, "wb") as file:
            file.write(binary_data)

        with open(binary_file, "rb") as file:
            read_data = file.read()
            print(f"Read binary data: {read_data!r}")
    finally:
        if os.path.exists(binary_file):
            os.remove(binary_file)

    # CSV-like operations (manual)
    print("\nCSV-like operations:")
    csv_data = [
        ["Name", "Age", "City"],
        ["Alice", "25", "Boston"],
        ["Bob", "30", "Chicago"],
        ["Charlie", "35", "Denver"],
    ]

    csv_file = "demo_data.csv"
    try:
        with open(csv_file, "w", encoding="utf-8") as file:
            for row in csv_data:
                file.write(",".join(row) + "\n")

        print(f"CSV data written to {csv_file}")

        with open(csv_file, "r", encoding="utf-8") as file:
            print("Reading CSV data:")
            for line_num, line in enumerate(file, 1):
                columns = line.strip().split(",")
                print(f"  Row {line_num}: {columns}")
    finally:
        if os.path.exists(csv_file):
            os.remove(csv_file)
