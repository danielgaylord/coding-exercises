# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def diffHelper(node):
            minNode = float('inf')
            maxNode = float('-inf')
            maxDiff = 0
            if not node.left and not node.right:
                return node.val, node.val, 0
            if node.left:
                minLeft, maxLeft, leftDiff = diffHelper(node.left)
                minNode = min(minNode, minLeft)
                maxNode = max(maxNode, maxLeft)
                maxDiff = max(maxDiff, leftDiff)
            if node.right:
                minRight, maxRight, rightDiff = diffHelper(node.right)
                minNode = min(minNode, minRight)
                maxNode = max(maxNode, maxRight)
                maxDiff = max(maxDiff, rightDiff)
            maxDiff = max(maxDiff, abs(node.val - minNode), abs(node.val - maxNode))
            return min(minNode, node.val), max(maxNode, node.val), maxDiff
        
        minNode, maxNode, maxDiff = diffHelper(root)
        return maxDiff
            