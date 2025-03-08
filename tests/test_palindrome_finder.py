import pytest
from src.palindrome_finder import find_palindrome_substrings

def test_basic_palindrome_detection():
    """Test basic palindrome substring detection."""
    result = find_palindrome_substrings("abcba")
    assert result == ["abcba", "bcb"]

def test_multiple_palindromes():
    """Test finding multiple palindrome substrings."""
    result = find_palindrome_substrings("aabaa")
    assert result == ["aabaa", "aba", "aa"]

def test_no_palindromes():
    """Test string with no palindrome substrings."""
    result = find_palindrome_substrings("abcd")
    assert result == []

def test_empty_string():
    """Test empty string input."""
    result = find_palindrome_substrings("")
    assert result == []

def test_single_char_string():
    """Test string with single character."""
    result = find_palindrome_substrings("a")
    assert result == []

def test_invalid_input():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_palindrome_substrings(123)

def test_complex_palindrome_detection():
    """Test more complex palindrome detection."""
    result = find_palindrome_substrings("racecar")
    assert result == ["racecar", "aceca", "cec"]

def test_sorting_order():
    """Test sorting of palindrome substrings."""
    result = find_palindrome_substrings("abbaxyzzyx")
    # Expected: sorted by length (descending), then alphabetically
    assert result == ["xyzzyx", "yzzy", "abba", "zz", "bb"]