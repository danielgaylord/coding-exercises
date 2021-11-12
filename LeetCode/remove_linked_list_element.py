# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        while head.val == val:
            head = head.next
        
        node = head
        while node:
            if node.next and node.next.val == val:
                node.next = node.next.next
            node = node.next
        
        return head
