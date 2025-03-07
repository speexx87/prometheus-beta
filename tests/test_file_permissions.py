import os
import pytest
import tempfile
import stat

from src.file_permissions import change_file_permissions

def test_change_file_permissions_success():
    """Test successful file permission change."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        
        # Initial permissions (default is typically 0o644)
        initial_mode = os.stat(temp_path).st_mode & 0o777
        assert initial_mode == 0o644
        
        # Change permissions to read-only for owner
        change_file_permissions(temp_path, 0o400)
        
        # Verify new permissions
        new_mode = os.stat(temp_path).st_mode & 0o777
        assert new_mode == 0o400
        
        # Clean up
        os.unlink(temp_path)

def test_change_file_permissions_invalid_file():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        change_file_permissions("/path/to/nonexistent/file", 0o755)

def test_change_file_permissions_invalid_mode():
    """Test handling of invalid permission modes."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        
        # Test negative mode
        with pytest.raises(ValueError):
            change_file_permissions(temp_path, -1)
        
        # Test mode exceeding max octal value
        with pytest.raises(ValueError):
            change_file_permissions(temp_path, 0o1000)
        
        # Clean up
        os.unlink(temp_path)

def test_change_file_permissions_invalid_input_types():
    """Test handling of incorrect input types."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        
        # Test non-string file path
        with pytest.raises(TypeError):
            change_file_permissions(123, 0o755)
        
        # Test non-integer mode
        with pytest.raises(TypeError):
            change_file_permissions(temp_path, "755")
        
        # Clean up
        os.unlink(temp_path)

def test_change_file_permissions_return_value():
    """Test the return value of the function."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        
        # Verify function returns True on successful permission change
        result = change_file_permissions(temp_path, 0o666)
        assert result is True
        
        # Clean up
        os.unlink(temp_path)