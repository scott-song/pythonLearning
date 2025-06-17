"""
Basic class demonstrations for Python 3.12.

This module demonstrates fundamental class concepts including:
- Class definition syntax
- Class and instance objects
- Method objects
- Class and instance variables
- Basic object-oriented programming patterns
"""

from typing import List


class Person:
    """A basic class representing a person."""

    # Class variable - shared by all instances
    species = "Homo sapiens"
    population_count = 0

    def __init__(self, name: str, age: int) -> None:
        """Initialize a new Person instance."""
        # Instance variables - unique to each instance
        self.name = name
        self.age = age

        # Increment class variable when new instance is created
        Person.population_count += 1

    def introduce(self) -> str:
        """Return a greeting message."""
        return f"Hello, I'm {self.name} and I'm {self.age} years old."

    def have_birthday(self) -> None:
        """Increment age by one year."""
        self.age += 1
        print(f"Happy birthday {self.name}! Now {self.age} years old.")

    def __str__(self) -> str:
        """Return string representation of the person."""
        return f"Person(name='{self.name}', age={self.age})"

    @classmethod
    def get_population(cls) -> int:
        """Return the total population count."""
        return cls.population_count

    @staticmethod
    def is_adult(age: int) -> bool:
        """Check if age represents an adult (18 or older)."""
        return age >= 18


class BankAccount:
    """A class demonstrating encapsulation and methods."""

    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        """Initialize a bank account."""
        self.account_holder = account_holder
        self._balance = initial_balance  # Private-ish variable
        self._transactions: List[str] = []

    def deposit(self, amount: float) -> None:
        """Deposit money to the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        self._transactions.append(f"Deposited ${amount:.2f}")
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")

    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self._balance:
            print(f"Insufficient funds. Balance: ${self._balance:.2f}")
            return False

        self._balance -= amount
        self._transactions.append(f"Withdrew ${amount:.2f}")
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True

    def get_balance(self) -> float:
        """Get current account balance."""
        return self._balance

    def get_transaction_history(self) -> List[str]:
        """Get copy of transaction history."""
        return self._transactions.copy()

    def __str__(self) -> str:
        """Return string representation of the account."""
        return (
            f"BankAccount(holder='{self.account_holder}', balance=${self._balance:.2f})"
        )


class Rectangle:
    """A class demonstrating properties and computed attributes."""

    def __init__(self, width: float, height: float) -> None:
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    @property
    def is_square(self) -> bool:
        """Check if the rectangle is a square."""
        return self.width == self.height

    def scale(self, factor: float) -> None:
        """Scale the rectangle by a given factor."""
        self.width *= factor
        self.height *= factor

    def __str__(self) -> str:
        """Return string representation of the rectangle."""
        return f"Rectangle({self.width}x{self.height})"


def demo_basic_classes() -> None:
    """Demonstrate basic class concepts."""
    print("\n" + "=" * 50)
    print("BASIC CLASSES DEMONSTRATION")
    print("=" * 50)

    demo_person_class()
    demo_bank_account_class()
    demo_rectangle_class()
    demo_class_vs_instance_variables()


def demo_person_class() -> None:
    """Demonstrate the Person class."""
    print("\n1. Person Class Demonstration:")
    print("-" * 30)

    # Create instances
    alice = Person("Alice", 30)
    bob = Person("Bob", 25)

    # Instance methods
    print(alice.introduce())
    print(bob.introduce())

    # Modify instance data
    alice.have_birthday()

    # String representation
    print(f"Alice: {alice}")
    print(f"Bob: {bob}")

    # Class methods and static methods
    print(f"Species: {Person.species}")
    print(f"Population: {Person.get_population()}")
    print(f"Is Alice an adult? {Person.is_adult(alice.age)}")
    print(f"Is a 16-year-old an adult? {Person.is_adult(16)}")


def demo_bank_account_class() -> None:
    """Demonstrate the BankAccount class."""
    print("\n2. Bank Account Class Demonstration:")
    print("-" * 35)

    # Create account
    account = BankAccount("John Doe", 1000.0)
    print(f"Initial account: {account}")

    # Perform transactions
    account.deposit(500.0)
    account.withdraw(200.0)
    account.withdraw(2000.0)  # Should fail

    # Check balance and history
    print(f"Final balance: ${account.get_balance():.2f}")
    print("Transaction history:")
    for transaction in account.get_transaction_history():
        print(f"  - {transaction}")


def demo_rectangle_class() -> None:
    """Demonstrate the Rectangle class with properties."""
    print("\n3. Rectangle Class with Properties:")
    print("-" * 33)

    # Create rectangle
    rect = Rectangle(4.0, 6.0)
    print(f"Rectangle: {rect}")
    print(f"Area: {rect.area}")
    print(f"Perimeter: {rect.perimeter}")
    print(f"Is square? {rect.is_square}")

    # Create square
    square = Rectangle(5.0, 5.0)
    print(f"\nSquare: {square}")
    print(f"Area: {square.area}")
    print(f"Is square? {square.is_square}")

    # Scale rectangle
    rect.scale(2.0)
    print(f"\nAfter scaling by 2: {rect}")
    print(f"New area: {rect.area}")


def demo_class_vs_instance_variables() -> None:
    """Demonstrate class vs instance variables."""
    print("\n4. Class vs Instance Variables:")
    print("-" * 32)

    # Show initial population
    print(f"Initial population: {Person.get_population()}")

    # Create more instances
    charlie = Person("Charlie", 35)
    diana = Person("Diana", 28)

    print(f"After creating Charlie and Diana: {Person.get_population()}")

    # Show shared class variable
    print(f"Charlie's species: {charlie.species}")
    print(f"Diana's species: {diana.species}")

    # Modify class variable
    Person.species = "Homo sapiens sapiens"
    print(f"After updating species:")
    print(f"Charlie's species: {charlie.species}")
    print(f"Diana's species: {diana.species}")

    # Instance variables are independent
    charlie.name = "Charles"
    print(f"Charlie's name changed to: {charlie.name}")
    print(f"Diana's name unchanged: {diana.name}")
