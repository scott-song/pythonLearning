"""Path operations using pathlib module."""

from pathlib import Path


def demo_path_operations() -> None:
    """Demonstrate pathlib for path operations."""
    print("\n--- Path Operations (pathlib) ---")

    # Create Path objects
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")

    # Path manipulation
    demo_path = Path("demo_folder") / "subfolder" / "file.txt"
    print(f"Constructed path: {demo_path}")
    print(f"Parent directory: {demo_path.parent}")
    print(f"Filename: {demo_path.name}")
    print(f"Stem: {demo_path.stem}")
    print(f"Suffix: {demo_path.suffix}")

    # Create directories and files
    test_dir = Path("test_directory")
    test_file = test_dir / "test_file.txt"

    try:
        # Create directory
        test_dir.mkdir(exist_ok=True)
        print(f"Created directory: {test_dir}")

        # Create file
        test_file.write_text("Hello from pathlib!", encoding="utf-8")
        print(f"Created file: {test_file}")

        # Check if exists
        print(f"Directory exists: {test_dir.exists()}")
        print(f"File exists: {test_file.exists()}")

        # Read file
        content = test_file.read_text(encoding="utf-8")
        print(f"File content: {content}")

        # List directory contents
        print(f"Directory contents: {list(test_dir.iterdir())}")

    finally:
        # Clean up
        if test_file.exists():
            test_file.unlink()
        if test_dir.exists():
            test_dir.rmdir()
        print("Cleaned up test files")
