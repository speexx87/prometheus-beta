import pytest
from src.array_sum import sum_array_elements

def test_sum_array_elements_basic():
    """Test summing a basic list of positive integers."""
    assert sum_array_elements([1, 2, 3, 4]) == 10

def test_sum_array_elements_empty():
    """Test summing an empty list."""
    assert sum_array_elements([]) == 0

def test_sum_array_elements_negative():
    """Test summing a list with negative integers."""
    assert sum_array_elements([-1, -2, -3]) == -6

def test_sum_array_elements_mixed():
    """Test summing a list with positive and negative integers."""
    assert sum_array_elements([-1, 0, 1]) == 0

def test_sum_array_elements_single_element():
    """Test summing a list with a single element."""
    assert sum_array_elements([42]) == 42

def test_sum_array_elements_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_array_elements(42)

def test_sum_array_elements_non_integer_elements():
    """Test that a list with non-integer elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_array_elements([1, 2, '3'])