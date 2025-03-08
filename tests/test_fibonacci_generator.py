import pytest
from src.fibonacci_generator import fibonacci_generator

def test_fibonacci_generator_zero():
    assert fibonacci_generator(0) == []

def test_fibonacci_generator_one():
    assert fibonacci_generator(1) == [0]

def test_fibonacci_generator_two():
    assert fibonacci_generator(2) == [0, 1]

def test_fibonacci_generator_five():
    assert fibonacci_generator(5) == [0, 1, 1, 2, 3]

def test_fibonacci_generator_ten():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci_generator(10) == expected

def test_fibonacci_generator_negative_input():
    with pytest.raises(ValueError, match="Number of Fibonacci numbers must be non-negative"):
        fibonacci_generator(-1)

def test_fibonacci_generator_invalid_type():
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator("not an int")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator(None)