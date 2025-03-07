import os
import tarfile
import pytest
import tempfile
import shutil

from src.tar_archiver import create_tar_archive

def test_create_tar_archive_default():
    # Create a temporary directory with some files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('test content 1')
        with open(os.path.join(temp_dir, 'file2.txt'), 'w') as f:
            f.write('test content 2')

        # Create tar archive
        archive_path = create_tar_archive(temp_dir)

        # Verify archive was created
        assert os.path.exists(archive_path)
        assert archive_path.endswith('.tar.gz')

        # Verify contents of archive
        with tarfile.open(archive_path, 'r:gz') as tar:
            tar_contents = tar.getnames()
            assert len(tar_contents) > 0
            assert os.path.basename(temp_dir) in tar_contents

def test_create_tar_archive_custom_output():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test file
        with open(os.path.join(temp_dir, 'test.txt'), 'w') as f:
            f.write('test content')

        # Specify custom output path
        custom_output = os.path.join(temp_dir, 'custom_archive.tar.bz2')
        archive_path = create_tar_archive(temp_dir, output_path=custom_output, compression='bz2')

        # Verify archive created at specified path
        assert archive_path == custom_output
        assert os.path.exists(archive_path)

        # Verify contents of archive
        with tarfile.open(archive_path, 'r:bz2') as tar:
            tar_contents = tar.getnames()
            assert len(tar_contents) > 0

def test_create_tar_archive_no_compression():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test file
        with open(os.path.join(temp_dir, 'test.txt'), 'w') as f:
            f.write('test content')

        # Create uncompressed tar archive
        archive_path = create_tar_archive(temp_dir, compression='')

        # Verify archive was created
        assert os.path.exists(archive_path)
        assert archive_path.endswith('.tar')

        # Verify contents of archive
        with tarfile.open(archive_path, 'r:') as tar:
            tar_contents = tar.getnames()
            assert len(tar_contents) > 0

def test_create_tar_archive_invalid_directory():
    # Test with non-existent directory
    with pytest.raises(ValueError, match="Directory does not exist"):
        create_tar_archive('/path/to/nonexistent/directory')

def test_create_tar_archive_not_directory():
    # Create a temporary file (not a directory)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
        try:
            # Test with file instead of directory
            with pytest.raises(ValueError, match="Path is not a directory"):
                create_tar_archive(temp_file_path)
        finally:
            # Clean up
            os.unlink(temp_file_path)

def test_create_tar_archive_invalid_compression():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test with invalid compression type
        with pytest.raises(ValueError, match="Invalid compression type"):
            create_tar_archive(temp_dir, compression='invalid')