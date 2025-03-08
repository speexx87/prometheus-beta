class Node:
    """
    Represents a node in a binary tree.
    
    Attributes:
        value: The value stored in the node
        left: Left child node (can be None)
        right: Right child node (can be None)
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Perform in-order traversal of a binary tree (left -> root -> right).
    
    Args:
        root (Node): Root of the binary tree or subtree
    
    Returns:
        list: List of node values in in-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.value)
    result.extend(inorder_traversal(root.right))
    
    return result

def preorder_traversal(root):
    """
    Perform pre-order traversal of a binary tree (root -> left -> right).
    
    Args:
        root (Node): Root of the binary tree or subtree
    
    Returns:
        list: List of node values in pre-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    result.append(root.value)
    result.extend(preorder_traversal(root.left))
    result.extend(preorder_traversal(root.right))
    
    return result

def postorder_traversal(root):
    """
    Perform post-order traversal of a binary tree (left -> right -> root).
    
    Args:
        root (Node): Root of the binary tree or subtree
    
    Returns:
        list: List of node values in post-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    result.extend(postorder_traversal(root.left))
    result.extend(postorder_traversal(root.right))
    result.append(root.value)
    
    return result