"""
Exception chaining and propagation demonstrations.

This module shows advanced exception handling patterns including
chaining, suppression, and proper error propagation techniques.
"""

import json
import sys
from typing import Any, Dict, List


class DataProcessingError(Exception):
    """Base exception for data processing operations."""

    pass


class ValidationError(DataProcessingError):
    """Exception for validation failures."""

    pass


class TransformationError(DataProcessingError):
    """Exception for data transformation failures."""

    pass


class DatabaseError(Exception):
    """Base class for database-related errors."""

    pass


class ConnectionError(DatabaseError):
    """Raised when database connection fails."""

    pass


class QueryError(DatabaseError):
    """Raised when a database query fails."""

    pass


def demo_exception_chaining() -> None:
    """Demonstrate exception chaining patterns."""
    print("=== Exception Chaining ===\n")

    demo_basic_chaining()
    demo_chaining_with_context()
    demo_exception_suppression()
    demo_nested_exception_handling()
    demo_exception_groups()


def demo_basic_chaining() -> None:
    """Demonstrate basic exception chaining with 'from' keyword."""
    print("=== BASIC EXCEPTION CHAINING ===")

    def parse_config_value(value: str, field_name: str) -> int:
        """Convert string to int with chained exceptions."""
        try:
            return int(value)
        except ValueError as e:
            # Chain the original ValueError to our custom exception
            raise TypeError(f"Cannot convert '{value}' to integer") from e

    def load_configuration(config_data: Dict[str, str]) -> Dict[str, int]:
        """Load configuration with user-friendly error messages."""
        parsed_config = {}

        for key, value in config_data.items():
            try:
                parsed_config[key] = parse_config_value(value, key)
                print(
                    f"   {key}: {value} -> {parsed_config[key]} ({type(parsed_config[key]).__name__})"
                )
            except ValueError as e:
                print(f"   Error parsing {key}: {e}")
                # Note: No __cause__ attribute due to suppression

        return parsed_config

    # Test configuration parsing
    print("\n1. Configuration Parsing (with suppression):")
    test_config = {
        "port": "8080",
        "timeout": "30.5",
        "debug": "true",
        "invalid_field": "not_parseable_value",
    }

    result = load_configuration(test_config)
    print(f"   Parsed configuration: {result}")


