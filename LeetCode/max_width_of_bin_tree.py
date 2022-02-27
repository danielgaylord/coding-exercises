from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        nodes = deque()
        nodes.append((root, 0))
        max_len = 0
        
        while nodes:
            level_len = len(nodes)
            _, level_index = nodes[0]
            
            for _ in range(level_len):
                node, node_index = nodes.popleft()
                if node.left:
                    nodes.append((node.left, 2 * node_index))
                if node.right:
                    nodes.append((node.right, 2 * node_index + 1))
                
                max_len = max(max_len, node_index - level_index + 1)
        
        return max_len