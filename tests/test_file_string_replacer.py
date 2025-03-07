"""
Test suite for file_string_replacer module.

This module contains comprehensive tests for the replace_string_in_file function.
"""

import os
import pytest
import tempfile
from src.file_string_replacer import replace_string_in_file


def test_basic_string_replacement():
    """Test basic string replacement functionality."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello world, hello universe")
        temp_file.close()
        
        replacements = replace_string_in_file(temp_file.name, "hello", "hi")
        
        with open(temp_file.name, 'r') as f:
            content = f.read()
        
        os.unlink(temp_file.name)
        
        assert replacements == 2
        assert content == "Hello world, hi universe"


def test_no_replacements():
    """Test when no replacements are made."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello world")
        temp_file.close()
        
        replacements = replace_string_in_file(temp_file.name, "universe", "galaxy")
        
        with open(temp_file.name, 'r') as f:
            content = f.read()
        
        os.unlink(temp_file.name)
        
        assert replacements == 0
        assert content == "Hello world"


def test_case_sensitive_replacement():
    """Test case-sensitive replacement."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello HELLO hello")
        temp_file.close()
        
        replacements = replace_string_in_file(temp_file.name, "hello", "hi")
        
        with open(temp_file.name, 'r') as f:
            content = f.read()
        
        os.unlink(temp_file.name)
        
        assert replacements == 1
        assert content == "Hello HELLO hi"


def test_empty_replacement():
    """Test replacement with empty string."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello world")
        temp_file.close()
        
        replacements = replace_string_in_file(temp_file.name, "world", "")
        
        with open(temp_file.name, 'r') as f:
            content = f.read()
        
        os.unlink(temp_file.name)
        
        assert replacements == 1
        assert content == "Hello "


def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("nonexistent_file.txt", "test", "replacement")


def test_invalid_input_types():
    """Test input type validation."""
    with pytest.raises(TypeError):
        replace_string_in_file(123, "test", "replacement")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", 123, "replacement")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", "test", 123)


def test_empty_input_validation():
    """Test empty input validation."""
    with pytest.raises(ValueError):
        replace_string_in_file("", "test", "replacement")
    
    with pytest.raises(ValueError):
        replace_string_in_file("file.txt", "", "replacement")