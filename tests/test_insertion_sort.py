import pytest
from src.insertion_sort import insertion_sort

def test_insertion_sort_normal_list():
    """Test sorting a normal list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert insertion_sort(input_list) == expected
    assert input_list == expected  # Ensure in-place sorting

def test_insertion_sort_empty_list():
    """Test sorting an empty list."""
    assert insertion_sort([]) == []

def test_insertion_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert insertion_sort(input_list) == [42]

def test_insertion_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert insertion_sort(input_list) == [1, 2, 3, 4, 5]

def test_insertion_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    assert insertion_sort(input_list) == [1, 2, 3, 4, 5]

def test_insertion_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = sorted(input_list)
    assert insertion_sort(input_list) == expected

def test_insertion_sort_with_floats():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert insertion_sort(input_list) == sorted(input_list)

def test_insertion_sort_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort(None)

def test_insertion_sort_mixed_types():
    """Test sorting raises TypeError for non-comparable types."""
    with pytest.raises(TypeError):
        insertion_sort([1, "a", 3, "b"])