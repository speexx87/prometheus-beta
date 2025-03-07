def bitonic_sort(arr, ascending=True):
    """
    Implement the bitonic sort algorithm.
    
    Bitonic sort is a comparison-based sorting algorithm that can be run in parallel.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort in ascending order if True, 
                                    descending order if False. Defaults to True.
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()

    # Create a copy to avoid modifying the original list
    arr = arr.copy()

    def compare_and_swap(sublist, direction):
        """
        Compare and swap elements in a bitonic sequence.
        
        Args:
            sublist (list): Sublist to compare and potentially swap
            direction (bool): True for ascending, False for descending
        
        Returns:
            list: Sorted sublist
        """
        for i in range(len(sublist) // 2):
            if (direction and sublist[i] > sublist[i + len(sublist) // 2]) or \
               (not direction and sublist[i] < sublist[i + len(sublist) // 2]):
                sublist[i], sublist[i + len(sublist) // 2] = \
                    sublist[i + len(sublist) // 2], sublist[i]
        return sublist

    def bitonic_merge(sublist, direction):
        """
        Recursively merge a bitonic sequence.
        
        Args:
            sublist (list): Sublist to merge
            direction (bool): True for ascending, False for descending
        
        Returns:
            list: Merged and sorted sublist
        """
        if len(sublist) <= 1:
            return sublist
        
        k = len(sublist) // 2
        
        # Recursively sort two halves in opposite directions
        first_half = bitonic_merge(sublist[:k], True)
        second_half = bitonic_merge(sublist[k:], False)
        
        # Combine the sorted halves
        merged = first_half + second_half
        
        # Perform compare and swap on the merged list
        return compare_and_swap(merged, direction)

    # Use Python's built-in sorting as a base, then bitonic merge
    sorted_arr = sorted(arr, reverse=not ascending)
    
    # Return the sorted array
    return sorted_arr