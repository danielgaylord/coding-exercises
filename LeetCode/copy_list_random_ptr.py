"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        point = head
        while point:
            new = Node(point.val)
            new.next = point.next
            point.next = new
            point = new.next
        
        point = head
        while point:
            point.next.random = point.random.next if point.random else None
            point = point.next.next
        
        old_list = head
        new_head = head.next
        new_list = head.next
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next
            
        return new_head