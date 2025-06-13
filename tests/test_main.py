"""
Tests for the main module.
"""

import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import demo_function


def test_demo_function():
    """Test that demo_function runs without errors."""
    # This is a basic test - in real projects, you'd test actual functionality
    try:
        demo_function()
        assert True  # If we get here, the function ran successfully
    except Exception as e:
        pytest.fail(f"demo_function raised an exception: {e}")


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
