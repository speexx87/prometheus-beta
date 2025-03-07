def convert_to_lowercase_with_spaces(input_string):
    """
    Convert a given string to lowercase, preserving or normalizing spaces.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The input string converted to lowercase with normalized spaces.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase and normalize spaces (replace multiple spaces with single space)
    return ' '.join(input_string.lower().split())