import pytest
from src.array_transform import transform_array

def test_transform_array_basic():
    """Test basic functionality of array transformation"""
    assert transform_array([0, 1, 2, 3]) == [0, 2, 5, 10]

def test_transform_array_empty():
    """Test transformation of an empty array"""
    assert transform_array([]) == []

def test_transform_array_zeros():
    """Test array with only zeros"""
    assert transform_array([0, 0, 0]) == [0, 0, 0]

def test_transform_array_large_numbers():
    """Test array with larger numbers"""
    assert transform_array([0, 10, 20]) == [0, 101, 401]

def test_transform_array_invalid_input_negative():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        transform_array([-1, 2, 3])

def test_transform_array_invalid_input_type():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        transform_array("not a list")

def test_transform_array_invalid_element_type():
    """Test that non-integer elements raise a ValueError"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        transform_array([1, 2, "3"])