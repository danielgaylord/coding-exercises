# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        quick = head
        move_slow = True
        while quick.next:
            if move_slow:
                slow = slow.next
            move_slow = not move_slow
            quick = quick.next
        
        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next

        node = head
        while stack:
            print(node.val)
            temp = node.next
            node.next = stack.pop()
            node = node.next
            if not stack:
                break
            node.next = temp
            node = node.next
        if node.next:
            node
        node.next = None