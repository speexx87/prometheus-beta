import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snappy_compression import compress_data, decompress_data

def test_compress_decompress_text():
    """Test compression and decompression of text data"""
    original_text = "Hello, Snappy compression!"
    compressed = compress_data(original_text)
    decompressed = decompress_data(compressed)
    
    assert decompressed.decode('utf-8') == original_text
    assert len(compressed) < len(original_text.encode('utf-8'))

def test_compress_decompress_bytes():
    """Test compression and decompression of byte data"""
    original_bytes = b'\x00\x01\x02\x03\xff\xfe'
    compressed = compress_data(original_bytes)
    decompressed = decompress_data(compressed)
    
    assert decompressed == original_bytes

def test_empty_input_compression():
    """Test handling of empty input during compression"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_data(b'')
    
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_data('')

def test_invalid_input_type_compression():
    """Test handling of invalid input types during compression"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        compress_data(123)
    
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        compress_data(None)

def test_empty_input_decompression():
    """Test handling of empty input during decompression"""
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        decompress_data(b'')

def test_invalid_input_type_decompression():
    """Test handling of invalid input types during decompression"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_data('not bytes')
    
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_data(None)

def test_large_data_compression():
    """Test compression of relatively large data"""
    large_data = b'x' * 10000
    compressed = compress_data(large_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed == large_data