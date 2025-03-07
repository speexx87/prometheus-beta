import logging
import json
from typing import Any, Dict, Optional, Union

def log_api_response_payload_size(response: Union[Dict[str, Any], str], 
                                   logger: Optional[logging.Logger] = None,
                                   log_level: int = logging.INFO) -> int:
    """
    Log the size of an API response payload.

    Args:
        response (Union[Dict[str, Any], str]): The API response to log. 
            Can be a dictionary or a JSON string.
        logger (Optional[logging.Logger]): Logger to use. 
            If None, uses the root logger.
        log_level (int): Logging level to use. Defaults to logging.INFO.

    Returns:
        int: The size of the payload in bytes.

    Raises:
        TypeError: If the response is not a dict or string.
        json.JSONDecodeError: If the string response cannot be parsed as JSON.
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()

    # Convert response to a string representation
    if isinstance(response, dict):
        payload_str = json.dumps(response)
    elif isinstance(response, str):
        # Attempt to parse to validate JSON and normalize
        try:
            json.loads(response)
            payload_str = response
        except json.JSONDecodeError:
            payload_str = response
    else:
        raise TypeError("Response must be a dictionary or JSON string")

    # Calculate payload size
    payload_size = len(payload_str.encode('utf-8'))

    # Log the payload size
    logger.log(log_level, f"API Response Payload Size: {payload_size} bytes")

    return payload_size