class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root, key):
    """
    Delete a node with given key in a BST (ITERATIVE).
    Time: O(h)
    Space: O(1)
    """
    parent = None
    curr = root

    # 1️⃣ Find the node to delete
    while curr and curr.val != key:
        parent = curr
        if key < curr.val:
            curr = curr.left
        else:
            curr = curr.right

    # Key not found
    if not curr:
        return root

    # 2️⃣ Case: node has 2 children
    if curr.left and curr.right:
        # Find inorder successor (min in right subtree)
        succ_parent = curr
        succ = curr.right
        while succ.left:
            succ_parent = succ
            succ = succ.left

        # Copy successor value to current node
        curr.val = succ.val

        # Prepare to delete successor node
        curr = succ
        parent = succ_parent

    # 3️⃣ Case: node has 0 or 1 child
    child = curr.left if curr.left else curr.right

    # If deleting the root node
    if not parent:
        return child

    # Reconnect parent to child
    if parent.left == curr:
        parent.left = child
    else:
        parent.right = child

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

    """
    Expected BST after deletion of 3:
            5
           / \
          4   7
         /     \
        2       8
    """
