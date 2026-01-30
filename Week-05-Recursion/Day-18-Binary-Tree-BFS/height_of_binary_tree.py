class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    """
    Returns the height of a binary tree.
    Height is defined as the number of edges on the longest path from root to a leaf.
    An empty tree has height -1, a single node has height 0.
    """
    if root is None:
        return -1
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    return max(left_height, right_height) + 1

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

    print("Height of the binary tree is:", height(root))