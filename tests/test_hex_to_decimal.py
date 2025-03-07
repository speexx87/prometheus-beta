import pytest
from src.hex_to_decimal import hex_to_decimal

def test_basic_hex_conversion():
    """Test basic hexadecimal to decimal conversions."""
    assert hex_to_decimal('A') == 10
    assert hex_to_decimal('F') == 15
    assert hex_to_decimal('10') == 16
    assert hex_to_decimal('FF') == 255
    assert hex_to_decimal('100') == 256

def test_hex_conversion_with_prefix():
    """Test conversions with '0x' or '0X' prefix."""
    assert hex_to_decimal('0xA') == 10
    assert hex_to_decimal('0XFF') == 255
    assert hex_to_decimal('0x100') == 256

def test_case_insensitivity():
    """Ensure the function works with both uppercase and lowercase hex."""
    assert hex_to_decimal('a') == 10
    assert hex_to_decimal('A') == 10
    assert hex_to_decimal('ff') == 255
    assert hex_to_decimal('FF') == 255

def test_large_hex_number():
    """Test conversion of larger hexadecimal numbers."""
    assert hex_to_decimal('1234') == 4660
    assert hex_to_decimal('ABCD') == 43981
    assert hex_to_decimal('0xABCD') == 43981

def test_invalid_hex_input():
    """Test error handling for invalid hexadecimal inputs."""
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('G')
    
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('12345G')
    
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('0x')
    
    with pytest.raises(ValueError, match="Invalid hexadecimal string"):
        hex_to_decimal('')

def test_zero_hex():
    """Test conversion of zero in hexadecimal."""
    assert hex_to_decimal('0') == 0
    assert hex_to_decimal('00') == 0
    assert hex_to_decimal('0x0') == 0