class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_min(root):
    """
    Find minimum value in BST.
    Always the LEFTMOST node.

    Time: O(h)
    Space: O(1)
    """
    if not root:
        return None

    current = root
    while current.left:
        current = current.left

    return current.val


def find_max(root):
    """
    Find maximum value in BST.
    Always the RIGHTMOST node.

    Time: O(h)
    Space: O(1)
    """
    if not root:
        return None

    current = root
    while current.right:
        current = current.right

    return current.val


# ------------------ Test ------------------
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

print(f"Minimum: {find_min(root)}")  # Output: 1
print(f"Maximum: {find_max(root)}")  # Output: 14
