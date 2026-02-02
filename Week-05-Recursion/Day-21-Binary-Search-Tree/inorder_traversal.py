class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    """
    In-order: Left -> Root -> Right
    
    For BST: Returns values in SORTED order!
    
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    result = []
    
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)      # Visit left subtree
        result.append(node.val) # Visit root
        inorder(node.right)     # Visit right subtree
    
    inorder(root)
    return result


# Test
#         8
#        / \
#       3   10
#      / \    \
#     1   6   14
#        / \  /
#       4  7 13

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

print(inorder_traversal(root))
# Output: [1, 3, 4, 6, 7, 8, 10, 13, 14] ← SORTED!