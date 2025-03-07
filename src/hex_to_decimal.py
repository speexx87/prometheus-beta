def hex_to_decimal(hex_string: str) -> int:
    """
    Convert a hexadecimal string to its decimal (base 10) integer representation.

    Args:
        hex_string (str): A string representing a hexadecimal number.
                           Can be prefixed with '0x' or '0X' (optional).
                           Case-insensitive (a-f or A-F are accepted).

    Returns:
        int: The decimal (base 10) representation of the hexadecimal number.

    Raises:
        ValueError: If the input is not a valid hexadecimal string.
    """
    # Remove '0x' or '0X' prefix if present
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    
    # Validate input
    if not all(c in '0123456789abcdefABCDEF' for c in hex_string):
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")
    
    # Convert to decimal using built-in int() function with base 16
    return int(hex_string, 16)