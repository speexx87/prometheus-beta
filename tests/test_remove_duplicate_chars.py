import pytest
from src.remove_duplicate_chars import remove_chars_over_twice

def test_remove_duplicate_chars_basic():
    """Test basic functionality of removing chars over twice"""
    assert remove_chars_over_twice("aabbbcccc") == "aabbcc"
    assert remove_chars_over_twice("hello") == "hello"

def test_remove_duplicate_chars_empty_string():
    """Test handling of empty string"""
    assert remove_chars_over_twice("") == ""

def test_remove_duplicate_chars_single_chars():
    """Test strings with single or no repeating characters"""
    assert remove_chars_over_twice("abcde") == "abcde"
    assert remove_chars_over_twice("aabbccddee") == "aabbccddee"

def test_remove_duplicate_chars_multiple_repeats():
    """Test strings with multiple repeated characters"""
    assert remove_chars_over_twice("aaabbbcccddd") == "aabbccdd"
    assert remove_chars_over_twice("aaaaabbbbbccccc") == "aabbcc"

def test_remove_duplicate_chars_mixed_repeats():
    """Test strings with mixed repeat patterns"""
    assert remove_chars_over_twice("aabbccddeeefff") == "aabbccddeeff"

def test_invalid_input_type():
    """Test handling of non-string inputs"""
    with pytest.raises(TypeError):
        remove_chars_over_twice(123)
    with pytest.raises(TypeError):
        remove_chars_over_twice(None)
    with pytest.raises(TypeError):
        remove_chars_over_twice(["a", "b", "c"])