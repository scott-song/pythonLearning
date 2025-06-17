"""
Inheritance demonstrations for Python 3.12.

This module demonstrates inheritance concepts including:
- Single inheritance
- Multiple inheritance
- Method resolution order (MRO)
- super() usage
- Abstract base classes
- Polymorphism
"""

from abc import ABC, abstractmethod
from typing import Any, List


# Base classes for single inheritance
class Animal:
    """Base class for all animals."""

    def __init__(self, name: str, species: str) -> None:
        """Initialize an animal with name and species."""
        self.name = name
        self.species = species
        self.alive = True

    def make_sound(self) -> str:
        """Make a generic animal sound."""
        return "Some animal sound"

    def eat(self, food: str) -> None:
        """Animal eating behavior."""
        print(f"{self.name} the {self.species} is eating {food}")

    def sleep(self) -> None:
        """Animal sleeping behavior."""
        print(f"{self.name} is sleeping")

    def __str__(self) -> str:
        """Return string representation of animal."""
        return f"{self.species} named {self.name}"


class Mammal(Animal):
    """Mammal class inheriting from Animal."""

    def __init__(self, name: str, species: str, fur_color: str) -> None:
        """Initialize a mammal with additional fur color."""
        super().__init__(name, species)
        self.fur_color = fur_color
        self.warm_blooded = True

    def give_birth(self) -> None:
        """Mammal-specific behavior."""
        print(f"{self.name} gives birth to live young")

    def __str__(self) -> str:
        """Return string representation of mammal."""
        return f"{super().__str__()} with {self.fur_color} fur"


class Dog(Mammal):
    """Dog class inheriting from Mammal."""

    def __init__(self, name: str, breed: str, fur_color: str) -> None:
        """Initialize a dog with breed information."""
        super().__init__(name, "Dog", fur_color)
        self.breed = breed
        self.loyalty = 100

    def make_sound(self) -> str:
        """Override the make_sound method for dogs."""
        return "Woof! Woof!"

    def fetch(self, item: str) -> None:
        """Dog-specific behavior."""
        print(f"{self.name} fetches the {item}")

    def wag_tail(self) -> None:
        """Dog-specific behavior."""
        print(f"{self.name} wags tail happily")

    def __str__(self) -> str:
        """Return string representation of dog."""
        return f"{self.breed} dog named {self.name} with {self.fur_color} fur"


class Cat(Mammal):
    """Cat class inheriting from Mammal."""

    def __init__(self, name: str, fur_color: str, indoor: bool = True) -> None:
        """Initialize a cat."""
        super().__init__(name, "Cat", fur_color)
        self.indoor = indoor
        self.independence = 90

    def make_sound(self) -> str:
        """Override the make_sound method for cats."""
        return "Meow"

    def purr(self) -> None:
        """Cat-specific behavior."""
        print(f"{self.name} purrs contentedly")

    def climb(self) -> None:
        """Cat-specific behavior."""
        print(f"{self.name} climbs up high")


# Multiple inheritance example
class Flyable:
    """Mixin class for flying behavior."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize flyable with proper super() call."""
        super().__init__(*args, **kwargs)
        self.can_fly = True
        self.altitude = 0

    def fly(self) -> None:
        """Flying behavior."""
        self.altitude = 1000
        print(f"Flying at altitude {self.altitude} feet")

    def land(self) -> None:
        """Landing behavior."""
        self.altitude = 0
        print("Landing on the ground")


class Swimmable:
    """Mixin class for swimming behavior."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize swimmable with proper super() call."""
        super().__init__(*args, **kwargs)
        self.can_swim = True
        self.depth = 0

    def swim(self) -> None:
        """Swimming behavior."""
        self.depth = 10
        print(f"Swimming at depth {self.depth} feet")

    def surface(self) -> None:
        """Surface behavior."""
        self.depth = 0
        print("Surfacing to breathe")


class Duck(Animal, Flyable, Swimmable):
    """Duck class demonstrating multiple inheritance."""

    def __init__(self, name: str) -> None:
        """Initialize a duck with multiple inheritance."""
        super().__init__(name, "Duck")

    def make_sound(self) -> str:
        """Override the make_sound method for ducks."""
        return "Quack! Quack!"

    def dabble(self) -> None:
        """Duck-specific feeding behavior."""
        print(f"{self.name} dabbles for food in the water")


# Abstract base class example
class Shape(ABC):
    """Abstract base class for geometric shapes."""

    def __init__(self, name: str) -> None:
        """Initialize shape with name."""
        self.name = name

    @abstractmethod
    def area(self) -> float:
        """Calculate area - must be implemented by subclasses."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter - must be implemented by subclasses."""
        pass

    def describe(self) -> str:
        """Describe the shape."""
        return f"This is a {self.name} with area {self.area():.2f} and perimeter {self.perimeter():.2f}"


