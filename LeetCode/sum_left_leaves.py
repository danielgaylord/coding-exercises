# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, left):
            if not node:
                return 0
            elif left and not node.left and not node.right:
                return node.val
            elif not left and not node.left and not node.right:
                return 0
            else:
                return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)
