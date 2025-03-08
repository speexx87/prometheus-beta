from typing import List

def find_duplicates(numbers: List[int]) -> List[int]:
    """
    Find and return a list of duplicate integers from the input list.
    
    Args:
        numbers (List[int]): A list of integers to check for duplicates.
    
    Returns:
        List[int]: A list of integers that appear more than once in the input list.
    
    Examples:
        >>> find_duplicates([1, 2, 3, 4, 2, 5, 6, 3])
        [2, 3]
        >>> find_duplicates([1, 1, 1, 2, 2])
        [1, 2]
        >>> find_duplicates([])
        []
    """
    # Use a set to track duplicates efficiently
    seen = set()
    duplicates = set()
    
    for num in numbers:
        # If already seen, it's a duplicate
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    # Convert to sorted list to ensure consistent output
    return sorted(list(duplicates))