import os
import typing


def create_directory(path: str, mode: int = 0o755) -> bool:
    """
    Create a new directory with optional permission mode.

    Args:
        path (str): The path of the directory to create
        mode (int, optional): Permission mode for the directory. Defaults to 0o755.

    Returns:
        bool: True if directory was created, False if directory already exists

    Raises:
        PermissionError: If insufficient permissions to create directory
        OSError: For other OS-related errors during directory creation
    """
    # Normalize the path to handle potential inconsistent path separators
    normalized_path = os.path.normpath(path)

    # Check if directory already exists
    if os.path.exists(normalized_path):
        return False

    try:
        # Create directory with specified permissions
        os.makedirs(normalized_path, mode=mode, exist_ok=False)
        return True
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to create directory: {normalized_path}")
    except OSError as e:
        raise OSError(f"Could not create directory {normalized_path}: {str(e)}")