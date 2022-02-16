from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odds = deque()
        evns = deque()
        odd_head = True
        
        while head:
            if odd_head:
                odds.append(head)
            else:
                evns.append(head)
            odd_head = not odd_head
            head = head.next
        
        head = evns.popleft()
        node = head
        while evns:
            node.next = odds.popleft()
            node = node.next
            node.next = evns.popleft()
            node = node.next
        
        while odds:
            node.next = odds.popleft()
            node = node.next
        
        node.next = None
        return head
            
            