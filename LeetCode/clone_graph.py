from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])
        
        while queue:
            temp = queue.popleft()
            for neighbor in temp.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[temp].neighbors.append(visited[neighbor])
        
        return visited[node]
        
        