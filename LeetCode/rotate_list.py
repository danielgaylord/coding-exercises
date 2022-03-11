# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        node = head
        
        if not head:
            return head
        
        while node.next:
            node = node.next
            count += 1
        
        node.next = head
        k = k % count
        k = count - k
        for _ in range(k):
            node = node.next
            
        head = node.next
        node.next = None
        return head
        
        