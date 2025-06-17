"""File operations and I/O handling."""

import csv
import json
import stat
import tempfile
from pathlib import Path


def demo_file_operations() -> None:
    """Demonstrate file operations with proper error handling."""
    print("File Operations Demo")
    print("-" * 20)

    # Create a temporary file for demo
    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, suffix=".txt"
    ) as temp_file:
        temp_path = Path(temp_file.name)
        temp_file.write("Hello, World!\nThis is a test file.\n")

    try:
        # Reading file
        print(f"Reading from: {temp_path}")
        with open(temp_path, "r") as file:
            content = file.read()
            print(f"Content: {repr(content)}")

        # Writing to file
        with open(temp_path, "a") as file:
            file.write("Additional line.\n")

        # Reading lines
        with open(temp_path, "r") as file:
            lines = file.readlines()
            print(f"Lines: {lines}")

        # JSON operations
        json_data = {"name": "Alice", "age": 30, "city": "New York"}
        json_path = temp_path.with_suffix(".json")

        with open(json_path, "w") as file:
            json.dump(json_data, file, indent=2)

        with open(json_path, "r") as file:
            loaded_data = json.load(file)
            print(f"JSON data: {loaded_data}")

        # Clean up
        temp_path.unlink()
        json_path.unlink()

    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")


def demo_advanced_io() -> None:
    """Demonstrate advanced I/O operations including binary files and CSV."""
    print("\nAdvanced I/O Operations Demo")
    print("-" * 30)

    # Binary file operations
    print("1. Binary File Operations:")
    binary_data = b"Hello, binary world!\x00\x01\x02\x03"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".bin") as temp_file:
        binary_path = Path(temp_file.name)
        temp_file.write(binary_data)

    try:
        # Read binary file
        with open(binary_path, "rb") as file:
            read_data = file.read()
            print(f"   Binary data: {read_data!r}")
            print(f"   Length: {len(read_data)} bytes")

        # File metadata
        file_stat = binary_path.stat()
        print(f"   File size: {file_stat.st_size} bytes")
        print(f"   Permissions: {stat.filemode(file_stat.st_mode)}")

    finally:
        binary_path.unlink()

    # CSV operations
    print("\n2. CSV File Operations:")
    csv_data = [
        ["Name", "Age", "City"],
        ["Alice", "25", "Boston"],
        ["Bob", "30", "Chicago"],
        ["Charlie", "35", "Denver"],
    ]

    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, suffix=".csv", newline=""
    ) as temp_file:
        csv_path = Path(temp_file.name)
        writer = csv.writer(temp_file)
        writer.writerows(csv_data)

    try:
        # Read CSV file
        with open(csv_path, "r", newline="") as file:
            reader = csv.reader(file)
            print("   CSV Contents:")
            for row_num, row in enumerate(reader, 1):
                print(f"     Row {row_num}: {row}")

    finally:
        csv_path.unlink()

    # File modes demonstration
    print("\n3. Different File Modes:")
    with tempfile.NamedTemporaryFile(
        mode="w", delete=False, suffix=".txt"
    ) as temp_file:
        text_path = Path(temp_file.name)
        temp_file.write("Initial content\n")

    try:
        # Append mode
        with open(text_path, "a") as file:
            file.write("Appended content\n")

        # Read mode with different encodings
        with open(text_path, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"   UTF-8 content: {repr(content)}")

        # Read with line-by-line processing
        with open(text_path, "r") as file:
            print("   Line-by-line reading:")
            for line_num, line in enumerate(file, 1):
                print(f"     Line {line_num}: {line.strip()}")

    finally:
        text_path.unlink()


def demo_directory_operations() -> None:
    """Demonstrate directory operations."""
    print("\nDirectory Operations Demo")
    print("-" * 25)

    # Create temporary directory
    temp_dir = Path(tempfile.mkdtemp())
    print(f"Created temporary directory: {temp_dir}")

    try:
        # Create subdirectories
        sub_dir = temp_dir / "subdir"
        sub_dir.mkdir()
        print(f"Created subdirectory: {sub_dir}")

        # Create files in directory
        for i in range(3):
            file_path = temp_dir / f"file_{i}.txt"
            with open(file_path, "w") as file:
                file.write(f"Content of file {i}")

        # List directory contents
        print("Directory contents:")
        for item in temp_dir.iterdir():
            if item.is_file():
                print(f"  File: {item.name} (size: {item.stat().st_size} bytes)")
            elif item.is_dir():
                print(f"  Directory: {item.name}")

        # Clean up
        import shutil

        shutil.rmtree(temp_dir)
        print("Cleaned up temporary directory")

    except OSError as e:
        print(f"OS error: {e}")


def demo_path_operations() -> None:
    """Demonstrate Path operations."""
    print("\nPath Operations Demo")
    print("-" * 20)

    # Path construction
    current_path = Path.cwd()
    print(f"Current directory: {current_path}")

    file_path = current_path / "example.txt"
    print(f"File path: {file_path}")

    # Path properties
    print(f"Path parts: {file_path.parts}")
    print(f"Parent: {file_path.parent}")
    print(f"Name: {file_path.name}")
    print(f"Stem: {file_path.stem}")
    print(f"Suffix: {file_path.suffix}")

    # Path checks
    print(f"Exists: {file_path.exists()}")
    print(f"Is file: {file_path.is_file()}")
    print(f"Is directory: {file_path.is_dir()}")

    # Absolute path
    abs_path = file_path.resolve()
    print(f"Absolute path: {abs_path}")
