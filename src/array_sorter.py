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
    
    # Create a copy of the input array to avoid modifying the original
    sorted_arr = sorted(arr)
    
    # Separate even and odd numbers
    evens = [x for x in sorted_arr if x % 2 == 0]
    odds = [x for x in sorted_arr if x % 2 != 0]
    
    # Sort even number squares in descending order
    even_squares = sorted([x**2 for x in evens], reverse=True)
    
    # Reconstruct the array
    result = []
    even_idx = 0
    odd_idx = 0
    
    for num in sorted_arr:
        if num % 2 == 0:
            # Replace even numbers with their descending squared order
            result.append(even_squares[even_idx])
            even_idx += 1
        else:
            # Preserve original odd numbers in ascending order
            result.append(num)
    
    return result