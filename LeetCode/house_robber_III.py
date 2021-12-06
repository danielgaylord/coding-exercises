# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dfs(node, include):
            if not node:
                return 0
            else:
                if include:
                    do = node.val + dfs(node.left, False) + dfs(node.right, False)
                else:
                    do = -1
                dont = dfs(node.left, True) + dfs(node.right, True)
                return max(do, dont)
        return dfs(root, True)