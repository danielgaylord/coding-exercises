from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        new_root = Node(root.val)
        queue = deque([(root, new_root)])
        
        while queue:
            old, new = queue.popleft()
            
            for child in old.children:
                node = Node(child.val)
                new.children.append(node)
                queue.append((child, node))
        
        return new_root