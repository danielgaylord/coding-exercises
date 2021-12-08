# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.result = [0]
        
        def tiltHelper(node):
            if not node:
                return 0
            sumLeft = tiltHelper(node.left)
            sumRight = tiltHelper(node.right)
            self.result += abs(sumLeft - sumRight)
            return sumLeft + sumRight + node.val
        
        tiltHelper(root)
        return self.result
        
        
        