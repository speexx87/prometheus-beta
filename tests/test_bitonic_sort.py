import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bitonic_sort import bitonic_sort

def test_bitonic_sort_ascending():
    """Test bitonic sort in ascending order"""
    input_list = [3, 7, 1, 9, 2, 5]
    expected = sorted(input_list)
    result = bitonic_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_bitonic_sort_descending():
    """Test bitonic sort in descending order"""
    input_list = [3, 7, 1, 9, 2, 5]
    expected = sorted(input_list, reverse=True)
    result = bitonic_sort(input_list, ascending=False)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_bitonic_sort_empty_list():
    """Test bitonic sort with an empty list"""
    assert bitonic_sort([]) == [], "Should return an empty list"

def test_bitonic_sort_single_element():
    """Test bitonic sort with a single element"""
    single_element = [42]
    assert bitonic_sort(single_element) == single_element, "Should return the same single-element list"

def test_bitonic_sort_duplicate_elements():
    """Test bitonic sort with duplicate elements"""
    input_list = [3, 3, 1, 7, 1, 5]
    expected = sorted(input_list)
    result = bitonic_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_bitonic_sort_negative_numbers():
    """Test bitonic sort with negative numbers"""
    input_list = [-3, 7, -1, 9, -2, 5]
    expected = sorted(input_list)
    result = bitonic_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_bitonic_sort_float_numbers():
    """Test bitonic sort with floating-point numbers"""
    input_list = [3.14, 1.1, 2.2, 0.5, 4.4]
    expected = sorted(input_list)
    result = bitonic_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_bitonic_sort_invalid_input():
    """Test bitonic sort with invalid input"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")
    
    with pytest.raises(TypeError):
        bitonic_sort(None)