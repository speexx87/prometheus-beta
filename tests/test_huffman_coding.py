import pytest
from src.huffman_coding import (
    huffman_encode, 
    huffman_decode, 
    build_frequency_dict, 
    build_huffman_tree, 
    build_huffman_codes
)

def test_build_frequency_dict():
    data = "hello world"
    freq_dict = build_frequency_dict(data)
    assert freq_dict == {
        'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1
    }

def test_huffman_encode_decode():
    # Test simple string
    original_data = "hello world"
    encoded_data, huffman_codes = huffman_encode(original_data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == original_data

def test_huffman_encode_decode_empty_string():
    # Test empty string
    original_data = ""
    encoded_data, huffman_codes = huffman_encode(original_data)
    assert encoded_data == ''
    assert huffman_codes == {}
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == ''

def test_huffman_encode_decode_single_char():
    # Test single character
    original_data = "a"
    encoded_data, huffman_codes = huffman_encode(original_data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == original_data

def test_invalid_decode():
    # Test decoding with invalid data
    huffman_codes = {'a': '0', 'b': '1'}
    with pytest.raises(ValueError):
        huffman_decode('010', huffman_codes)

def test_build_huffman_codes():
    # Test Huffman code generation
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16}
    tree = build_huffman_tree(freq_dict)
    codes = build_huffman_codes(tree)
    
    # Verify codes are unique
    assert len(set(codes.values())) == len(codes)

def test_encode_decode_complex_data():
    # Test with a more complex string
    original_data = "this is a test of huffman coding implementation"
    encoded_data, huffman_codes = huffman_encode(original_data)
    decoded_data = huffman_decode(encoded_data, huffman_codes)
    assert decoded_data == original_data