class Circle(Shape):
    """Circle implementation of Shape."""

    def __init__(self, radius: float) -> None:
        """Initialize circle with radius."""
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        """Calculate circle area."""
        return 3.14159 * self.radius**2

    def perimeter(self) -> float:
        """Calculate circle perimeter (circumference)."""
        return 2 * 3.14159 * self.radius


class Triangle(Shape):
    """Triangle implementation of Shape."""

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        """Initialize triangle with three sides."""
        super().__init__("Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self) -> float:
        """Calculate triangle area using Heron's formula."""
        s = self.perimeter() / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    def perimeter(self) -> float:
        """Calculate triangle perimeter."""
        return self.side_a + self.side_b + self.side_c


def demo_inheritance() -> None:
    """Demonstrate inheritance concepts."""
    print("\n" + "=" * 50)
    print("INHERITANCE DEMONSTRATION")
    print("=" * 50)

    demo_single_inheritance()
    demo_method_overriding()
    demo_multiple_inheritance()
    demo_method_resolution_order()
    demo_abstract_classes()
    demo_polymorphism()


def demo_single_inheritance() -> None:
    """Demonstrate single inheritance chain."""
    print("\n1. Single Inheritance Chain:")
    print("-" * 28)

    # Create instances at different levels
    generic_animal = Animal("Generic", "Unknown Species")
    mammal = Mammal("Fluffy", "Generic Mammal", "brown")
    dog = Dog("Buddy", "Golden Retriever", "golden")
    cat = Cat("Whiskers", "gray", indoor=True)

    print(f"Animal: {generic_animal}")
    print(f"Mammal: {mammal}")
    print(f"Dog: {dog}")
    print(f"Cat: {cat}")

    # Show inherited behaviors
    print(f"\nSounds:")
    print(f"Generic animal: {generic_animal.make_sound()}")
    print(f"Dog: {dog.make_sound()}")
    print(f"Cat: {cat.make_sound()}")


def demo_method_overriding() -> None:
    """Demonstrate method overriding."""
    print("\n2. Method Overriding:")
    print("-" * 20)

    animals = [
        Animal("Generic", "Unknown"),
        Dog("Rex", "German Shepherd", "brown"),
        Cat("Mittens", "black"),
    ]

    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")


def demo_multiple_inheritance() -> None:
    """Demonstrate multiple inheritance."""
    print("\n3. Multiple Inheritance:")
    print("-" * 23)

    duck = Duck("Donald")
    print(f"Duck: {duck}")
    print(f"Sound: {duck.make_sound()}")

    # Use inherited methods from multiple parents
    duck.fly()
    duck.swim()
    duck.dabble()
    duck.land()
    duck.surface()

    # Check attributes from multiple inheritance
    print(f"Can fly: {hasattr(duck, 'can_fly') and duck.can_fly}")
    print(f"Can swim: {hasattr(duck, 'can_swim') and duck.can_swim}")


def demo_method_resolution_order() -> None:
    """Demonstrate Method Resolution Order (MRO)."""
    print("\n4. Method Resolution Order (MRO):")
    print("-" * 34)

    print("Duck MRO:")
    for i, cls in enumerate(Duck.__mro__):
        print(f"  {i + 1}. {cls.__name__}")

    print("\nDog MRO:")
    for i, cls in enumerate(Dog.__mro__):
        print(f"  {i + 1}. {cls.__name__}")


def demo_abstract_classes() -> None:
    """Demonstrate abstract base classes."""
    print("\n5. Abstract Base Classes:")
    print("-" * 24)

    # Create concrete implementations
    circle = Circle(5.0)
    triangle = Triangle(3.0, 4.0, 5.0)

    shapes: List[Shape] = [circle, triangle]

    for shape in shapes:
        print(shape.describe())

    # Trying to instantiate abstract class would raise TypeError:
    # shape = Shape("Generic")  # This would fail


def demo_polymorphism() -> None:
    """Demonstrate polymorphism."""
    print("\n6. Polymorphism:")
    print("-" * 14)

    # Same interface, different implementations
    animals: List[Animal] = [
        Dog("Fido", "Labrador", "yellow"),
        Cat("Shadow", "black"),
        Duck("Quackers"),
    ]

    print("All animals making sounds:")
    for animal in animals:
        print(f"{animal.name} ({animal.species}): {animal.make_sound()}")

    print("\nAll animals eating:")
    for animal in animals:
        animal.eat("food")

    # Demonstrate isinstance and type checking
    print("\nType checking:")
    for animal in animals:
        print(f"{animal.name} is Animal: {isinstance(animal, Animal)}")
        print(f"{animal.name} is Mammal: {isinstance(animal, Mammal)}")
        if isinstance(animal, Duck):
            can_fly = hasattr(animal, "can_fly") and animal.can_fly
            print(f"{animal.name} can fly: {can_fly}")
