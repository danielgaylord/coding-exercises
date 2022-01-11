# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        def pathway(node, curr_bin):
            curr_bin += str(node.val)
            
            if not node.left and not node.right:
                self.result += int(curr_bin, 2)
            
            if node.left:
                pathway(node.left, curr_bin)
            
            if node.right:
                pathway(node.right, curr_bin)
        
        pathway(root, "")
        
        return self.result