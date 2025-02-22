import pytest
from src.robot_vacuum import cleanRoom

def test_clean_empty_room():
    """Test cleaning an empty room"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 1, 1, 0)
    assert steps == 9  # Should visit all 9 cells

def test_room_with_obstacles():
    """Test cleaning a room with obstacles"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps == 8  # Should visit all cells except the obstacle

def test_single_cell_room():
    """Test cleaning a single-cell room"""
    grid = [[0]]
    steps = cleanRoom(grid, 0, 0, 0)
    assert steps == 1  # Should only visit the single cell

def test_room_with_multiple_obstacles():
    """Test cleaning a room with multiple obstacles"""
    grid = [
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]
    steps = cleanRoom(grid, 2, 2, 3)
    assert 7 <= steps <= 12  # Exact number may vary due to DFS traversal

def test_starting_on_obstacle():
    """Test starting the robot on an obstacle"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    with pytest.raises(IndexError):
        cleanRoom(grid, 1, 1, 0)

def test_out_of_bounds_start():
    """Test starting the robot outside the grid"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    with pytest.raises(IndexError):
        cleanRoom(grid, 3, 3, 0)

def test_empty_grid():
    """Test empty grid input"""
    with pytest.raises(ValueError):
        cleanRoom([], 0, 0, 0)