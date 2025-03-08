import pytest
from src.substring_generator import generate_all_substrings

def test_generate_all_substrings_basic():
    """Test substring generation for a simple string."""
    result = generate_all_substrings("abc")
    expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == sorted(expected)

def test_generate_all_substrings_empty():
    """Test substring generation for an empty string."""
    assert generate_all_substrings("") == []

def test_generate_all_substrings_single_char():
    """Test substring generation for a single character string."""
    result = generate_all_substrings("x")
    assert result == ['x']

def test_generate_all_substrings_different_lengths():
    """Test substring generation for strings of different lengths."""
    result = generate_all_substrings("hello")
    expected = [
        'h', 'he', 'hel', 'hell', 'hello', 
        'e', 'el', 'ell', 'ello', 
        'l', 'll', 'llo', 
        'l', 'lo', 
        'o'
    ]
    assert sorted(result) == sorted(expected)

def test_generate_all_substrings_special_characters():
    """Test substring generation with special characters and spaces."""
    result = generate_all_substrings("a!b c")
    expected = ['a', 'a!', 'a!b', 'a!b ', 'a!b c', 
                '!', '!b', '!b ', '!b c', 
                'b', 'b ', 'b c', 
                ' ', ' c', 
                'c']
    assert sorted(result) == sorted(expected)

def test_generate_all_substrings_type_error():
    """Test that the function raises a TypeError for non-string input."""
    with pytest.raises(TypeError):
        generate_all_substrings(123)