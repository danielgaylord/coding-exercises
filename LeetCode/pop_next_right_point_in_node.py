from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        node = root
        
        if not node:
            return node
        
        queue.append(node)
        while queue:
            length = len(queue)
            curr = queue.popleft()
            temp = []
            for k in range(length):
                left = curr.left
                if left:
                    temp.append(left)
                right = curr.right
                if right:
                    temp.append(right)
                if queue:
                    next = queue.popleft()
                    curr.next = next
                    curr = next
            curr.next = None
            queue.extend(temp)
        return root
                