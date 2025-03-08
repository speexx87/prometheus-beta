def max_non_overlapping_subarray_sum(arr):
    """
    Calculate the maximum sum of a non-overlapping subarray in the given array.
    
    A non-overlapping subarray means no two subarrays can share any elements.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The maximum sum of non-overlapping subarrays
    
    Examples:
        >>> max_non_overlapping_subarray_sum([1, 2, 3, 4, 5])
        9
        >>> max_non_overlapping_subarray_sum([-1, -2, 3, 4, -5])
        7
        >>> max_non_overlapping_subarray_sum([])
        0
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Handle empty array case
    if not arr:
        return 0
    
    # If array has only one element, return that element if positive
    if len(arr) == 1:
        return max(arr[0], 0)
    
    # Dynamic programming approach to find max non-overlapping sum
    # We'll use two variables to track max sum including/excluding current element
    include = max(arr[0], 0)  # Max sum including first element
    exclude = 0  # Max sum excluding first element
    
    for num in arr[1:]:
        # Store previous include value
        prev_include = include
        
        # Two choices for current element:
        # 1. Start a new subarray from this element
        # 2. Skip this element and use previous best
        include = max(exclude + max(num, 0), 0)
        
        # Update exclude to be the max of previous states
        exclude = max(prev_include, exclude)
    
    # Return the maximum of final include and exclude
    return max(include, exclude)