import pytest
from src.string_converter import convert_to_lowercase_with_spaces

def test_convert_normal_string():
    """Test conversion of a normal string."""
    assert convert_to_lowercase_with_spaces("Hello World") == "hello world"

def test_convert_mixed_case():
    """Test conversion of a mixed case string."""
    assert convert_to_lowercase_with_spaces("HeLLo WoRLD") == "hello world"

def test_convert_with_extra_spaces():
    """Test conversion of a string with extra spaces."""
    assert convert_to_lowercase_with_spaces("  Hello   World  ") == "hello world"

def test_convert_single_word():
    """Test conversion of a single word."""
    assert convert_to_lowercase_with_spaces("HELLO") == "hello"

def test_convert_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_lowercase_with_spaces("") == ""

def test_convert_with_numbers_and_symbols():
    """Test conversion of a string with numbers and symbols."""
    assert convert_to_lowercase_with_spaces("Hello123 World!@#") == "hello123 world"

def test_input_type_error():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_lowercase_with_spaces(None)