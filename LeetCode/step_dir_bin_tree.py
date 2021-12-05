# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, target):
            if not node:
                return [False, ""]
            elif node.val == target:
                return [True, ""]
            else:
                left = dfs(node.left, target)
                right = dfs(node.right, target)
                if left[0]:
                    return [left[0], "L" + left[1]]
                elif right[0]:
                    return [right[0], "R" + right[1]]
                else:
                    return [False, ""]
        startPath = dfs(root, startValue)[1]
        destPath = dfs(root, destValue)[1]
        while len(startPath) > 0 and len(destPath) > 0 and startPath[0] == destPath[0]:
            startPath = startPath[1:]
            destPath = destPath[1:]
        startPath = "U" * len(startPath)
        return startPath + destPath