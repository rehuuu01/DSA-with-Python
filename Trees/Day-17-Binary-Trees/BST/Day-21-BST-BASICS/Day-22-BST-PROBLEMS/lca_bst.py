class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    """
    Find LCA of two nodes in a BST.
    Time: O(h) | Space: O(1)
    """

    while root:
        # both nodes lie in left subtree
        if p < root.val and q < root.val:
            root = root.left

        # both nodes lie in right subtree
        elif p > root.val and q > root.val:
            root = root.right

        # split happens here OR one node is root
        else:
            return root

    return None


# -------------------- MAIN (like int main) --------------------
if __name__ == "__main__":
    """
    BST:
            6
           / \
          2   8
         / \   \
        0   4   9
           / \
          3   5
    """

    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.right = TreeNode(9)

    p = 2
    q = 8

    lca = lowestCommonAncestor(root, p, q)
    print("LCA of", p, "and", q, "is:", lca.val)