def demo_chaining_with_context() -> None:
    """Demonstrate automatic exception chaining without 'from'."""
    print("2. Automatic exception context:")

    def process_user_data(user_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # This might raise KeyError
            user_id = user_data["id"]
            # This might raise ValueError
            age = int(user_data["age"])
            return {"user_id": user_id, "age": age}
        except (KeyError, ValueError):
            # Re-raise as custom exception without 'from'
            # Python automatically preserves the context
            raise DataProcessingError("Failed to process user data")

    test_data = [
        {"id": "123", "age": "25"},  # Valid
        {"id": "456"},  # Missing age
        {"id": "789", "age": "invalid"},  # Invalid age
    ]

    for i, data in enumerate(test_data, 1):
        try:
            result = process_user_data(data)
            print(f"User {i}: Success - {result}")
        except DataProcessingError as e:
            print(f"User {i}: {e}")
            # Show both __cause__ (explicit) and __context__ (implicit)
            print(f"  Explicit cause: {e.__cause__}")
            print(f"  Implicit context: {e.__context__}")
            if e.__context__:
                print(f"  Context type: {type(e.__context__).__name__}")

    print()


def demo_exception_suppression() -> None:
    """Demonstrate exception suppression with 'from None'."""
    print("=== EXCEPTION SUPPRESSION ===")

    def parse_config_value(value: str, field_name: str) -> Any:
        """Parse configuration value, suppressing implementation details."""
        try:
            # Try JSON parsing first
            return json.loads(value)
        except json.JSONDecodeError:
            try:
                # Try as integer
                return int(value)
            except ValueError:
                try:
                    # Try as float
                    return float(value)
                except ValueError:
                    # Suppress the chain of failed attempts
                    raise ValueError(
                        f"Cannot parse configuration value for '{field_name}'"
                    ) from None

    def load_configuration(config_data: Dict[str, str]) -> Dict[str, Any]:
        """Load configuration with user-friendly error messages."""
        parsed_config = {}

        for key, value in config_data.items():
            try:
                parsed_config[key] = parse_config_value(value, key)
                print(
                    f"   {key}: {value} -> {parsed_config[key]} ({type(parsed_config[key]).__name__})"
                )
            except ValueError as e:
                print(f"   Error parsing {key}: {e}")
                # Note: No __cause__ attribute due to suppression

        return parsed_config

    # Test configuration parsing
    print("\n2. Configuration Parsing (with suppression):")
    test_config = {
        "port": "8080",
        "timeout": "30.5",
        "debug": "true",
        "invalid_field": "not_parseable_value",
    }

    result = load_configuration(test_config)
    print(f"   Parsed configuration: {result}")


def demo_nested_exception_handling() -> None:
    """Demonstrate nested exception handling with multiple layers."""
    print("4. Nested exception handling:")

    def validate_data(data: Any) -> None:
        if not isinstance(data, dict):
            raise ValidationError("Data must be a dictionary")

    def transform_data(data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validate_data(data)
            # Simulate transformation that might fail
            if "error" in data:
                raise ValueError("Transformation failed")
            return {k: str(v).upper() for k, v in data.items()}
        except ValidationError:
            # Re-raise validation errors as-is
            raise
        except ValueError as e:
            # Chain transformation errors
            raise TransformationError("Data transformation failed") from e

    def process_batch(batch: List[Any]) -> List[Dict[str, Any]]:
        results = []
        errors = []

        for i, item in enumerate(batch):
            try:
                result = transform_data(item)
                results.append(result)
            except DataProcessingError as e:
                error_info = {
                    "item_index": i,
                    "error": str(e),
                    "error_type": type(e).__name__,
                    "original_cause": str(e.__cause__) if e.__cause__ else None,
                }
                errors.append(error_info)

        if errors:
            error_summary = f"Processing failed for {len(errors)} items"
            raise DataProcessingError(error_summary) from Exception(
                f"Batch errors: {errors}"
            )

        return results

    test_batch = [
        {"name": "alice", "role": "admin"},  # Valid
        "invalid_data",  # Invalid type
        {"name": "bob", "error": "simulate"},  # Transformation error
        {"name": "charlie", "role": "user"},  # Valid
    ]

    try:
        results = process_batch(test_batch)
        print(f"Batch processing successful: {results}")
    except DataProcessingError as e:
        print(f"Batch processing failed: {e}")
        if e.__cause__:
            print(f"Error details: {e.__cause__}")

    print()


def demo_exception_groups() -> None:
    """Demonstrate exception groups (Python 3.11+ feature)."""
    print("=== EXCEPTION GROUPING (SIMULATED) ===")

    class MultipleErrorsException(Exception):
        """Exception that can contain multiple sub-errors."""

        def __init__(self, message: str, errors: List[Exception]) -> None:
            super().__init__(message)
            self.errors = errors

        def __str__(self) -> str:
            """Format multiple errors for display."""
            lines = [super().__str__()]
            for i, error in enumerate(self.errors, 1):
                lines.append(f"  {i}. {type(error).__name__}: {error}")
            return "\n".join(lines)

    def validate_user_batch(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Validate a batch of users, collecting all errors."""
        valid_users = []
        validation_errors = []

        for i, user in enumerate(users):
            try:
                # Validate required fields
                if "name" not in user or not user["name"]:
                    raise ValueError(f"User {i}: Name is required")

                if "age" not in user:
                    raise ValueError(f"User {i}: Age is required")

                if not isinstance(user["age"], int) or user["age"] < 0:
                    raise ValueError(f"User {i}: Age must be a positive integer")

                valid_users.append(user)

            except ValueError as e:
                validation_errors.append(e)

        # If there were errors, raise them all together
        if validation_errors:
            raise MultipleErrorsException(
                f"Validation failed for {len(validation_errors)} users",
                validation_errors,
            )

        return valid_users

    # Test batch validation
    print("\n5. Exception Grouping:")

    test_users = [
        {"name": "Alice", "age": 25},  # Valid
        {"name": "", "age": 30},  # Invalid name
        {"name": "Charlie"},  # Missing age
        {"name": "David", "age": -5},  # Invalid age
        {"name": "Eve", "age": 35},  # Valid
    ]

    try:
        valid = validate_user_batch(test_users)
        print(f"   All {len(valid)} users are valid")
    except MultipleErrorsException as e:
        print(f"   Batch validation failed: {e}")


def demo_traceback_preservation() -> None:
    """Demonstrate traceback preservation techniques."""
    print("6. Traceback preservation:")

    def level_3_function() -> None:
        raise ValueError("Error at level 3")

    def level_2_function() -> None:
        try:
            level_3_function()
        except ValueError:
            # Re-raise to preserve full traceback
            raise DataProcessingError("Error caught at level 2") from sys.exc_info()[1]

    def level_1_function() -> None:
        try:
            level_2_function()
        except DataProcessingError as e:
            print("Full exception chain:")
            current = e
            level = 0
            while current:
                print(f"  Level {level}: {type(current).__name__}: {current}")
                current = current.__cause__
                level += 1

    level_1_function()
    print()


if __name__ == "__main__":
    demo_exception_chaining()
