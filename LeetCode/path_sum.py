# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, target):
            if not node:
                return False
            elif not node.left and not node.right:
                if node.val == target:
                    return True
                else:
                    return False
            else:
                return dfs(node.left, target - node.val) or dfs(node.right, target - node.val)
        return dfs(root, targetSum)
            