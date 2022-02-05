# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        head = None
        if node1.val < node2.val:
            head = node1
            node1 = node1.next
        else:
            head = node2
            node2 = node2.next
        
        snode = head
        while node1 and node2:
            if node1.val < node2.val:
                snode.next = node1
                node1 = node1.next
            else:
                snode.next = node2
                node2 = node2.next
            snode = snode.next
        
        if not node1:
            snode.next = node2
        if not node2:
            snode.next = node1
        