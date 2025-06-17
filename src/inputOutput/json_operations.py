"""JSON operations and data serialization demonstrations."""

import json
import os


def demo_json_operations() -> None:
    """Demonstrate JSON input/output operations."""
    print("\n--- JSON Operations ---")

    # Sample data
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "swimming", "coding"],
        "is_student": False,
    }

    # Convert to JSON string
    # json.dumps() converts Python object to JSON string
    # indent=2 adds 2 spaces of indentation to make the output more readable
    # Without indent, the JSON would be a single line
    json_string = json.dumps(data, indent=2)
    print("Python dict to JSON string:")
    print(json_string)

    # Convert back to Python object
    parsed_data = json.loads(json_string)
    print("\nJSON string back to Python dict:")
    print(f"Name: {parsed_data['name']}")
    print(f"Hobbies: {', '.join(parsed_data['hobbies'])}")

    # Write to JSON file
    json_file = "demo_data.json"
    try:
        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        print(f"\nData written to {json_file}")

        # Read from JSON file
        with open(json_file, "r", encoding="utf-8") as file:
            loaded_data = json.load(file)
        print(f"Data loaded from {json_file}: {loaded_data['name']}")

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"JSON error: {e}")
    finally:
        if os.path.exists(json_file):
            os.remove(json_file)
