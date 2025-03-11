import pytest
from src.most_frequent_char import find_most_frequent_character

def test_basic_most_frequent_character():
    """Test finding the most frequent character in a simple string."""
    assert find_most_frequent_character("hello") == 'l'

def test_multiple_same_frequency():
    """Test when multiple characters have same frequency."""
    result = find_most_frequent_character("aabbc")
    assert result in ['a', 'b']

def test_empty_string():
    """Test behavior with an empty string."""
    assert find_most_frequent_character("") is None

def test_single_character():
    """Test with a single character string."""
    assert find_most_frequent_character("x") == 'x'

def test_all_unique_characters():
    """Test when all characters appear once."""
    result = find_most_frequent_character("abcde")
    assert result in 'abcde'

def test_invalid_input_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_most_frequent_character(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        find_most_frequent_character(None)

def test_string_with_spaces_and_special_chars():
    """Test with a string containing spaces and special characters."""
    assert find_most_frequent_character("hello world!!") == 'l'