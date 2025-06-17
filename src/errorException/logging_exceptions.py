"""
Exception logging and debugging demonstrations.

This module shows how to properly log exceptions, preserve stack traces,
and implement debugging-friendly error handling in Python 3.12.
"""

import logging
import sys
import traceback
from datetime import datetime
from typing import Any, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger(__name__)


class ApplicationError(Exception):
    """Base application exception with enhanced logging."""

    def __init__(
        self,
        message: str,
        error_code: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.context = context or {}
        self.timestamp = datetime.now().isoformat()

        # Log the exception when it's created
        self._log_exception()

    def _log_exception(self) -> None:
        """Log the exception with context."""
        log_data = {
            "error_code": self.error_code,
            "error_message": self.message,
            "context": self.context,
            "timestamp": self.timestamp,
        }
        logger.error(f"ApplicationError: {self.message}", extra=log_data)


def demo_logging_exceptions() -> None:
    """Demonstrate exception logging patterns."""
    print("=== Exception Logging ===\n")

    demo_basic_exception_logging()
    demo_structured_logging()
    demo_traceback_logging()
    demo_exception_context_logging()
    demo_performance_logging()


def demo_basic_exception_logging() -> None:
    """Demonstrate basic exception logging."""
    print("1. Basic exception logging:")

    def divide_numbers(a: float, b: float) -> float:
        try:
            result = a / b
            logger.info(f"Division successful: {a} / {b} = {result}")
            return result
        except ZeroDivisionError as e:
            logger.error(f"Division by zero error: {a} / {b}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"Unexpected error in division: {type(e).__name__}: {e}")
            raise

    test_cases = [(10, 2), (10, 0), (10, "invalid")]

    for a, b in test_cases:
        try:
            result = divide_numbers(a, b)
            print(f"  {a} / {b} = {result}")
        except Exception as e:
            print(f"  Error: {type(e).__name__}: {e}")

    print()


def demo_structured_logging() -> None:
    """Demonstrate structured logging with exception context."""
    print("2. Structured exception logging:")

    def process_user_data(user_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            # Validate required fields
            if "name" not in data:
                raise ValueError("Missing required field: name")

            if "email" not in data:
                raise ValueError("Missing required field: email")

            # Process the data
            processed_data = {
                "user_id": user_id,
                "name": data["name"].strip().title(),
                "email": data["email"].lower(),
                "processed_at": datetime.now().isoformat(),
            }

            logger.info(
                "User data processed successfully",
                extra={
                    "user_id": user_id,
                    "operation": "process_user_data",
                    "fields_processed": list(processed_data.keys()),
                },
            )

            return processed_data

        except ValueError as e:
            logger.error(
                "User data validation failed",
                extra={
                    "user_id": user_id,
                    "operation": "process_user_data",
                    "error_type": "validation_error",
                    "input_data": data,
                    "error_message": str(e),
                },
            )
            raise
        except Exception as e:
            logger.error(
                "Unexpected error processing user data",
                extra={
                    "user_id": user_id,
                    "operation": "process_user_data",
                    "error_type": type(e).__name__,
                    "input_data": data,
                },
                exc_info=True,
            )
            raise

    test_users = [
        (1, {"name": "Alice", "email": "ALICE@EXAMPLE.COM"}),  # Valid
        (2, {"name": "Bob"}),  # Missing email
        (3, {"email": "charlie@example.com"}),  # Missing name
    ]

    for user_id, data in test_users:
        try:
            result = process_user_data(user_id, data)
            print(f"  User {user_id}: Success")
        except ValueError as e:
            print(f"  User {user_id}: Validation error - {e}")

    print()


def demo_traceback_logging() -> None:
    """Demonstrate detailed traceback logging."""
    print("3. Traceback logging:")

    def deep_function_call() -> None:
        """Function that calls other functions to create a deep stack."""
        level_1()

    def level_1() -> None:
        level_2()

    def level_2() -> None:
        level_3()

    def level_3() -> None:
        raise RuntimeError("Error in deep function call")

    # Method 1: Using exc_info=True
    try:
        deep_function_call()
    except RuntimeError as e:
        logger.error("Error caught with full traceback", exc_info=True)
        print("  Logged with exc_info=True")

    # Method 2: Manual traceback formatting
    try:
        deep_function_call()
    except RuntimeError as e:
        tb_str = traceback.format_exc()
        logger.error(f"Error with manual traceback:\n{tb_str}")
        print("  Logged with manual traceback formatting")

    # Method 3: Structured traceback information
    try:
        deep_function_call()
    except RuntimeError as e:
        tb_info = traceback.extract_tb(sys.exc_info()[2])
        stack_frames = [
            {
                "filename": frame.filename,
                "lineno": frame.lineno,
                "function": frame.name,
                "code": frame.line,
            }
            for frame in tb_info
        ]

        logger.error(
            "Error with structured traceback",
            extra={
                "error_type": type(e).__name__,
                "error_message": str(e),
                "stack_frames": stack_frames,
            },
        )
        print("  Logged with structured traceback data")

    print()


def demo_exception_context_logging() -> None:
    """Demonstrate logging with exception context and chaining."""
    print("4. Exception context logging:")

    def validate_config(config: Dict[str, Any]) -> None:
        try:
            port = int(config["port"])
            if port < 1 or port > 65535:
                raise ValueError(f"Port {port} is out of valid range")
        except KeyError as e:
            raise ApplicationError(
                "Configuration validation failed",
                error_code="CONFIG_MISSING_KEY",
                context={"missing_key": str(e), "config": config},
            ) from e
        except ValueError as e:
            raise ApplicationError(
                "Configuration validation failed",
                error_code="CONFIG_INVALID_VALUE",
                context={"config": config, "validation_error": str(e)},
            ) from e

    def load_application_config(config_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            validate_config(config_data)
            logger.info("Configuration loaded successfully")
            return config_data
        except ApplicationError as e:
            # Log the full exception chain
            logger.error(
                "Application configuration failed",
                extra={
                    "error_code": e.error_code,
                    "context": e.context,
                    "original_error": str(e.__cause__) if e.__cause__ else None,
                    "original_error_type": type(e.__cause__).__name__
                    if e.__cause__
                    else None,
                },
            )
            raise

    test_configs = [
        {"port": "8080", "host": "localhost"},  # Valid
        {"host": "localhost"},  # Missing port
        {"port": "invalid", "host": "localhost"},  # Invalid port
        {"port": "99999", "host": "localhost"},  # Port out of range
    ]

    for i, config in enumerate(test_configs, 1):
        try:
            result = load_application_config(config)
            print(f"  Config {i}: Success")
        except ApplicationError as e:
            print(f"  Config {i}: {e.error_code} - {e.message}")

    print()


def demo_performance_logging() -> None:
    """Demonstrate performance monitoring with exception logging."""
    print("5. Performance logging:")

    import time
    from functools import wraps

    def log_performance(operation_name: str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    end_time = time.time()
                    duration = end_time - start_time

                    logger.info(
                        f"Operation completed: {operation_name}",
                        extra={
                            "operation": operation_name,
                            "duration_seconds": duration,
                            "success": True,
                            "args_count": len(args),
                            "kwargs_count": len(kwargs),
                        },
                    )
                    return result
                except Exception as e:
                    end_time = time.time()
                    duration = end_time - start_time

                    logger.error(
                        f"Operation failed: {operation_name}",
                        extra={
                            "operation": operation_name,
                            "duration_seconds": duration,
                            "success": False,
                            "error_type": type(e).__name__,
                            "error_message": str(e),
                            "args_count": len(args),
                            "kwargs_count": len(kwargs),
                        },
                        exc_info=True,
                    )
                    raise

            return wrapper

        return decorator

    @log_performance("data_processing")
    def process_data(data: list, fail: bool = False) -> list:
        time.sleep(0.1)  # Simulate processing time
        if fail:
            raise ValueError("Processing failed as requested")
        return [item.upper() for item in data]

    # Test successful operation
    try:
        result = process_data(["hello", "world"])
        print(f"  Success: {result}")
    except Exception as e:
        print(f"  Error: {e}")

    # Test failed operation
    try:
        result = process_data(["hello", "world"], fail=True)
        print(f"  Success: {result}")
    except Exception as e:
        print(f"  Error: {e}")

    print()


def demo_custom_exception_logger() -> None:
    """Demonstrate custom exception logger with filtering."""
    print("6. Custom exception logger:")

    class ExceptionLogger:
        def __init__(self, logger_name: str = "custom_exception_logger"):
            self.logger = logging.getLogger(logger_name)
            self.exception_counts = {}

        def log_exception(
            self, exception: Exception, context: Optional[Dict[str, Any]] = None
        ):
            """Log exception with custom formatting and tracking."""
            exc_type = type(exception).__name__

            # Track exception frequency
            self.exception_counts[exc_type] = self.exception_counts.get(exc_type, 0) + 1

            log_data = {
                "exception_type": exc_type,
                "exception_message": str(exception),
                "exception_count": self.exception_counts[exc_type],
                "context": context or {},
            }

            # Different log levels based on exception type
            if isinstance(exception, (ValueError, TypeError)):
                self.logger.warning(
                    f"Data validation issue: {exception}", extra=log_data
                )
            elif isinstance(exception, (ConnectionError, TimeoutError)):
                self.logger.error(
                    f"Network/connectivity issue: {exception}", extra=log_data
                )
            else:
                self.logger.error(f"Unexpected exception: {exception}", extra=log_data)

        def get_exception_summary(self) -> Dict[str, int]:
            """Get summary of logged exceptions."""
            return self.exception_counts.copy()

    # Use custom logger
    exc_logger = ExceptionLogger()

    test_exceptions = [
        ValueError("Invalid input data"),
        TypeError("Type mismatch"),
        ConnectionError("Network timeout"),
        ValueError("Another validation error"),
        RuntimeError("Unexpected runtime error"),
    ]

    for exc in test_exceptions:
        exc_logger.log_exception(exc, context={"test_run": True})

    summary = exc_logger.get_exception_summary()
    print(f"  Exception summary: {summary}")
    print()


if __name__ == "__main__":
    demo_logging_exceptions()
