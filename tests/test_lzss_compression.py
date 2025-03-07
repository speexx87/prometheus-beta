"""
Test suite for LZSS Compression Algorithm
"""

import pytest
import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzss_compression import LZSSCompressor

def test_lzss_compression_basic():
    """Test basic compression and decompression"""
    compressor = LZSSCompressor()
    test_data = b"HELLO HELLO WORLD"
    
    # Compress
    compressed = compressor.compress(test_data)
    assert compressed is not None
    assert len(compressed) < len(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    assert decompressed == test_data

def test_lzss_compression_empty_input():
    """Test compression and decompression with empty input"""
    compressor = LZSSCompressor()
    
    # Empty bytes
    empty_bytes = b''
    assert compressor.compress(empty_bytes) == b''
    assert compressor.decompress(b'') == b''

def test_lzss_compression_string_input():
    """Test compression with string input"""
    compressor = LZSSCompressor()
    test_string = "Hello, repeated repeated text!"
    
    # Compress
    compressed = compressor.compress(test_string)
    assert compressed is not None
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == test_string

def test_lzss_compression_repeating_pattern():
    """Test compression with highly repetitive data"""
    compressor = LZSSCompressor()
    test_data = b"ABCABCABCABCABCABC" * 10
    
    # Compress
    compressed = compressor.compress(test_data)
    assert len(compressed) < len(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    assert decompressed == test_data

def test_lzss_compression_different_window_sizes():
    """Test compression with different window sizes"""
    # Test with small and large window sizes
    window_sizes = [256, 1024, 4096, 8192]
    test_data = b"This is a test string with some repeated content " * 5
    
    for window_size in window_sizes:
        compressor = LZSSCompressor(window_size=window_size)
        compressed = compressor.compress(test_data)
        decompressed = compressor.decompress(compressed)
        assert decompressed == test_data

def test_lzss_edge_cases():
    """Test edge cases like single character, minimal matches"""
    compressor = LZSSCompressor()
    
    # Single character
    single_char = b'A'
    compressed = compressor.compress(single_char)
    decompressed = compressor.decompress(compressed)
    assert decompressed == single_char
    
    # Minimal repetition
    minimal_repeat = b'ABCDEFABCDEF'
    compressed = compressor.compress(minimal_repeat)
    decompressed = compressor.decompress(compressed)
    assert decompressed == minimal_repeat