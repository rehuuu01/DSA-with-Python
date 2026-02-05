class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_bst(root, val):
    """
    Insert a value into BST (iterative).
    
    Time: O(h) where h is height
    Space: O(1)
    """
    # If tree is empty, create root
    if not root:
        return TreeNode(val)
    
    current = root
    
    while True:
        if val < current.val:
            # Go left
            if current.left is None:
                current.left = TreeNode(val)
                break
            current = current.left
        else:
            # Go right (handles duplicates by inserting right)
            if current.right is None:
                current.right = TreeNode(val)
                break
            current = current.right
    
    return root


# Test
root = TreeNode(8)
root = insert_bst(root, 3)
root = insert_bst(root, 10)
root = insert_bst(root, 1)
root = insert_bst(root, 6)
root = insert_bst(root, 14)

# Tree structure:
#         8
#        / \
#       3   10
#      / \    \
#     1   6   14