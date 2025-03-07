import pytest
from src.prims_algorithm import prims_algorithm

def test_simple_graph():
    """Test a simple connected graph."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    
    mst = prims_algorithm(graph)
    
    # Validate MST properties
    assert mst is not None
    assert len(mst) == len(graph) - 1  # MST should have V-1 edges
    
    # Expected edges (there might be multiple valid MSTs)
    expected_edges = {
        ('A', 'C', 2),
        ('C', 'B', 1),
        ('D', 'E', 2),
        ('B', 'D', 5)
    }
    
    # Convert mst to a set of tuples for comparison
    mst_set = {tuple(sorted(edge[:2]) + [edge[2]]) for edge in mst}
    expected_set = {tuple(sorted(edge[:2]) + [edge[2]]) for edge in expected_edges}
    
    assert mst_set == expected_set

def test_empty_graph():
    """Test an empty graph."""
    graph = {}
    assert prims_algorithm(graph) is None

def test_single_vertex_graph():
    """Test a graph with a single vertex."""
    graph = {'A': {}}
    assert prims_algorithm(graph) == []

def test_disconnected_graph():
    """Test a disconnected graph."""
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 2},
        'D': {'C': 2}
    }
    assert prims_algorithm(graph) is None

def test_invalid_graph_structure():
    """Test invalid graph structure."""
    with pytest.raises(ValueError):
        prims_algorithm({'A': [1, 2, 3]})

def test_weighted_graph_with_negative_weights():
    """Test a graph with negative weights."""
    graph = {
        'A': {'B': -1, 'C': -2},
        'B': {'A': -1, 'C': -3},
        'C': {'A': -2, 'B': -3}
    }
    
    mst = prims_algorithm(graph)
    
    # Validate MST properties
    assert mst is not None
    assert len(mst) == len(graph) - 1

def test_graph_with_multiple_same_weight_edges():
    """Test a graph with multiple edges of the same weight."""
    graph = {
        'A': {'B': 2, 'C': 2},
        'B': {'A': 2, 'C': 2},
        'C': {'A': 2, 'B': 2}
    }
    
    mst = prims_algorithm(graph)
    
    # Validate MST properties
    assert mst is not None
    assert len(mst) == len(graph) - 1