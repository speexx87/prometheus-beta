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
    
    # Sort array first
    sorted_arr = sorted(arr)
    
    # Separate odd and even numbers
    odds = [x for x in sorted_arr if x % 2 != 0]
    evens = [x for x in sorted_arr if x % 2 == 0]
    
    # Square and sort even numbers in descending order
    squared_evens = sorted([x**2 for x in evens], reverse=True)
    
    # Create result list following exact pattern
    result = []
    odd_index = 0
    even_index = 0
    
    for num in sorted_arr:
        if num % 2 != 0:
            # Add odd numbers first
            result.append(odds[odd_index])
            odd_index += 1
        else:
            # Add squared even numbers
            result.append(squared_evens[even_index])
            even_index += 1
    
    return result