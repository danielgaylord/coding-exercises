# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_depth(node):
            if not node:
                return 0
            else:
                return max(max_depth(node.left) + 1, max_depth(node.right) + 1)
        return max_depth(root)