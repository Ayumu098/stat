"""Test the functions in the module1 module."""

from pytemp.module import add, divide, multiply, subtract


def test_add():
    """Test the add function."""
    assert add(1, 2) == 3


def test_subtract():
    """Test the subtract function."""
    assert subtract(2, 1) == 1


def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6


def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
