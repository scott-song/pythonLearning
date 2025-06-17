"""Best practices for exception handling in production code."""

import logging
import time
from dataclasses import dataclass
from functools import wraps
from typing import Any, Callable, Dict, List, Optional


@dataclass
class ValidationError(Exception):
    """Custom validation error with detailed information."""

    field: str
    value: Any
    message: str

    def __init__(self, field: str, value: Any, message: str) -> None:
        """Initialize validation error."""
        self.field = field
        self.value = value
        self.message = message
        super().__init__(f"Validation failed for {field}: {message}")


@dataclass
class ProcessingError(Exception):
    """Error during data processing operations."""

    operation: str
    data: Any
    original_error: Optional[Exception] = None

    def __init__(
        self,
        operation: str,
        data: Any,
        original_error: Optional[Exception] = None,
    ) -> None:
        """Initialize processing error."""
        self.operation = operation
        self.data = data
        self.original_error = original_error
        message = f"Processing failed during {operation}"
        if original_error:
            message += f": {original_error}"
        super().__init__(message)


def validate_user_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate user data with comprehensive error checking."""
    if not isinstance(data, dict):
        raise ValidationError("data", data, "Must be a dictionary")

    if "name" not in data:
        raise ValidationError("name", None, "Name is required")

    if not data["name"].strip():
        raise ValidationError("name", data["name"], "Name cannot be empty")

    if "age" in data:
        try:
            age = int(data["age"])
            if age < 0 or age > 150:
                raise ValidationError("age", age, "Age must be between 0 and 150")
        except (ValueError, TypeError) as e:
            raise ValidationError("age", data["age"], "Age must be a number") from e

    return data


def retry_with_backoff(
    max_retries: int = 3, base_delay: float = 1.0, max_delay: float = 60.0
) -> Callable:
    """Decorate functions with retry logic and exponential backoff."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt == max_retries:
                        raise

                    delay = min(base_delay * (2**attempt), max_delay)
                    logging.warning(
                        f"Attempt {attempt + 1} failed: {e}. "
                        f"Retrying in {delay:.1f}s"
                    )
                    time.sleep(delay)

            # This should never be reached due to the raise above
            raise last_exception  # pragma: no cover

        return wrapper

    return decorator


def safe_division(numerator: float, denominator: float) -> float:
    """Perform safe division with proper error handling."""
    if not isinstance(numerator, (int, float)):
        raise TypeError(f"Numerator must be a number, got {type(numerator)}")

    if not isinstance(denominator, (int, float)):
        raise TypeError(f"Denominator must be a number, got {type(denominator)}")

    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return float(numerator) / float(denominator)


def process_configuration(config_data: Dict[str, Any]) -> Dict[str, Any]:
    """Process configuration with validation and error recovery."""
    try:
        # Validate required fields
        required_fields = ["host", "port", "database"]
        for field in required_fields:
            if field not in config_data:
                raise ValidationError(field, None, f"{field} is required")

        # Type validation
        if not isinstance(config_data["port"], int):
            try:
                config_data["port"] = int(config_data["port"])
            except (ValueError, TypeError) as e:
                raise ValidationError(
                    "port", config_data["port"], "Port must be an integer"
                ) from e

        # Range validation
        if not 1 <= config_data["port"] <= 65535:
            raise ValidationError(
                "port",
                config_data["port"],
                "Port must be between 1 and 65535",
            )

        # Provide defaults for optional fields
        config_data.setdefault("timeout", 30)
        config_data.setdefault("ssl", False)
        config_data.setdefault("pool_size", 10)

        return config_data

    except ValidationError:
        # Re-raise validation errors as-is
        raise
    except Exception as e:
        # Wrap unexpected errors
        raise ProcessingError("configuration_processing", config_data, e) from e


def demonstrate_anti_patterns() -> None:
    """Show common anti-patterns to avoid."""
    print("=== ANTI-PATTERNS TO AVOID ===")

    # Anti-pattern 1: Bare except clause
    print("\n1. Bare except clause (DON'T DO THIS):")
    try:
        # This is bad practice
        result = 10 / 0
    except:  # noqa: E722 - Intentionally showing anti-pattern
        print("   Something went wrong (too generic!)")

        # Anti-pattern 2: Ignoring exceptions silently
    print("\n2. Silent exception handling (DON'T DO THIS):")
    try:
        _ = int("not_a_number")
    except ValueError:
        pass  # Silent failure - very bad!

    # Anti-pattern 3: Exception for control flow
    print("\n3. Using exceptions for control flow (DON'T DO THIS):")
    try:
        items = [1, 2, 3]
        for i in range(100):  # Will eventually raise IndexError
            print(f"   Item {i}: {items[i]}")
    except IndexError:
        print("   End of list reached")  # This is bad design

    print("\nBetter alternatives:")
    print("- Use specific exception types")
    print("- Log exceptions appropriately")
    print("- Use proper bounds checking instead of exception control flow")


