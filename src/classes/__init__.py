"""Classes sub-package for Python 3.12 class feature demonstrations.

This package demonstrates comprehensive class features available in Python 3.12,
including basic classes, inheritance, special methods, iterators, generators,
dataclasses, and advanced features.
"""

from classes.advanced_features import demo_advanced_features
from classes.basic_classes import demo_basic_classes
from classes.dataclasses_demo import demo_dataclasses
from classes.inheritance import demo_inheritance
from classes.iterators_generators import demo_iterators_generators
from classes.special_methods import demo_special_methods

__version__ = "0.1.0"

__all__ = [
    "demo_basic_classes",
    "demo_inheritance",
    "demo_special_methods",
    "demo_iterators_generators",
    "demo_dataclasses",
    "demo_advanced_features",
    "demo_classes",
]


def demo_classes() -> None:
    """Demonstrate all Python 3.12 class features."""
    print("=" * 60)
    print("PYTHON 3.12 CLASS FEATURES DEMONSTRATION")
    print("=" * 60)

    demo_basic_classes()
    demo_inheritance()
    demo_special_methods()
    demo_iterators_generators()
    demo_dataclasses()
    demo_advanced_features()

    print("=" * 60)
    print("CLASS DEMONSTRATIONS COMPLETED")
    print("=" * 60)
