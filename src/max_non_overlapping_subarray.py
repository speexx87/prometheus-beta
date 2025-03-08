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
        >>> max_non_overlapping_subarray_sum([-1, 2, 3, -4, 5])
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
    # dp[i] represents the max sum of non-overlapping subarrays up to index i
    dp = [0] * len(arr)
    
    # First element is handled separately
    dp[0] = max(arr[0], 0)
    
    # Second element depends on first and second
    if len(arr) > 1:
        dp[1] = max(dp[0], arr[1], 0)
    
    # Iterate through rest of the array
    for i in range(2, len(arr)):
        # We have two choices:
        # 1. Include current element and the max sum 2 steps back
        # 2. Skip current element and take previous max
        dp[i] = max(
            dp[i-2] + max(arr[i], 0),  # Include current, skip previous
            dp[i-1]  # Skip current
        )
    
    # Return maximum sum
    return dp[-1]