@retry_with_backoff(max_retries=2, base_delay=0.1)
def unreliable_operation(success_rate: float = 0.3) -> str:
    """Simulate an unreliable operation for retry demonstration."""
    import random

    if random.random() > success_rate:
        raise ConnectionError("Simulated network error")
    return "Operation successful!"


def demonstrate_defensive_programming() -> None:
    """Show defensive programming techniques."""
    print("=== DEFENSIVE PROGRAMMING ===")

    # Input validation
    print("\n1. Input Validation:")
    test_data = {"name": "John Doe", "age": "25"}
    try:
        validated = validate_user_data(test_data)
        print(f"   Validated data: {validated}")
    except ValidationError as e:
        print(f"   Validation error: {e}")

    # Safe operations
    print("\n2. Safe Operations:")
    try:
        result = safe_division(10, 2)
        print(f"   10 / 2 = {result}")

        result = safe_division(10, 0)
    except (TypeError, ZeroDivisionError) as e:
        print(f"   Division error: {e}")

    # Configuration processing
    print("\n3. Configuration Processing:")
    test_config = {"host": "localhost", "port": "5432", "database": "mydb"}
    try:
        processed = process_configuration(test_config)
        print(f"   Processed config: {processed}")
    except (ValidationError, ProcessingError) as e:
        print(f"   Configuration error: {e}")


def demonstrate_error_recovery() -> None:
    """Show error recovery strategies."""
    print("=== ERROR RECOVERY STRATEGIES ===")

    # Retry with backoff
    print("\n1. Retry with Exponential Backoff:")
    try:
        result = unreliable_operation(success_rate=0.7)
        print(f"   Result: {result}")
    except ConnectionError as e:
        print(f"   Final failure: {e}")

    # Graceful degradation
    print("\n2. Graceful Degradation:")

    def get_user_preferences(user_id: int) -> Dict[str, Any]:
        """Get user preferences with fallback to defaults."""
        try:
            # Simulate database call that might fail
            if user_id == 999:  # Simulate missing user
                raise KeyError(f"User {user_id} not found")

            return {"theme": "dark", "language": "en", "notifications": True}
        except KeyError:
            # Return default preferences
            print(f"   Using default preferences for user {user_id}")
            return {"theme": "light", "language": "en", "notifications": False}

    prefs = get_user_preferences(123)
    print(f"   User preferences: {prefs}")

    prefs = get_user_preferences(999)  # This will use defaults
    print(f"   Default preferences: {prefs}")


def demonstrate_monitoring_and_alerting() -> None:
    """Show how to implement monitoring and alerting."""
    print("=== MONITORING AND ALERTING ===")

    # Set up logging for monitoring
    logger = logging.getLogger("application.monitor")

    def process_batch(items: List[Any]) -> Dict[str, int]:
        """Process a batch of items with monitoring."""
        stats = {"processed": 0, "errors": 0, "warnings": 0}

        for i, item in enumerate(items):
            try:
                # Simulate processing
                if item == "error":
                    raise ProcessingError("batch_processing", item)
                elif item == "warning":
                    logger.warning("Item %d requires attention: %s", i, item)
                    stats["warnings"] += 1
                else:
                    stats["processed"] += 1

            except ProcessingError as e:
                logger.error("Failed to process item %d: %s", i, e)
                stats["errors"] += 1
                # Continue processing other items (resilient design)

        # Alert on high error rates
        error_rate = stats["errors"] / len(items) if items else 0
        if error_rate > 0.1:  # More than 10% errors
            logger.critical(
                "High error rate detected: %.1f%% (%d/%d)",
                error_rate * 100,
                stats["errors"],
                len(items),
            )

        return stats

    # Test batch processing
    test_batch = ["good", "error", "good", "warning", "good"]
    result = process_batch(test_batch)
    print(f"   Batch processing results: {result}")


def demo_best_practices() -> None:
    """Run all best practices demonstrations."""
    print("BEST PRACTICES FOR EXCEPTION HANDLING")
    print("=" * 50)

    demonstrate_defensive_programming()
    print()

    demonstrate_error_recovery()
    print()

    demonstrate_anti_patterns()
    print()

    demonstrate_monitoring_and_alerting()
