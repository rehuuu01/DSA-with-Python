class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes(root):
    """
    Returns the total number of nodes in a binary tree.
    """
    if root is None:
        return 0
    
    return 1 + count_nodes(root.left) + count_nodes(root.right)
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

    print("Total number of nodes in the binary tree is:", count_nodes(root))

