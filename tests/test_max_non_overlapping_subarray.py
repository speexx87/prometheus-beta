import pytest
from src.max_non_overlapping_subarray import max_non_overlapping_subarray_sum

def test_empty_array():
    """Test empty array returns 0"""
    assert max_non_overlapping_subarray_sum([]) == 0

def test_single_positive_element():
    """Test single positive element returns that element"""
    assert max_non_overlapping_subarray_sum([5]) == 5

def test_single_negative_element():
    """Test single negative element returns 0"""
    assert max_non_overlapping_subarray_sum([-5]) == 0

def test_multiple_positive_elements():
    """Test multiple positive elements"""
    assert max_non_overlapping_subarray_sum([1, 2, 3, 4, 5]) == 9

def test_mixed_elements():
    """Test array with mixed positive and negative elements"""
    assert max_non_overlapping_subarray_sum([-1, 2, 3, -4, 5]) == 7

def test_all_negative_elements():
    """Test array with all negative elements"""
    assert max_non_overlapping_subarray_sum([-1, -2, -3, -4, -5]) == 0

def test_complex_case():
    """Test a more complex case with non-trivial non-overlapping selection"""
    assert max_non_overlapping_subarray_sum([3, -1, 4, -2, 5, -3]) == 10

def test_large_numbers():
    """Test with large numbers"""
    assert max_non_overlapping_subarray_sum([1000, -500, 700, -300, 800]) == 2500

def test_zero_elements():
    """Test array with zero elements"""
    assert max_non_overlapping_subarray_sum([0, 0, 0, 0]) == 0

def test_alternating_signs():
    """Test array with alternating positive and negative signs"""
    assert max_non_overlapping_subarray_sum([1, -1, 2, -2, 3, -3]) == 6