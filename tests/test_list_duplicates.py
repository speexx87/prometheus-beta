import pytest
from src.list_duplicates import find_duplicates

def test_find_duplicates_basic():
    """Test basic duplicate detection"""
    assert find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]) == [2, 3]

def test_find_duplicates_multiple_duplicates():
    """Test list with multiple duplicates of the same number"""
    assert find_duplicates([1, 1, 1, 2, 2]) == [1, 2]

def test_find_duplicates_empty_list():
    """Test empty list returns empty list"""
    assert find_duplicates([]) == []

def test_find_duplicates_no_duplicates():
    """Test list with no duplicates returns empty list"""
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_find_duplicates_negative_numbers():
    """Test list with negative numbers"""
    assert find_duplicates([-1, -1, 2, 3, -1, 4]) == [-1]

def test_find_duplicates_large_list():
    """Test large list with duplicates"""
    large_list = [1] * 10 + [2] * 5 + [3] * 3 + list(range(4, 100))
    assert find_duplicates(large_list) == [1, 2, 3]