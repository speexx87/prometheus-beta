"""
Lempel-Ziv-Storer-Szymanski (LZSS) Compression Algorithm

This module provides functionality for LZSS data compression.
LZSS is a sliding window compression algorithm that replaces 
repeated occurrences of data with references to a single copy.
"""

class LZSSCompressor:
    def __init__(self, window_size=4096, lookahead_size=16):
        """
        Initialize the LZSS compressor.
        
        :param window_size: Size of the sliding window for searching previous occurrences
        :param lookahead_size: Size of the lookahead buffer for finding matches
        """
        self.window_size = window_size
        self.lookahead_size = lookahead_size

    def compress(self, data):
        """
        Compress input data using LZSS algorithm.
        
        :param data: Input data to compress (bytes or string)
        :return: Compressed data as bytes
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Validate input
        if not data:
            return b''
        
        compressed = bytearray()
        data_length = len(data)
        current_pos = 0
        
        while current_pos < data_length:
            # Find the longest match in the sliding window
            best_length = 0
            best_offset = 0
            
            # Define search range (sliding window)
            search_start = max(0, current_pos - self.window_size)
            search_end = current_pos
            
            # Look for the longest match
            for offset in range(search_start, search_end):
                match_length = 0
                
                # Check how long the match can be
                while (match_length < self.lookahead_size and 
                       current_pos + match_length < data_length and 
                       data[offset + match_length] == data[current_pos + match_length]):
                    match_length += 1
                
                # Update best match if found
                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_pos - offset
            
            # Encode the data
            if best_length > 2:
                # Encode a match: (offset, length)
                # Use 12 bits for offset, 4 bits for length
                compressed.append(0x80 | ((best_offset >> 4) & 0x0F))  # Flag bit + high 4 bits of offset
                compressed.append(((best_offset & 0x0F) << 4) | (best_length - 3))  # Low 4 bits of offset + length
                current_pos += best_length
            else:
                # Encode a literal byte
                compressed.append(data[current_pos])
                current_pos += 1
        
        return bytes(compressed)

    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZSS algorithm.
        
        :param compressed_data: Compressed data to decompress
        :return: Decompressed data as bytes
        """
        # Validate input
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        idx = 0
        
        while idx < len(compressed_data):
            # Check if it's a match or a literal
            if compressed_data[idx] & 0x80:
                # Match encoding
                # First byte: flag bit + high 4 bits of offset
                # Second byte: low 4 bits of offset + length
                high_offset = compressed_data[idx] & 0x0F
                idx += 1
                low_offset_and_length = compressed_data[idx]
                
                # Extract offset and length
                offset = (high_offset << 4) | (low_offset_and_length >> 4)
                length = (low_offset_and_length & 0x0F) + 3
                
                # Copy from previously decompressed data
                start = len(decompressed) - offset
                for _ in range(length):
                    decompressed.append(decompressed[start])
                    start += 1
                
                idx += 1
            else:
                # Literal byte
                decompressed.append(compressed_data[idx])
                idx += 1
        
        return bytes(decompressed)