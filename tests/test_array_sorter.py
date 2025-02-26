import pytest
from src.array_sorter import sort_array_with_even_squares

def test_basic_sorting():
    """Test basic array sorting with even square descending"""
    input_arr = [5, 3, 2, 4, 1, 6]
    expected = [1, 3, 5, 36, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_no_even_numbers():
    """Test array with only odd numbers"""
    input_arr = [5, 3, 7, 1]
    expected = [1, 3, 5, 7]
    assert sort_array_with_even_squares(input_arr) == expected

def test_only_even_numbers():
    """Test array with only even numbers"""
    input_arr = [4, 2, 6, 8]
    expected = [64, 36, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_empty_array():
    """Test empty input array"""
    assert sort_array_with_even_squares([]) == []

def test_negative_numbers():
    """Test array with negative numbers"""
    input_arr = [-5, -3, -2, -4, -1, -6]
    expected = [-5, -3, -1, 36, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_mixed_numbers():
    """Test array with mixed positive and negative numbers"""
    input_arr = [-5, 3, -2, 4, 1, -6]
    expected = [-5, 1, 3, 36, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_invalid_input_type():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        sort_array_with_even_squares("not a list")

def test_non_numeric_input():
    """Test input with non-numeric elements"""
    with pytest.raises(ValueError):
        sort_array_with_even_squares([1, 2, 'a', 3])