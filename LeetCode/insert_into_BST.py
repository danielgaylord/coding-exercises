from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def bst(node, val):
            if val < node.val:
                if node.left:
                    bst(node.left, val)
                else:
                    node.left = TreeNode(val)
            if val > node.val:
                if node.right:
                    bst(node.right, val)
                else:
                    node.right = TreeNode(val)
        
        bst(root, val)
        return root