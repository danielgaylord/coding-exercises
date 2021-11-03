# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, val):
            if not node.left and not node.right:
                return (val * 10) + node.val
            else:
                sum = 0
                if node.left:
                    sum += dfs(node.left, (val * 10) + node.val)
                if node.right:
                    sum += dfs(node.right, (val * 10) + node.val)
                return sum
        return dfs(root, 0)
