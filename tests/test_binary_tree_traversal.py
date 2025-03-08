import pytest
from src.binary_tree_traversal import Node, inorder_traversal, preorder_traversal, postorder_traversal

def test_empty_tree():
    """Test traversals on an empty (None) tree."""
    assert inorder_traversal(None) == []
    assert preorder_traversal(None) == []
    assert postorder_traversal(None) == []

def test_single_node_tree():
    """Test traversals on a tree with only a root node."""
    root = Node(5)
    assert inorder_traversal(root) == [5]
    assert preorder_traversal(root) == [5]
    assert postorder_traversal(root) == [5]

def test_full_binary_tree():
    """Test traversals on a full binary tree."""
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    assert inorder_traversal(root) == [4, 2, 5, 1, 6, 3, 7]
    assert preorder_traversal(root) == [1, 2, 4, 5, 3, 6, 7]
    assert postorder_traversal(root) == [4, 5, 2, 6, 7, 3, 1]

def test_unbalanced_tree():
    """Test traversals on an unbalanced tree."""
    #       1
    #      /
    #     2
    #    /
    #   3
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    
    assert inorder_traversal(root) == [3, 2, 1]
    assert preorder_traversal(root) == [1, 2, 3]
    assert postorder_traversal(root) == [3, 2, 1]

def test_complete_tree():
    """Test traversals on a complete tree."""
    #       10
    #     /    \
    #    5      15
    #   / \    /  \
    #  3   7  12   20
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(20)
    
    assert inorder_traversal(root) == [3, 5, 7, 10, 12, 15, 20]
    assert preorder_traversal(root) == [10, 5, 3, 7, 15, 12, 20]
    assert postorder_traversal(root) == [3, 7, 5, 12, 20, 15, 10]