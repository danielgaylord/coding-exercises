# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def split_list(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            while node and node.next:
                prev = node if not prev else prev.next
                node = node.next.next
            split = prev.next
            prev.next = None
            return split
            
        
        def merge(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            temp = ListNode()
            tail = temp
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                    tail = tail.next
                else:
                    tail.next = list2
                    list2 = list2.next
                    tail = tail.next
            tail.next = list1 if list1 else list2
            return temp.next
        
        split_head = split_list(head)
        left = self.sortList(head)
        right = self.sortList(split_head)
        return merge(left, right)