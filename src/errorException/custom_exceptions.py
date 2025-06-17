"""
Custom exception demonstrations.

This module shows how to create custom exception classes with proper
inheritance, attributes, and best practices for real-world applications.
"""

from typing import Any, Dict, Optional


class BusinessLogicError(Exception):
    """Base class for business logic related errors."""

    def __init__(self, message: str, error_code: Optional[str] = None) -> None:
        """Initialize business logic error with message and optional error code."""
        super().__init__(message)
        self.error_code = error_code

    def __str__(self) -> str:
        """Return string representation of the error."""
        if self.error_code:
            return f"[{self.error_code}] {super().__str__()}"
        return super().__str__()


class ValidationError(BusinessLogicError):
    """Raised when data validation fails."""

    def __init__(
        self,
        message: str,
        field_name: Optional[str] = None,
        field_value: Any = None,
        error_code: str = "VALIDATION_ERROR",
    ) -> None:
        """Initialize validation error with field details."""
        super().__init__(message, error_code)
        self.field_name = field_name
        self.field_value = field_value

    def __str__(self) -> str:
        """Return detailed string representation of validation error."""
        base_msg = super().__str__()
        if self.field_name:
            return f"{base_msg} (Field: {self.field_name})"
        return base_msg


class AuthenticationError(BusinessLogicError):
    """Raised when authentication fails."""

    def __init__(
        self, message: str = "Authentication failed", user_id: Optional[str] = None
    ) -> None:
        """Initialize authentication error with optional user ID."""
        super().__init__(message, "AUTH_ERROR")
        self.user_id = user_id


