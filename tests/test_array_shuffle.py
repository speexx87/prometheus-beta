import pytest
import random
from src.array_shuffle import shuffle_array

def test_shuffle_basic_list():
    """Test shuffling a basic list of integers."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that the shuffled list contains the same elements
    assert sorted(shuffled) == sorted(original)
    
    # Check that the order is different (with high probability)
    assert shuffled != original

def test_shuffle_empty_list():
    """Test shuffling an empty list."""
    original = []
    shuffled = shuffle_array(original)
    assert shuffled == []

def test_shuffle_single_element_list():
    """Test shuffling a list with a single element."""
    original = [42]
    shuffled = shuffle_array(original)
    assert shuffled == [42]

def test_shuffle_different_types():
    """Test shuffling a list with different types of elements."""
    original = [1, 'a', True, 3.14, None]
    shuffled = shuffle_array(original)
    
    # Check that the shuffled list contains the same elements
    assert sorted(shuffled) == sorted(original)
    
    # Check that the order is different (with high probability)
    assert shuffled != original

def test_shuffle_raises_type_error():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(42)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(None)

def test_shuffle_randomness():
    """
    Test the randomness of the shuffling.
    This test checks that multiple shuffles are likely to produce different orders.
    Note: This is a probabilistic test and might rarely fail.
    """
    original = list(range(10))
    
    # Generate multiple shuffles
    shuffles = [shuffle_array(original) for _ in range(100)]
    
    # Check that at least some shuffles are different from the original
    different_shuffles = [s for s in shuffles if s != original]
    assert len(different_shuffles) > 0, "Shuffle does not seem random"