import heapq
from typing import Dict, List, Tuple, Union

def prims_algorithm(graph: Dict[str, Dict[str, int]]) -> Union[List[Tuple[str, str, int]], None]:
    """
    Implement Prim's algorithm to find the minimum spanning tree (MST) of a graph.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph.
                                           Each key is a vertex, and its value is a dictionary 
                                           of connected vertices with their edge weights.
    
    Returns:
        List[Tuple[str, str, int]]: A list of edges in the minimum spanning tree, 
                                    where each edge is (start_vertex, end_vertex, weight).
        None: If the graph is empty or disconnected.
    
    Raises:
        ValueError: If the input graph is not a valid adjacency list.
    """
    # Validate input
    if not graph:
        return None
    
    # Validate graph structure
    if not all(isinstance(neighbors, dict) for neighbors in graph.values()):
        raise ValueError("Invalid graph structure. Must be an adjacency list.")
    
    # Choose an arbitrary starting vertex
    start_vertex = list(graph.keys())[0]
    
    # Initialize data structures
    mst = []
    visited = set([start_vertex])
    edges = []
    
    # Add all edges from the start vertex to the heap
    for neighbor, weight in graph[start_vertex].items():
        heapq.heappush(edges, (weight, start_vertex, neighbor))
    
    # Continue until we've visited all vertices or can't expand further
    while edges:
        weight, from_vertex, to_vertex = heapq.heappop(edges)
        
        # Skip if the vertex is already in the MST
        if to_vertex in visited:
            continue
        
        # Add the edge to MST and mark vertex as visited
        mst.append((from_vertex, to_vertex, weight))
        visited.add(to_vertex)
        
        # Add new edges from the newly visited vertex
        for next_neighbor, next_weight in graph[to_vertex].items():
            if next_neighbor not in visited:
                heapq.heappush(edges, (next_weight, to_vertex, next_neighbor))
    
    # Check if MST includes all vertices
    if len(visited) != len(graph):
        return None
    
    return mst