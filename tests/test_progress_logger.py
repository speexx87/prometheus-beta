import pytest
import io
import sys
from src.progress_logger import dynamic_progress_bar, log_progress

def test_dynamic_progress_bar_with_list():
    """Test progress bar with a known length list"""
    test_list = list(range(10))
    processed_items = []
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    for item in dynamic_progress_bar(test_list):
        processed_items.append(item)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check if all items were processed
    assert processed_items == test_list
    
    # Check if output contains expected formatting
    output = captured_output.getvalue()
    assert 'Progress:' in output
    assert '100.0%' in output
    assert 'Complete' in output

def test_dynamic_progress_bar_with_generator():
    """Test progress bar with a generator"""
    def test_generator():
        for i in range(5):
            yield i
    
    processed_items = []
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    for item in dynamic_progress_bar(test_generator()):
        processed_items.append(item)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check if all items were processed
    assert processed_items == list(range(5))
    
    # Check if output contains expected formatting
    output = captured_output.getvalue()
    assert 'Progress:' in output
    assert '100.0%' in output

def test_log_progress_wrapper():
    """Test the log_progress wrapper function"""
    test_list = list(range(10))
    processed_items = []
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    for item in log_progress(test_list):
        processed_items.append(item)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check if all items were processed
    assert processed_items == test_list
    
    # Check if output contains expected formatting
    output = captured_output.getvalue()
    assert 'Progress:' in output
    assert '100.0%' in output
    assert 'Complete' in output

def test_invalid_total():
    """Test that ValueError is raised for invalid total"""
    with pytest.raises(ValueError):
        list(dynamic_progress_bar(range(10), total=0))
    
    with pytest.raises(ValueError):
        list(dynamic_progress_bar(range(10), total=-5))

def test_custom_formatting():
    """Test custom formatting options"""
    test_list = list(range(10))
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    for item in dynamic_progress_bar(test_list, 
                                     prefix='Custom:', 
                                     suffix='Done', 
                                     decimals=2, 
                                     length=20, 
                                     fill='#'):
        pass
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check custom formatting
    output = captured_output.getvalue()
    assert 'Custom:' in output
    assert 'Done' in output
    assert '100.00%' in output