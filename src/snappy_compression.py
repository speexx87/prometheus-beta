import snappy

def compress_data(data):
    """
    Compress input data using the Snappy compression algorithm.

    Args:
        data (bytes or str): The data to be compressed. 
                              If str is provided, it will be encoded to bytes.

    Returns:
        bytes: Compressed data

    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Check input type and convert if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Perform Snappy compression
    try:
        compressed_data = snappy.compress(data)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_data(compressed_data):
    """
    Decompress data that was compressed using Snappy.

    Args:
        compressed_data (bytes): The compressed data to decompress

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
        RuntimeError: If decompression fails
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Perform Snappy decompression
    try:
        decompressed_data = snappy.decompress(compressed_data)
        return decompressed_data
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")