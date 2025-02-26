def sort_array_with_even_squares(arr):
    """
    Sort an array in ascending order, with even number squares sorted in descending order.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Sorted array with even number squares in descending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numeric")
    
    # If array is empty, return empty list
    if not arr:
        return []
    
    # First sort the array
    sorted_arr = sorted(arr)
    
    # Create a mapping of original indices
    index_map = {num: idx for idx, num in enumerate(sorted_arr)}
    
    # Collect even numbers
    evens = [x for x in sorted_arr if x % 2 == 0]
    
    # Square and sort even numbers in descending order
    squared_evens = sorted([x**2 for x in evens], reverse=True)
    
    # Recreate array with precise rules
    result = sorted_arr.copy()
    even_idx = 0
    
    for i, num in enumerate(sorted_arr):
        if num % 2 == 0:
            result[i] = squared_evens[even_idx]
            even_idx += 1
    
    return result