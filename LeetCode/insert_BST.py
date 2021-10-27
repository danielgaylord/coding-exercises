class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        currNode = root
        while currNode != None:
            if val <= currNode.val:
                if currNode.left == None:
                    currNode.left = TreeNode(val)
                    return root
                else:
                    currNode = currNode.left
            else:
                if currNode.right == None:
                    currNode.right = TreeNode(val)
                    return root
                else:
                    currNode = currNode.right
        return TreeNode(val)
        