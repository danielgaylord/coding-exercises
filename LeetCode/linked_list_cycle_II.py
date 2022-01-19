# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Using set/hashtable
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        visited = set()
        #visited = {}
        
        if not node:
            return None
        
        while node.next:
            if node in visited:
                return node
            visited.add(node)
            #visited[node] = 1
            node = node.next
            
        return None

# Using two pointers
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        if not fast.next or not fast.next.next:
            return None
            
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return fast