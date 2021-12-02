# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd_point = head
        even_point = head.next
        even_start = even_point
        
        while even_point.next:
            odd_point.next = even_point.next
            odd_point = odd_point.next
            if not odd_point.next:
                break
            even_point.next = odd_point.next
            even_point = even_point.next
        
        even_point.next = None
        odd_point.next = even_start
        
        return head
        