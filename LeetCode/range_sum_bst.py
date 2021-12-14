# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:       
        def helper(node, low, high):
            if not node:
                return 0
            
            sum = 0
            if low <= node.val <= high:
                sum += node.val
            if node.left:
                sum += helper(node.left, low, high)
            if node.right:
                sum += helper(node.right, low, high)
            return sum
        return helper(root, low, high)