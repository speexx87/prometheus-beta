import pytest
from src.string_case_converter import to_alternating_path_case

def test_basic_conversion():
    """Test basic string conversion"""
    assert to_alternating_path_case("hello world") == "hello-World"
    assert to_alternating_path_case("PYTHON PROGRAMMING") == "python-Programming"

def test_multiple_separators():
    """Test conversion with multiple separators"""
    assert to_alternating_path_case("snake_case example") == "snake-Case-Example"
    assert to_alternating_path_case("kebab-case_mixed test") == "kebab-Case-Mixed-Test"

def test_empty_input():
    """Test empty input"""
    assert to_alternating_path_case("") == ""
    assert to_alternating_path_case("   ") == ""

def test_single_word():
    """Test single word conversion"""
    assert to_alternating_path_case("hello") == "hello"
    assert to_alternating_path_case("HELLO") == "hello"

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        to_alternating_path_case(None)
    
    with pytest.raises(TypeError):
        to_alternating_path_case(123)

def test_complex_cases():
    """Test more complex input scenarios"""
    assert to_alternating_path_case("  Hello   World  ") == "hello-World"
    assert to_alternating_path_case("MULTI__SEPARATOR_TEST") == "multi-Separator-Test"
    assert to_alternating_path_case("a b c d e") == "a-B-C-D-E"