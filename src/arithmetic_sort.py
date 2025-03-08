def arithmetic_sort(arr):
    """
    Sort a list of integers using only basic arithmetic operations.
    
    This function implements a basic sorting algorithm using only 
    arithmetic operations, avoiding built-in sorting functions.
    
    Args:
        arr (list): A list of integers to be sorted.
    
    Returns:
        list: A new list with integers sorted in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Bubble sort using only arithmetic operations
    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare and swap using arithmetic comparisons
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap without using temp variable
                sorted_arr[j] = sorted_arr[j] + sorted_arr[j + 1]
                sorted_arr[j + 1] = sorted_arr[j] - sorted_arr[j + 1]
                sorted_arr[j] = sorted_arr[j] - sorted_arr[j + 1]
    
    return sorted_arr