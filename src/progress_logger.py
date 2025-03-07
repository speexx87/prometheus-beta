import sys
import time

def dynamic_progress_bar(iterable, total=None, prefix='Progress:', 
                          suffix='Complete', decimals=1, length=50, 
                          fill='█', print_end="\r"):
    """
    Create a dynamic progress bar for tracking iteration progress.
    
    Args:
        iterable (iterable): The iterable to track progress over
        total (int, optional): Total number of iterations. Defaults to len(iterable)
        prefix (str, optional): Prefix string before progress bar
        suffix (str, optional): Suffix string after progress bar
        decimals (int, optional): Number of decimal places for percentage
        length (int, optional): Character length of progress bar
        fill (str, optional): Bar fill character
        print_end (str, optional): End character for print (default suppresses newline)
    
    Yields:
        The items from the original iterable
    
    Raises:
        ValueError: If total is less than or equal to zero
    """
    # Validate inputs
    if total is not None and total <= 0:
        raise ValueError("Total must be a positive number")
    
    # If total is not provided, try to get length of iterable
    if total is None:
        try:
            total = len(iterable)
        except TypeError:
            # For generators, we'll just work with known iterations
            total = None
    
    # Track iterations
    count = 0
    
    # Iterate over the items
    for item in iterable:
        count += 1
        
        # If total is known, print progress bar
        if total is not None:
            # Calculate percentage and bar length
            percent = ("{0:." + str(decimals) + "f}").format(100 * (count / float(total)))
            filled_length = int(length * count // total)
            bar = fill * filled_length + '-' * (length - filled_length)
            
            # Print progress bar
            print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end, flush=True)
        
        yield item
    
    # If total was known or last iteration occurred
    if total is not None or count > 0:
        print()

def log_progress(iterable, **kwargs):
    """
    Wrapper function that logs progress for an iterable while preserving iteration.
    
    Args:
        iterable (iterable): The iterable to track
        **kwargs: Additional arguments for dynamic_progress_bar
    
    Returns:
        generator: A generator that yields items from the original iterable
    """
    return dynamic_progress_bar(iterable, **kwargs)