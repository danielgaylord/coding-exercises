"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        point = head
        holds = []
        if not head:
            return head
        while point.next or point.child or holds:
            if point.child:
               holds.append(point.next)
               point.next = point.child
               point.child.prev = point
               point.child = None
            elif not point.next and holds:
                point.next = holds.pop()
                if point.next:
                    point.next.prev = point
            if point.next:
                point = point.next
        return head