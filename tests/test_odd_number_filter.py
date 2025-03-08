import pytest
from src.odd_number_filter import filter_odd_numbers

def test_filter_odd_numbers_basic():
    """Test basic functionality of filtering and sorting odd numbers."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert filter_odd_numbers(input_list) == [1, 3, 5, 7, 9]

def test_filter_odd_numbers_empty_list():
    """Test filtering an empty list."""
    assert filter_odd_numbers([]) == []

def test_filter_odd_numbers_no_odds():
    """Test a list with no odd numbers."""
    assert filter_odd_numbers([2, 4, 6, 8]) == []

def test_filter_odd_numbers_negative():
    """Test filtering with negative numbers."""
    input_list = [-1, -2, -3, 0, 1, 2, 3]
    assert filter_odd_numbers(input_list) == [-3, -1, 1, 3]

def test_filter_odd_numbers_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_odd_numbers("not a list")

def test_filter_odd_numbers_invalid_element_type():
    """Test raising TypeError for list with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_odd_numbers([1, 2, "3", 4])

def test_filter_odd_numbers_large_numbers():
    """Test with large numbers."""
    input_list = [10001, 10002, 10003, 10004, 10005]
    assert filter_odd_numbers(input_list) == [10001, 10003, 10005]