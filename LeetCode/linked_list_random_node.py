import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Typical randomness
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        node = head
        while node:
            self.length += 1
            node = node.next

    def getRandom(self) -> int:
        if not self.head:
            return None
        time = random.randint(1, self.length)
        node = self.head
        for _ in range (1, time):
            node = node.next
        return node.val

# Resivoir sampling
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        chosen = 0
        node = self.head
        while node:
            if random.random() < 1 / scope:
                chosen = node.val
            scope += 1
            node = node.next
        return chosen

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()