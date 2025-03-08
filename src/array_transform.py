def transform_array(arr):
    """
    Transform an array of non-negative integers based on specific rules:
    - 0 remains 0
    - Non-zero elements are transformed to their square plus 1

    Args:
        arr (list): Input list of non-negative integers

    Returns:
        list: Transformed array based on the specified rules

    Raises:
        TypeError: If input is not a list
        ValueError: If any element is negative
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are non-negative integers
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # Transform the array
    return [0 if x == 0 else x**2 + 1 for x in arr]