class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Recursive approach to find maximum depth of a binary tree.

        Time Complexity: O(n)
        Space Complexity: O(h) where h is the height of the tree
        """
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


# -------- Example Usage --------
if __name__ == "__main__":
    """
    Example Binary Tree:
            1
           / \
          2   3
         / \
        4   5

    Maximum Depth = 3
    """

    # Creating nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Solution instance
    sol = Solution()

    # Finding maximum depth
    result = sol.maxDepth(root)

    print("Maximum Depth of Binary Tree:", result)
