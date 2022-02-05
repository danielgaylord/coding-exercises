import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        result = []
        heapq.heapify(result)
        empty = True
        
        for link in lists:
            if link:
                empty = False
            node = link
            while node:
                heapq.heappush(result, node.val)
                node = node.next

        if empty:
            return None
        
        head = ListNode()
        node = head
        while result:
            node.val = heapq.heappop(result)
            if not result:
                node.next = None
            else:
                node.next = ListNode()
            node = node.next
        
        return head