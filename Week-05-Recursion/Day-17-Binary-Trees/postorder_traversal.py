class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        result = []

        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)

        postorder(root)
        return result


if __name__ == "__main__":
    # Manually creating the tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    sol = Solution()
    print("Postorder Traversal:", sol.postorderTraversal(root))