class AuthorizationError(BusinessLogicError):
    """Raised when user lacks permission for an operation."""

    def __init__(
        self,
        message: str = "Access denied",
        required_permission: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> None:
        """Initialize authorization error with permission and user details."""
        super().__init__(message, "AUTHZ_ERROR")
        self.required_permission = required_permission
        self.user_id = user_id


class ResourceNotFoundError(BusinessLogicError):
    """Raised when a requested resource cannot be found."""

    def __init__(
        self,
        resource_type: str,
        resource_id: Any,
        message: Optional[str] = None,
    ) -> None:
        """Initialize resource not found error with resource details."""
        if message is None:
            message = f"{resource_type} with ID '{resource_id}' not found"
        super().__init__(message, "RESOURCE_NOT_FOUND")
        self.resource_type = resource_type
        self.resource_id = resource_id

    def __str__(self) -> str:
        """Return detailed string representation of resource error."""
        return (
            f"{super().__str__()} (Type: {self.resource_type}, ID: {self.resource_id})"
        )


class ConfigurationError(Exception):
    """Raised when there's an issue with application configuration."""

    def __init__(
        self,
        message: str,
        config_key: Optional[str] = None,
        config_value: Any = None,
    ) -> None:
        """Initialize configuration error with config details."""
        super().__init__(message)
        self.config_key = config_key
        self.config_value = config_value

    def __str__(self) -> str:
        parts = [self.args[0]]
        if self.config_key:
            parts.append(f"Key: {self.config_key}")
        if self.config_value is not None:
            parts.append(f"Value: {self.config_value}")
        return " | ".join(parts)


class RetryableError(Exception):
    """Exception that indicates the operation can be retried."""

    def __init__(
        self,
        message: str,
        retry_after: Optional[int] = None,
        max_retries: int = 3,
    ) -> None:
        super().__init__(message)
        self.retry_after = retry_after
        self.max_retries = max_retries


def demo_custom_exceptions() -> None:
    """Demonstrate custom exception usage."""
    print("=== Custom Exceptions ===\n")

    demo_basic_custom_exceptions()
    demo_exception_hierarchy_usage()
    demo_exception_with_context()
    demo_exception_chaining()


def demo_basic_custom_exceptions() -> None:
    """Demonstrate basic custom exception usage."""
    print("1. Basic custom exceptions:")

    def validate_user_data(data: Dict[str, Any]) -> None:
        if "username" not in data:
            raise ValidationError("Username is required", field_name="username")

        if len(data["username"]) < 3:
            raise ValidationError(
                "Username must be at least 3 characters",
                field_name="username",
                field_value=data["username"],
            )

        if "age" in data and not isinstance(data["age"], int):
            raise ValidationError(
                "Age must be an integer",
                field_name="age",
                field_value=data["age"],
            )

    test_cases = [
        {},  # Missing username
        {"username": "ab"},  # Username too short
        {"username": "alice", "age": "twenty"},  # Invalid age type
        {"username": "alice", "age": 25},  # Valid data
    ]

    for i, test_data in enumerate(test_cases, 1):
        try:
            validate_user_data(test_data)
            print(f"Test {i}: Valid data - {test_data}")
        except ValidationError as e:
            print(f"Test {i}: {e}")

    print()


def demo_exception_hierarchy_usage() -> None:
    """Demonstrate exception hierarchy in action."""
    print("2. Exception hierarchy usage:")

    def authenticate_user(username: str, password: str) -> bool:
        if not username:
            raise AuthenticationError("Username cannot be empty")
        if not password:
            raise AuthenticationError("Password cannot be empty")
        if username == "admin" and password == "secret":
            return True
        raise AuthenticationError("Invalid credentials", user_id=username)

    def find_user(user_id: int) -> Dict[str, Any]:
        users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
        if user_id not in users:
            raise ResourceNotFoundError("User", user_id)
        return users[user_id]

    # Test authentication
    auth_tests = [
        ("", "password"),  # Empty username
        ("user", ""),  # Empty password
        ("user", "wrong"),  # Invalid credentials
        ("admin", "secret"),  # Valid credentials
    ]

    for username, password in auth_tests:
        try:
            result = authenticate_user(username, password)
            print(f"Auth success for {username}: {result}")
        except BusinessLogicError as e:
            print(f"Auth error: {e}")

    # Test resource finding
    user_ids = [1, 2, 999]
    for user_id in user_ids:
        try:
            user = find_user(user_id)
            print(f"Found user {user_id}: {user}")
        except BusinessLogicError as e:
            print(f"User lookup error: {e}")

    print()


def demo_exception_with_context() -> None:
    """Demonstrate exceptions with rich context information."""
    print("3. Exceptions with context:")

    def load_config(config_file: str) -> Dict[str, Any]:
        # Simulate configuration loading
        if config_file == "missing.conf":
            raise ConfigurationError(
                "Configuration file not found",
                config_value=config_file,
            )

        if config_file == "invalid.conf":
            raise ConfigurationError(
                "Invalid configuration format",
                config_key="database.port",
                config_value=config_file,
            )

        return {"database": {"host": "localhost", "port": 5432}}

    config_files = ["app.conf", "missing.conf", "invalid.conf"]

    for config_file in config_files:
        try:
            config = load_config(config_file)
            print(f"Loaded config from {config_file}: {config}")
        except ConfigurationError as e:
            print(f"Config error: {e}")

    print()


def demo_exception_chaining() -> None:
    """Demonstrate exception chaining with custom exceptions."""
    print("4. Exception chaining:")

    def process_data(data: str) -> int:
        try:
            return int(data)
        except ValueError as e:
            raise ValidationError(
                f"Cannot convert '{data}' to integer",
                field_name="data",
                field_value=data,
            ) from e

    def calculate_result(data_list: list[str]) -> int:
        try:
            total = sum(process_data(item) for item in data_list)
            return total
        except ValidationError as e:
            raise BusinessLogicError(
                "Failed to calculate result due to invalid data",
                error_code="CALCULATION_ERROR",
            ) from e

    test_data = ["1", "2", "invalid", "4"]

    try:
        result = calculate_result(test_data)
        print(f"Calculation result: {result}")
    except BusinessLogicError as e:
        print(f"Business error: {e}")
        print(f"Original cause: {e.__cause__}")
        if e.__cause__ and hasattr(e.__cause__, "__cause__"):
            print(f"Root cause: {e.__cause__.__cause__}")

    print()


def demo_retryable_exceptions() -> None:
    """Demonstrate retryable exception pattern."""
    print("5. Retryable exceptions:")

    import random

    def unreliable_service() -> str:
        if random.random() < 0.7:  # 70% chance of failure
            raise RetryableError(
                "Service temporarily unavailable",
                retry_after=2,
                max_retries=3,
            )
        return "Service response: Success!"

    def call_with_retry(func, max_attempts: int = 3):
        for attempt in range(1, max_attempts + 1):
            try:
                return func()
            except RetryableError as e:
                print(f"Attempt {attempt} failed: {e}")
                if attempt >= e.max_retries:
                    print("Max retries exceeded")
                    raise
                print(f"Retrying in {e.retry_after} seconds...")

    try:
        result = call_with_retry(unreliable_service)
        print(f"Success: {result}")
    except RetryableError as e:
        print(f"Final failure: {e}")

    print()


if __name__ == "__main__":
    demo_custom_exceptions()
