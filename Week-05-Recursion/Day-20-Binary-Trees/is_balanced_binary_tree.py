class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Check if binary tree is height-balanced.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """

        def check_height(node):
            # Base case
            if node is None:
                return 0

            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1

            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1

            # If unbalanced at current node
            if abs(left_height - right_height) > 1:
                return -1

            # Return height
            return max(left_height, right_height) + 1

        return check_height(root) != -1


# -------- Example Usage --------
if __name__ == "__main__":
    """
    Balanced Tree Example:
            1
           / \
          2   3
         /
        4
    """

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    sol = Solution()
    print("Is Balanced:", sol.isBalanced(root))  # True


    """
    Unbalanced Tree Example:
            1
           /
          2
         /
        3
    """

    unbalanced_root = TreeNode(1)
    unbalanced_root.left = TreeNode(2)
    unbalanced_root.left.left = TreeNode(3)

    print("Is Balanced:", sol.isBalanced(unbalanced_root))  # False
