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
    
    # Sort even numbers as squares in descending order
    squared_evens = sorted([x**2 for x in evens], reverse=True)
    
    # Reconstruct result with precise order
    result = []
    odd_idx = 0
    even_idx = 0
    
    for num in sorted_arr:
        if num % 2 == 0:
            # Add squared even number from descending list
            result.append(squared_evens[even_idx])
            even_idx += 1
        else:
            # Add odd number
            result.append(odds[odd_idx])
            odd_idx += 1
    
    return result