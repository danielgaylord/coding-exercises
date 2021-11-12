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
        
        while head and head.val == val:
            head = head.next
        
        node = head
        test = node
        while node:
            test = node.next
            while test and test.val == val:
                test = test.next
            node.next = test
            node = node.next
        
        return head
