from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a room using a robot vacuum cleaner.
    
    Args:
    - grid: 2D grid representing the room (0 = empty, 1 = obstacle)
    - r: Starting row of the robot
    - c: Starting column of the robot
    - direction: Initial direction of the robot (0: North, 1: East, 2: South, 3: West)
    
    Returns:
    - Minimum number of steps required to clean the entire room
    """
    # Validate input first
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    rows, cols = len(grid), len(grid[0])
    
    # Check if start position is valid
    if not (0 <= r < rows and 0 <= c < cols):
        raise IndexError("Starting position is out of grid bounds")
    
    if grid[r][c] == 1:
        raise IndexError("Starting position is an obstacle")
    
    # Directions: North, East, South, West
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    # Track visited cells and cleaned cells
    visited = set()
    cleaned = set()
    
    def is_valid_move(r: int, c: int) -> bool:
        """Check if the move is within grid and not an obstacle"""
        return (0 <= r < rows and 
                0 <= c < cols and 
                grid[r][c] != 1)
    
    def dfs(r: int, c: int, direction: int) -> int:
        """Depth-first search to clean the room"""
        # Stop if cell is already visited
        if (r, c) in visited:
            return 0
        
        # Mark current cell as visited and cleaned
        visited.add((r, c))
        cleaned.add((r, c))
        
        steps = 1
        
        # Try moving in all 4 directions
        for i in range(4):
            # Calculate new direction and position
            new_direction = (direction + i) % 4
            new_r = r + dr[new_direction]
            new_c = c + dc[new_direction]
            
            # If new position is valid and not visited
            if is_valid_move(new_r, new_c) and (new_r, new_c) not in visited:
                # Recursively clean from the new position
                steps += dfs(new_r, new_c, new_direction)
        
        return steps
    
    # Start cleaning from the initial position
    return dfs(r, c, direction)