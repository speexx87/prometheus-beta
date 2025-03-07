def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array for KMP algorithm.
    
    Args:
        pattern (str): The pattern string to compute LPS array for
    
    Returns:
        list: LPS array representing the longest proper prefix which is also a suffix
    
    Raises:
        TypeError: If input is not a string
    """
    # Type checking
    if not isinstance(pattern, str):
        raise TypeError("Pattern must be a string")
    
    # Initialize LPS array with zeros
    lps = [0] * len(pattern)
    
    # Length of the previous longest prefix suffix
    length = 0
    i = 1
    
    # Build the LPS array
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky - handle cases where characters don't match
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform Knuth-Morris-Pratt string search algorithm.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is empty
    """
    # Type and validity checking
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    # If pattern is longer than text, no match is possible
    if len(pattern) > len(text):
        return []
    
    # Compute the LPS array
    lps = compute_lps_array(pattern)
    
    # List to store starting indices of matches
    matches = []
    
    # Pointers for text and pattern
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        # If characters match, move both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # If full pattern is matched, record the match
        if j == len(pattern):
            matches.append(i - j)
            # Reset j to continue searching
            j = lps[j-1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If we have some matched characters
            if j != 0:
                # Use LPS array to determine next state
                j = lps[j-1]
            else:
                # No match, move to next character in text
                i += 1
    
    return matches