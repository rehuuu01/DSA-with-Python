class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root, key):
    """
    Delete a node with given key in a BST.
    Time: O(h) | Space: O(h)
    """

    if not root:
        return None

    if key < root.val:
        root.left = deleteNode(root.left, key)

    elif key > root.val:
        root.right = deleteNode(root.right, key)

    else:
        # Case 1 & 2: node with 0 or 1 child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 3: node with 2 children
        # Find inorder successor (min in right subtree)
        successor = root.right
        while successor.left:
            successor = successor.left

        root.val = successor.val
        root.right = deleteNode(root.right, successor.val)

    return root


# Utility function: inorder traversal (to verify BST)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


# -------------------- MAIN (like int main) --------------------
if __name__ == "__main__":
    """
    Initial BST:
            5
           / \
          3   7
         / \   \
        2   4   8
    """

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)

    print("Inorder before deletion:")
    inorder(root)

    key = 3
    root = deleteNode(root, key)

    print("\nInorder after deleting", key, ":")
    inorder(root)
