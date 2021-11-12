# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        node = root
        queue = deque()
        queue.append(node)
        l2r = True
        result = []
        while queue:
            temp = deque()
            hold = []
            for _ in range(len(queue)):
                element = queue.popleft()
                if element.left:
                    temp.append(element.left)
                if element.right:
                    temp.append(element.right)
                hold.append(element.val)
            if not l2r:
                hold.reverse()
            l2r = not l2r
            queue = temp
            result.append(hold)
        return result
