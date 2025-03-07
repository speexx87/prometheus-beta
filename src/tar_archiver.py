import os
import tarfile
from typing import Union, Optional

def create_tar_archive(directory_path: str, 
                       output_path: Optional[str] = None, 
                       compression: str = 'gz') -> str:
    """
    Create a tar archive of a given directory.

    Args:
        directory_path (str): Path to the directory to be archived
        output_path (Optional[str], optional): Path for the output tar file. 
            If None, creates archive in the same directory as the source.
        compression (str, optional): Compression type. 
            Supports 'gz' (gzip), 'bz2' (bzip2), or '' (no compression). 
            Defaults to 'gz'.

    Returns:
        str: Path to the created tar archive

    Raises:
        ValueError: If directory does not exist or is not a directory
        ValueError: If invalid compression type is provided
    """
    # Validate directory exists and is a directory
    directory_path = os.path.abspath(directory_path)
    if not os.path.exists(directory_path):
        raise ValueError(f"Directory does not exist: {directory_path}")
    if not os.path.isdir(directory_path):
        raise ValueError(f"Path is not a directory: {directory_path}")

    # Validate compression type
    valid_compression = ['', 'gz', 'bz2']
    if compression not in valid_compression:
        raise ValueError(f"Invalid compression type. Must be one of {valid_compression}")

    # Determine output path
    if output_path is None:
        output_path = os.path.join(
            os.path.dirname(directory_path), 
            f"{os.path.basename(directory_path)}.tar{'.'+compression if compression else ''}"
        )
    else:
        output_path = os.path.abspath(output_path)

    # Create tar archive
    mode = f'w:{compression}' if compression else 'w'
    with tarfile.open(output_path, mode) as tar:
        tar.add(directory_path, arcname=os.path.basename(directory_path))

    return output_path