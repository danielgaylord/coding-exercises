# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hold = ListNode()
        node = head
        
        while node:
            pre = hold
            while pre.next and pre.next.val < node.val:
                pre = pre.next
            
            upcoming = node.next
            
            node.next = pre.next
            pre.next = node
            
            node = upcoming
        
        return hold.next