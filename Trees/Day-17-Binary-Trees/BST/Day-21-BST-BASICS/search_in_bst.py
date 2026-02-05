class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_bst(root, val):
    """
    Search for a value in BST (iterative).
    
    Time: O(h) where h is height
          O(log n) for balanced, O(n) for skewed
    Space: O(1)
    """
    current = root
    
    while current:
        if val == current.val:
            return current  # Found!
        elif val < current.val:
            current = current.left  # Go left
        else:
            current = current.right  # Go right
    
    return None  # Not found


# Test
#         8
#        / \
#       3   10
#      / \    \
#     1   6   14
#        / \  /
#       4  7 13

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

result = search_bst(root, 6)
print(f"Found: {result.val if result else None}")  # Output: Found: 6

result = search_bst(root, 5)
print(f"Found: {result.val if result else None}")  # Output: Found: None