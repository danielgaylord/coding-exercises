# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inOrder(node):
            if not node:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)
        
        node1 = root1
        result1 = inOrder(node1)
        node2 = root2
        result2 = inOrder(node2)
        result = []
        p1 = 0
        p2 = 0
        
        if not result1:
            return result2
        
        if not result2:
            return result1
        
        while p1 < len(result1) and p2 < len(result2):
            if result1[p1] < result2[p2]:
                result.append(result1[p1])
                p1 += 1
            else:
                result.append(result2[p2])
                p2 += 1
        
        while p1 < len(result1):
            result.append(result1[p1])
            p1 += 1
        
        while p2 < len(result2):
            result.append(result2[p2])
            p2 += 1
        
        return result