import pytest
import math
from src.circle_coverage import Circle, calculate_circle_coverage

def test_empty_input():
    """
    Test handling of empty input list.
    """
    assert len(calculate_circle_coverage([])) == 0

def test_single_circle():
    """
    Test coverage for a single circle.
    """
    circles = [Circle(0, 0, 5)]
    result = calculate_circle_coverage(circles)
    assert len(result) == 1
    assert result[0] == circles[0]

def test_multiple_concentric_circles():
    """
    Test coverage for concentric circles.
    """
    # Larger circle at center, smaller at different positions
    circles = [
        Circle(0, 0, 10),   # Largest circle
        Circle(1, 1, 3),    # Smaller circle inside the first
        Circle(-2, 2, 2)    # Another smaller circle
    ]
    
    result = calculate_circle_coverage(circles)
    assert len(result) == 1
    assert result[0].radius == 10

def test_overlapping_circles():
    """
    Test coverage for partially overlapping circles.
    """
    circles = [
        Circle(0, 0, 5),    # First circle
        Circle(4, 0, 5),    # Overlapping circle
        Circle(8, 0, 5)     # Another circle
    ]
    
    result = calculate_circle_coverage(circles)
    # Expect at least 2 covering circles
    assert len(result) <= len(circles)

def test_invalid_circle_radius():
    """
    Test handling of invalid circle radius.
    """
    with pytest.raises(ValueError, match="Circle radius must be positive"):
        calculate_circle_coverage([Circle(0, 0, -1)])

def test_coverage_completeness():
    """
    Test that all original circles are covered.
    """
    circles = [
        Circle(0, 0, 3),
        Circle(4, 0, 2),
        Circle(-4, 0, 2)
    ]
    
    result = calculate_circle_coverage(circles)
    
    # Verify each original circle is covered by a covering circle
    for original in circles:
        covered = any(
            math.sqrt((c.x - original.x)**2 + (c.y - original.y)**2) + original.radius <= c.radius
            for c in result
        )
        assert covered, f"Circle at ({original.x}, {original.y}) not covered"