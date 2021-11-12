# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        while node:
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                return node
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                node = node.right
        return None
