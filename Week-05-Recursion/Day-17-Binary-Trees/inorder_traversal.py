from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(values):
    if not values or values[0] == -1:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if values[i] != -1:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] != -1:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result


if __name__ == "__main__":
    values = list(map(int, input("Enter tree nodes (level order, -1 for NULL): ").split()))
    root = build_tree(values)

    sol = Solution()
    print("Inorder Traversal:", sol.inorderTraversal(root))
