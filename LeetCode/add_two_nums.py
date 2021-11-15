# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        sum = l1.val + l2.val
        carry = sum // 10
        head = ListNode(sum % 10)
        node = head
        l1 = l1.next
        l2 = l2.next
        while l1 or l2: 
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            node.next = ListNode(sum % 10)
            node = node.next
        if carry > 0:
            node.next = ListNode(carry)
        return head