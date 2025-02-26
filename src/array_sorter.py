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
    
    # If there are no even numbers, return sorted array
    if not any(x % 2 == 0 for x in sorted_arr):
        return sorted_arr
    
    # Create a copy of the sorted array
    result = sorted_arr.copy()
    
    # Find and replace even numbers with squares in descending order
    even_numbers = sorted([x for x in sorted_arr if x % 2 == 0])
    even_squares = sorted([x**2 for x in even_numbers], reverse=True)
    
    j = 0
    for i in range(len(result)):
        if result[i] % 2 == 0:
            result[i] = even_squares[j]
            j += 1
    
    return result