# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# V1: String
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ""
        node = head
        while node:
            binary += str(node.val)
            node = node.next
            
        return int(binary, 2)

# V2: Math
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        binary = 0
        while node:
            binary *= 2
            binary += node.val
            node = node.next
            
        return binary

#V3: Bitwise
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        binary = 0
        while node:
            binary <<= 1
            binary |= node.val
            node = node.next
            
        return binary