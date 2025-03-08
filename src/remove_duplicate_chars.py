def remove_chars_over_twice(input_string):
    """
    Remove characters that appear more than twice in the given string.
    
    Args:
        input_string (str): The input string to process.
    
    Returns:
        str: A string with characters appearing more than twice removed.
    
    Examples:
        >>> remove_chars_over_twice("aabbbcccc")
        'aabbcc'
        >>> remove_chars_over_twice("hello")
        'hello'
        >>> remove_chars_over_twice("")
        ''
    """
    # If input is not a string, raise a TypeError
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return input_string
    
    # Count character occurrences
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Build result string, keeping chars that appear 1 or 2 times
    result = []
    for char in input_string:
        # Count current occurrences of the character in the result
        current_char_count = result.count(char)
        
        # Only append if character appears less than 2 times, or total count is less than original count
        if (current_char_count < 2) or (char_counts[char] > 2 and current_char_count < 2):
            result.append(char)
    
    return ''.join(result)