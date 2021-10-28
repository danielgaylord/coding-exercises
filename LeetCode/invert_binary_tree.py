class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root
            