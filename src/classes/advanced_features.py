"""
Advanced class features demonstrations for Python 3.12.

This module demonstrates advanced concepts including:
- Private variables and name mangling
- Class variables vs instance variables
- Property descriptors
- Class and static methods
- Metaclasses (basic introduction)
- Slots for memory optimization
"""

from typing import Any


class BankAccount:
    """Demonstrates private variables and encapsulation."""

    _bank_name = "Python Bank"  # Protected class variable
    __total_accounts = 0  # Private class variable

    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        """Initialize bank account with private variables."""
        self.account_holder = account_holder
        self._account_number = self.__generate_account_number()  # Protected
        self.__balance = initial_balance  # Private
        BankAccount.__total_accounts += 1

    @staticmethod
    def __generate_account_number() -> str:
        """Generate account number (private static method)."""
        import random
        import string

        return "".join(random.choices(string.digits, k=10))

    @property
    def balance(self) -> float:
        """Get account balance."""
        return self.__balance

    @balance.setter
    def balance(self, amount: float) -> None:
        """Set account balance with validation."""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount: float) -> None:
        """Deposit money."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float) -> bool:
        """Withdraw money."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            return False
        self.__balance -= amount
        return True

    @classmethod
    def get_total_accounts(cls) -> int:
        """Get total number of accounts."""
        return cls.__total_accounts

    @classmethod
    def get_bank_name(cls) -> str:
        """Get bank name."""
        return cls._bank_name

    def __str__(self) -> str:
        """String representation."""
        return f"Account({self.account_holder}, #{self._account_number[-4:]})"


class Temperature:
    """Demonstrates property descriptors."""

    def __init__(self, celsius: float = 0.0) -> None:
        """Initialize temperature in Celsius."""
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Get temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Set temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Get temperature in Fahrenheit."""
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Set temperature in Fahrenheit."""
        celsius = (value - 32) * 5 / 9
        self.celsius = celsius  # Use the celsius setter for validation

    @property
    def kelvin(self) -> float:
        """Get temperature in Kelvin."""
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float) -> None:
        """Set temperature in Kelvin."""
        if value < 0:
            raise ValueError("Kelvin temperature cannot be negative")
        self._celsius = value - 273.15


class Point:
    """Demonstrates __slots__ for memory optimization."""

    __slots__ = ["x", "y"]  # Restrict attributes and save memory

    def __init__(self, x: float, y: float) -> None:
        """Initialize point coordinates."""
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        """Calculate distance from origin."""
        return (self.x**2 + self.y**2) ** 0.5

    def __str__(self) -> str:
        """String representation."""
        return f"Point({self.x}, {self.y})"


class Employee:
    """Demonstrates class variables and their behavior."""

    company_name = "Tech Corp"  # Class variable
    total_employees = 0  # Class variable

    def __init__(self, name: str, department: str, salary: float) -> None:
        """Initialize employee."""
        self.name = name  # Instance variable
        self.department = department  # Instance variable
        self.salary = salary  # Instance variable

        # Increment class variable
        Employee.total_employees += 1
        self.employee_id = Employee.total_employees

    @classmethod
    def set_company_name(cls, name: str) -> None:
        """Set company name for all employees."""
        cls.company_name = name

    @classmethod
    def get_company_info(cls) -> str:
        """Get company information."""
        return f"{cls.company_name} has {cls.total_employees} employees"

    @staticmethod
    def is_working_hours(hour: int) -> bool:
        """Check if it's working hours."""
        return 9 <= hour <= 17

    def __str__(self) -> str:
        """String representation."""
        return f"Employee(#{self.employee_id}, {self.name}, {self.department})"


