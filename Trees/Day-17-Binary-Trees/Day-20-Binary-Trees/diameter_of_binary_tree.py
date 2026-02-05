class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        Calculate the diameter of a binary tree.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        self.diameter = 0

        def height(node):
            if node is None:
                return 0

            # Height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # Update diameter (number of edges)
            self.diameter = max(self.diameter, left_height + right_height)

            # Return height of current node
            return max(left_height, right_height) + 1

        height(root)
        return self.diameter


# -------- Example Usage --------
if __name__ == "__main__":
    """
    Example Binary Tree:
              1
             / \
            2   3
           / \
          4   5

    Longest path: 4 -> 2 -> 1 -> 3
    Diameter = 3 edges
    """

    # Create tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    result = sol.diameterOfBinaryTree(root)

    print("Diameter of Binary Tree:", result)
