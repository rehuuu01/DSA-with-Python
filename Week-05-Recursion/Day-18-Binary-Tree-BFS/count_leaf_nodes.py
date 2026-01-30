class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_leaf_nodes(root):
    """
    Returns the number of leaf nodes in a binary tree.
    A leaf node is a node with no children.
    """
    if root is None:
        return 0
    
    # If it's a leaf node (no left and right child)
    if root.left is None and root.right is None:
        return 1
    
    # Recursively count leaf nodes in left and right subtrees
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)
# Example usage:
if __name__ == "__main__":
    # Constructing a binary tree
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Number of leaf nodes in the binary tree is:", count_leaf_nodes(root))

 