import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.

    Args:
        file_path (str): The path to the file whose permissions will be changed.
        mode (int): The new permission mode (in octal, e.g., 0o755).

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permission to change file permissions.
        TypeError: If incorrect argument types are provided.
        ValueError: If an invalid permission mode is given.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer")
    
    # Validate file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate mode is a valid octal permission
    if mode < 0 or mode > 0o777:
        raise ValueError("Invalid permission mode. Must be between 0 and 0o777")
    
    try:
        # Change file permissions
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to change mode of {file_path}")
    
    return True