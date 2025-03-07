import pytest
from src.kmp_search import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test basic LPS array computation
    assert compute_lps_array('AAAA') == [0, 1, 2, 3]
    assert compute_lps_array('ABCDE') == [0, 0, 0, 0, 0]
    assert compute_lps_array('ABABC') == [0, 0, 1, 2, 0]
    
    # Test empty string
    assert compute_lps_array('') == []

def test_kmp_search_basic():
    # Test basic string matching
    assert kmp_search('ABABDABACDABABCABAB', 'ABABCABAB') == [10]
    assert kmp_search('AABAACAADAABAABA', 'AABA') == [0, 9, 12]
    
    # Test multiple occurrences
    assert kmp_search('ABABABAB', 'ABAB') == [0, 2, 4]
    
    # Test no occurrences
    assert kmp_search('ABCDE', 'XYZ') == []

def test_kmp_search_edge_cases():
    # Test empty text
    assert kmp_search('', 'ABC') == []
    
    # Test pattern longer than text
    assert kmp_search('ABC', 'ABCD') == []
    
    # Test single character matches
    assert kmp_search('AAAAA', 'A') == [0, 1, 2, 3, 4]

def test_kmp_search_type_errors():
    # Test type errors
    with pytest.raises(TypeError):
        kmp_search(123, 'pattern')
    with pytest.raises(TypeError):
        kmp_search('text', 123)

def test_kmp_search_value_errors():
    # Test empty pattern
    with pytest.raises(ValueError):
        kmp_search('text', '')

def test_compute_lps_array_type_error():
    # Test type error for LPS array computation
    with pytest.raises(TypeError):
        compute_lps_array(123)

def test_complex_pattern():
    # Test a more complex pattern with repeated subsequences
    text = 'PARTICIPATE IN PARACHUTE'
    pattern = 'PARA'
    assert kmp_search(text, pattern) == [15]