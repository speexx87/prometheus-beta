import logging
import json
import pytest
from src.api_payload_logger import log_api_response_payload_size

class MockLogger:
    def __init__(self):
        self.records = []

    def log(self, level, msg):
        self.records.append((level, msg))

def test_log_payload_size_with_dict():
    mock_logger = MockLogger()
    test_dict = {"key": "value", "numbers": [1, 2, 3]}
    
    # Log and check return value
    size = log_api_response_payload_size(test_dict, logger=mock_logger)
    
    # Verify size calculation
    expected_size = len(json.dumps(test_dict).encode('utf-8'))
    assert size == expected_size
    
    # Verify logging
    assert len(mock_logger.records) == 1
    assert mock_logger.records[0][0] == logging.INFO
    assert f"API Response Payload Size: {size} bytes" in mock_logger.records[0][1]

def test_log_payload_size_with_json_string():
    mock_logger = MockLogger()
    test_json = '{"key": "value", "numbers": [1, 2, 3]}'
    
    # Log and check return value
    size = log_api_response_payload_size(test_json, logger=mock_logger)
    
    # Verify size calculation
    expected_size = len(test_json.encode('utf-8'))
    assert size == expected_size
    
    # Verify logging
    assert len(mock_logger.records) == 1
    assert mock_logger.records[0][0] == logging.INFO
    assert f"API Response Payload Size: {size} bytes" in mock_logger.records[0][1]

def test_log_payload_size_with_custom_log_level():
    mock_logger = MockLogger()
    test_dict = {"key": "value"}
    
    # Log with custom log level
    size = log_api_response_payload_size(test_dict, logger=mock_logger, log_level=logging.DEBUG)
    
    # Verify logging level
    assert mock_logger.records[0][0] == logging.DEBUG

def test_log_payload_size_invalid_type():
    with pytest.raises(TypeError):
        log_api_response_payload_size(123)  # Invalid type

def test_log_payload_size_non_json_string():
    mock_logger = MockLogger()
    non_json_string = "This is a plain text string"
    
    # Log non-JSON string
    size = log_api_response_payload_size(non_json_string, logger=mock_logger)
    
    # Verify size and logging
    expected_size = len(non_json_string.encode('utf-8'))
    assert size == expected_size
    assert len(mock_logger.records) == 1
    assert f"API Response Payload Size: {size} bytes" in mock_logger.records[0][1]