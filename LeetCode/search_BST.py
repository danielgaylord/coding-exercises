class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if val == root.val:
            return root
        elif root.left and val <= root.val:
            return self.searchBST(root.left, val)
        elif root.right and val > root.val:
            return self.searchBST(root.right, val)
        else:
            return None