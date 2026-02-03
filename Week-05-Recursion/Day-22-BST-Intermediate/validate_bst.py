class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --------------------------------------------------
# Approach 1: Inorder Traversal + Prev Pointer
# Time: O(n) | Space: O(h)
# --------------------------------------------------
def isValidBST(root):
    """
    Validate BST using inorder traversal.
    In a valid BST, inorder traversal produces
    strictly increasing values.
    """
    prev = [float('-inf')]  # mutable container

    def inorder(node):
        if not node:
            return True

        if not inorder(node.left):
            return False

        if node.val <= prev[0]:
            return False
        prev[0] = node.val

        return inorder(node.right)

    return inorder(root)


# --------------------------------------------------
# Approach 2: Min-Max Range Method
# Time: O(n) | Space: O(h)
# --------------------------------------------------
def isValidBST_minmax(root):
    """
    Validate BST using min-max constraints.
    Each node must lie within a valid range.
    """

    def helper(node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return (helper(node.left, low, node.val) and
                helper(node.right, node.val, high))

    return helper(root, float('-inf'), float('inf'))


# --------------------------------------------------
# Test Cases
# --------------------------------------------------
if __name__ == "__main__":
    # Valid BST
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print(isValidBST(root1))         # True
    print(isValidBST_minmax(root1))  # True

    # Invalid BST
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    print(isValidBST(root2))         # False
    print(isValidBST_minmax(root2))  # False
