def filter_odd_numbers(numbers):
    """
    Filter and sort odd integers from a given list.

    Args:
        numbers (list): A list of integers to filter.

    Returns:
        list: A new list containing only the odd integers, sorted in ascending order.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Filter odd numbers and sort
    return sorted([num for num in numbers if num % 2 != 0])