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
    seen_chars = {}
    for char in input_string:
        if char_counts[char] > 2:
            # For chars that appear more than twice, allow only 2 occurrences
            if seen_chars.get(char, 0) < 2:
                result.append(char)
                seen_chars[char] = seen_chars.get(char, 0) + 1
        else:
            # For chars that appear 1 or 2 times, keep all
            result.append(char)
    
    return ''.join(result)