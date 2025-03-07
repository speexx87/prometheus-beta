import os
import pytest
import tempfile
import shutil

from src.directory_utils import create_directory


def test_create_directory_success():
    """Test creating a new directory successfully"""
    with tempfile.TemporaryDirectory() as temp_base_dir:
        new_dir_path = os.path.join(temp_base_dir, 'new_test_dir')
        result = create_directory(new_dir_path)
        
        assert result is True
        assert os.path.exists(new_dir_path)
        assert os.path.isdir(new_dir_path)


def test_create_directory_already_exists():
    """Test attempting to create an existing directory"""
    with tempfile.TemporaryDirectory() as temp_base_dir:
        existing_dir = os.path.join(temp_base_dir, 'existing_dir')
        os.mkdir(existing_dir)
        
        result = create_directory(existing_dir)
        assert result is False


def test_create_directory_nested():
    """Test creating nested directories"""
    with tempfile.TemporaryDirectory() as temp_base_dir:
        nested_dir_path = os.path.join(temp_base_dir, 'parent', 'child', 'grandchild')
        result = create_directory(nested_dir_path)
        
        assert result is True
        assert os.path.exists(nested_dir_path)
        assert os.path.isdir(nested_dir_path)


def test_create_directory_permission_error(monkeypatch):
    """Test handling permission errors"""
    def mock_makedirs(*args, **kwargs):
        raise PermissionError("Mock permission denied")
    
    monkeypatch.setattr(os, 'makedirs', mock_makedirs)
    
    with pytest.raises(PermissionError, match="Insufficient permissions"):
        create_directory('/root/impossible/path')


def test_create_directory_invalid_path():
    """Test creating directory with invalid path characters"""
    with pytest.raises(ValueError, match="Invalid characters in filename"):
        create_directory('invalid:path')


def test_create_directory_permission_mode():
    """Test creating directory with specific permission mode"""
    with tempfile.TemporaryDirectory() as temp_base_dir:
        new_dir_path = os.path.join(temp_base_dir, 'mode_test_dir')
        result = create_directory(new_dir_path, mode=0o700)
        
        assert result is True
        assert os.path.exists(new_dir_path)
        
        # Check file mode (Python's os.stat returns octal representation)
        dir_mode = oct(os.stat(new_dir_path).st_mode)[-3:]
        assert dir_mode == '700'