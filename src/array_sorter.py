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
    
    # Sort array to maintain overall ascending order
    sorted_arr = sorted(arr)
    
    # Create an index of even numbers
    even_indices = [i for i, x in enumerate(sorted_arr) if x % 2 == 0]
    
    # Create a list of squared even numbers to be sorted in descending order
    squared_even_numbers = sorted([x**2 for x in sorted_arr if x % 2 == 0], reverse=True)
    
    # Create copy of sorted array to modify
    result = sorted_arr.copy()
    
    # Replace even numbers with their squared values in descending order
    for idx, square in zip(even_indices, squared_even_numbers):
        result[idx] = square
    
    return result