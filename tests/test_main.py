"""
Tests for the main module.
"""

import pytest
import sys
import os
from src.main import demo_function

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


def test_demo_function():
    """Test that demo_function runs without errors."""
    # This is a basic test - in real projects, you'd test actual functionality
    demo_function()  # If this doesn't raise an exception, the test passes


def test_basic_python_features():
    """Test some basic Python features."""
    # Test list operations
    fruits = ["apple", "banana", "orange"]
    assert len(fruits) == 3
    assert "apple" in fruits

    # Test dictionary operations
    fruit_dict = {"apple": 5, "banana": 6}
    assert fruit_dict["apple"] == 5
    assert "banana" in fruit_dict


if __name__ == "__main__":
    pytest.main([__file__])
