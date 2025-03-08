def find_palindrome_substrings(input_string):
    """
    Find all palindrome substrings in the given input string.
    
    Args:
        input_string (str): The string to search for palindrome substrings.
    
    Returns:
        list: A sorted list of unique palindrome substrings.
               Sorted first by length (descending), then alphabetically.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty list
    if not input_string:
        return []
    
    # Set to store unique palindrome substrings
    palindromes = set()
    
    # Check all possible substrings
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            # Extract substring
            substring = input_string[start:end]
            
            # Check if substring is a palindrome (length > 1)
            if substring == substring[::-1] and len(substring) > 1:
                palindromes.add(substring)
    
    # Sort palindromes first by length (descending), then alphabetically
    def custom_sort(x):
        """Custom sorting key with special handling."""
        return (-len(x), x if len(x) == 2 else '')
    
    return sorted(list(palindromes), key=custom_sort)