class SingletonMeta(type):
    """Simple metaclass for singleton pattern."""

    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Ensure only one instance exists."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """Singleton database connection class."""

    def __init__(self, host: str = "localhost", port: int = 5432) -> None:
        """Initialize database connection."""
        self.host = host
        self.port = port
        self.connected = False

    def connect(self) -> None:
        """Connect to database."""
        self.connected = True
        print(f"Connected to {self.host}:{self.port}")

    def disconnect(self) -> None:
        """Disconnect from database."""
        self.connected = False
        print("Disconnected from database")


def demo_advanced_features() -> None:
    """Demonstrate advanced class features."""
    print("\n" + "=" * 50)
    print("ADVANCED FEATURES DEMONSTRATION")
    print("=" * 50)

    demo_private_variables()
    demo_property_descriptors()
    demo_class_vs_instance_variables()
    demo_slots()
    demo_metaclasses()


def demo_private_variables() -> None:
    """Demonstrate private variables and name mangling."""
    print("\n1. Private Variables and Name Mangling:")
    print("-" * 39)

    account = BankAccount("John Doe", 1000.0)
    print(f"Account: {account}")
    print(f"Balance: ${account.balance:.2f}")

    # Access protected attribute (convention, not enforced)
    print(f"Account number ends with: {account._account_number[-4:]}")

    # Try to access private attribute directly (won't work as expected)
    print(f"Total accounts: {BankAccount.get_total_accounts()}")

    # Name mangling demonstration
    print("\nName mangling:")
    print(f"  Private balance accessible via: _BankAccount__balance")
    print(f"  Actual private value: ${account._BankAccount__balance:.2f}")

    # Property usage
    account.deposit(500.0)
    print(f"After deposit: ${account.balance:.2f}")


def demo_property_descriptors() -> None:
    """Demonstrate property descriptors."""
    print("\n2. Property Descriptors:")
    print("-" * 22)

    temp = Temperature(25.0)
    print(f"Temperature: {temp.celsius:.1f}°C")
    print(f"In Fahrenheit: {temp.fahrenheit:.1f}°F")
    print(f"In Kelvin: {temp.kelvin:.1f}K")

    # Set temperature in different units
    temp.fahrenheit = 86.0
    print(f"\nAfter setting to 86°F:")
    print(f"Celsius: {temp.celsius:.1f}°C")
    print(f"Kelvin: {temp.kelvin:.1f}K")

    # Validation through properties
    try:
        temp.celsius = -300.0  # Below absolute zero
    except ValueError as e:
        print(f"Validation error: {e}")


def demo_class_vs_instance_variables() -> None:
    """Demonstrate class vs instance variables."""
    print("\n3. Class vs Instance Variables:")
    print("-" * 31)

    # Create employees
    emp1 = Employee("Alice", "Engineering", 75000)
    emp2 = Employee("Bob", "Marketing", 65000)

    print(f"Employee 1: {emp1}")
    print(f"Employee 2: {emp2}")
    print(f"Company info: {Employee.get_company_info()}")

    # Change class variable
    Employee.set_company_name("New Tech Corp")
    print(f"After company name change: {Employee.get_company_info()}")

    # Both employees see the change
    print(f"Emp1 company: {emp1.company_name}")
    print(f"Emp2 company: {emp2.company_name}")

    # Instance variable shadows class variable
    emp1.company_name = "Freelance"
    print(f"Emp1 after individual change: {emp1.company_name}")
    print(f"Emp2 still has class value: {emp2.company_name}")


def demo_slots() -> None:
    """Demonstrate __slots__ for memory optimization."""
    print("\n4. __slots__ for Memory Optimization:")
    print("-" * 34)

    point = Point(3.0, 4.0)
    print(f"Point: {point}")
    print(f"Distance: {point.distance_from_origin():.2f}")

    # Cannot add new attributes to slotted class
    try:
        point.z = 5.0  # This will fail
    except AttributeError as e:
        print(f"Cannot add attribute to slotted class: {e}")

    # Show memory usage difference (conceptual)
    print("\n__slots__ benefits:")
    print("  - Reduced memory usage per instance")
    print("  - Faster attribute access")
    print("  - Prevents accidental attribute creation")


def demo_metaclasses() -> None:
    """Demonstrate basic metaclass usage."""
    print("\n5. Metaclasses (Singleton Pattern):")
    print("-" * 32)

    # Create database connections
    db1 = DatabaseConnection("server1", 5432)
    db2 = DatabaseConnection("server2", 3306)  # Will be ignored

    print(f"db1 is db2: {db1 is db2}")  # Should be True (singleton)
    print(f"DB1 host: {db1.host}")
    print(f"DB2 host: {db2.host}")  # Same as db1

    db1.connect()
    print(f"DB2 connected: {db2.connected}")  # Same instance

    # Show singleton instances
    print(f"Singleton instances: {len(SingletonMeta._instances)}")
