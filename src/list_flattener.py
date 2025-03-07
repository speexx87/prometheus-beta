from typing import List, Any

def flatten_nested_list(nested_list: List[Any]) -> List[Any]:
    """
    Flatten a nested list of arbitrary depth into a single-level list.
    
    Args:
        nested_list (List[Any]): A potentially nested list to be flattened.
    
    Returns:
        List[Any]: A flattened list containing all non-list elements.
    
    Raises:
        TypeError: If the input is not a list.
    
    Examples:
        >>> flatten_nested_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_nested_list([])
        []
    """
    # Check if input is a list
    if not isinstance(nested_list, list):
        raise TypeError("Input must be a list")
    
    # Use recursive approach to flatten the list
    flattened = []
    for item in nested_list:
        # If item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_nested_list(item))
        else:
            flattened.append(item)
    
    return flattened