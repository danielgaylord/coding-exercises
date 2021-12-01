"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        node1 = head
        node2 = node1.next
        
        while True:
            if node1.val < insertVal <= node2.val or node2 == head or (node2.val < node1.val and (insertVal <= node2.val or insertVal >= node1.val)):
                break
            node1 = node1.next
            node2 = node2.next
            
        new_node = Node(insertVal)
        new_node.next = node2
        node1.next = new_node
        
        return head
            
        
            