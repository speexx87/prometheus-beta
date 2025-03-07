"""
Module for replacing strings in files.

This module provides functionality to replace all occurrences of a specific 
string within a file, with robust error handling and flexibility.
"""

import os


def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of a specified string in a file.

    Args:
        file_path (str): Path to the file to be modified
        old_string (str): The string to be replaced
        new_string (str): The string to replace with

    Returns:
        int: Number of replacements made

    Raises:
        FileNotFoundError: If the specified file does not exist
        TypeError: If inputs are not strings
        ValueError: If any input is empty
    """
    # Input validation
    if not isinstance(file_path, str) or not isinstance(old_string, str) or not isinstance(new_string, str):
        raise TypeError("All arguments must be strings")
    
    if not file_path or not old_string:
        raise ValueError("File path and old string cannot be empty")
    
    # Check file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Read the file
    with open(file_path, 'r') as file:
        file_contents = file.read()
    
    # Case-sensitive string replacement
    modified_contents = file_contents.replace(old_string, new_string)
    replacements = file_contents.count(old_string)
    
    # Write back to file
    with open(file_path, 'w') as file:
        file.write(modified_contents)
    
    return replacements