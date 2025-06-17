"""
Dataclasses demonstrations for Python 3.12.

This module demonstrates modern Python class features including:
- @dataclass decorator
- Field configuration
- Post-init processing
- Frozen dataclasses
- Dataclass inheritance
- Custom methods in dataclasses
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Person:
    """Basic dataclass representing a person."""

    name: str
    age: int
    email: Optional[str] = None

    def is_adult(self) -> bool:
        """Check if person is an adult."""
        return self.age >= 18


@dataclass
class Point:
    """2D point with automatic methods."""

    x: float
    y: float

    def distance_from_origin(self) -> float:
        """Calculate distance from origin."""
        return (self.x**2 + self.y**2) ** 0.5


@dataclass(frozen=True)
class ImmutablePoint:
    """Immutable point that cannot be modified after creation."""

    x: float
    y: float

    def __post_init__(self) -> None:
        """Validate point after initialization."""
        if self.x < 0 or self.y < 0:
            raise ValueError("Coordinates must be non-negative")


@dataclass
class Employee:
    """Employee with complex field configurations."""

    name: str
    department: str
    salary: float = field(repr=False)  # Don't show in repr
    skills: List[str] = field(default_factory=list)
    hire_date: datetime = field(default_factory=datetime.now)
    employee_id: int = field(init=False)  # Not in __init__

    def __post_init__(self) -> None:
        """Set employee ID after initialization."""
        self.employee_id = hash(self.name + self.department) % 10000


@dataclass
class Product:
    """Product with validation and computed fields."""

    name: str
    price: float
    category: str
    tags: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate product data."""
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if not self.name.strip():
            raise ValueError("Product name cannot be empty")


@dataclass
class Manager(Employee):
    """Manager inheriting from Employee."""

    team_size: int = 0
    reports: List[str] = field(default_factory=list)

    def add_report(self, employee_name: str) -> None:
        """Add an employee to reports."""
        if employee_name not in self.reports:
            self.reports.append(employee_name)
            self.team_size = len(self.reports)


def demo_dataclasses() -> None:
    """Demonstrate dataclass features."""
    print("\n" + "=" * 50)
    print("DATACLASSES DEMONSTRATION")
    print("=" * 50)

    demo_basic_dataclasses()
    demo_field_configurations()
    demo_frozen_dataclasses()
    demo_post_init_processing()
    demo_dataclass_inheritance()


def demo_basic_dataclasses() -> None:
    """Demonstrate basic dataclass usage."""
    print("\n1. Basic Dataclasses:")
    print("-" * 20)

    # Create instances
    alice = Person("Alice", 30, "alice@example.com")
    bob = Person("Bob", 17)  # No email

    print(f"Alice: {alice}")
    print(f"Bob: {bob}")
    print(f"Alice is adult: {alice.is_adult()}")
    print(f"Bob is adult: {bob.is_adult()}")

    # Automatic comparison
    alice2 = Person("Alice", 30, "alice@example.com")
    print(f"alice == alice2: {alice == alice2}")

    # Point dataclass
    p1 = Point(3.0, 4.0)
    p2 = Point(1.0, 1.0)

    print(f"\nPoint 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"P1 distance from origin: {p1.distance_from_origin():.2f}")


def demo_field_configurations() -> None:
    """Demonstrate field configuration options."""
    print("\n2. Field Configurations:")
    print("-" * 22)

    # Employee with complex field setup
    emp = Employee(
        name="John Doe",
        department="Engineering",
        salary=75000.0,
        skills=["Python", "Django"],
    )

    print(f"Employee: {emp}")  # salary not shown due to repr=False
    print(f"Employee ID: {emp.employee_id}")
    print(f"Skills: {emp.skills}")
    print(f"Hire date: {emp.hire_date}")

    # Product with validation
    try:
        product = Product("Laptop", 999.99, "Electronics", ["portable", "work"])
        print(f"\nValid product: {product}")

        # This will raise an error
        invalid_product = Product("", -100, "Invalid")
    except ValueError as e:
        print(f"Validation error: {e}")


def demo_frozen_dataclasses() -> None:
    """Demonstrate frozen (immutable) dataclasses."""
    print("\n3. Frozen Dataclasses:")
    print("-" * 21)

    # Create immutable point
    point = ImmutablePoint(5.0, 10.0)
    print(f"Immutable point: {point}")

    # Try to modify (this will fail)
    try:
        point.x = 15.0  # This will raise an error
    except Exception as e:
        print(f"Cannot modify frozen dataclass: {type(e).__name__}")

    # Validation in frozen dataclass
    try:
        invalid_point = ImmutablePoint(-1.0, 5.0)
    except ValueError as e:
        print(f"Validation error: {e}")


def demo_post_init_processing() -> None:
    """Demonstrate __post_init__ processing."""
    print("\n4. Post-Init Processing:")
    print("-" * 24)

    # Employee with auto-generated ID
    emp1 = Employee("Jane Smith", "Marketing", 65000.0)
    emp2 = Employee("John Doe", "Engineering", 75000.0)

    print(f"Employee 1 ID: {emp1.employee_id}")
    print(f"Employee 2 ID: {emp2.employee_id}")

    # Product with validation
    try:
        products = [
            Product("iPhone", 999.0, "Electronics"),
            Product("Book", 29.99, "Literature", ["fiction"]),
        ]

        for product in products:
            print(f"Valid product: {product}")

    except ValueError as e:
        print(f"Product validation failed: {e}")


def demo_dataclass_inheritance() -> None:
    """Demonstrate dataclass inheritance."""
    print("\n5. Dataclass Inheritance:")
    print("-" * 25)

    # Create manager (inherits from Employee)
    manager = Manager(
        name="Sarah Connor",
        department="Engineering",
        salary=120000.0,
        skills=["Leadership", "Python", "Architecture"],
        team_size=5,
    )

    print(f"Manager: {manager}")
    print(f"Manager ID: {manager.employee_id}")

    # Add reports
    manager.add_report("Alice Johnson")
    manager.add_report("Bob Wilson")
    manager.add_report("Carol Davis")

    print(f"Team size: {manager.team_size}")
    print(f"Reports: {manager.reports}")

    # Manager is also an Employee
    print(f"Is Employee: {isinstance(manager, Employee)}")
    print(f"Is Manager: {isinstance(manager, Manager)}")
