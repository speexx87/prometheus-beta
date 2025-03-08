import pytest
from src.arithmetic_sort import arithmetic_sort

def test_basic_sorting():
    """Test sorting a list of positive integers"""
    input_list = [5, 2, 8, 12, 1, 6]
    expected = [1, 2, 5, 6, 8, 12]
    assert arithmetic_sort(input_list) == expected

def test_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == input_list

def test_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert arithmetic_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert arithmetic_sort(input_list) == [42]

def test_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert arithmetic_sort(input_list) == expected

def test_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 2, -8, 12, 1, -6]
    expected = [-8, -6, -5, 1, 2, 12]
    assert arithmetic_sort(input_list) == expected

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        arithmetic_sort(42)

def test_invalid_element_type():
    """Test that a TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        arithmetic_sort([1, 2, "3", 4])