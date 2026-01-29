class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        result = []

        def preorder(node):
            if not node:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return result


if __name__ == "__main__":
    # Manually creating the tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    sol = Solution()
    print("Preorder Traversal:", sol.preorderTraversal(root))

