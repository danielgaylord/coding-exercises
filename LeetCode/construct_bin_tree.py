# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ele = postorder[-1]
            pos = inorder.index(ele)
        else:
            ele = None
            pos = -1
        if pos > -1:
            node = TreeNode(ele)
            node.left = self.buildTree(inorder[:pos], postorder[:pos])
            node.right = self.buildTree(inorder[pos + 1:], postorder[pos:-1])
            return node
        else:
            return None