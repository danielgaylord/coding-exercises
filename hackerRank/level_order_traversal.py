from collections import deque
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    queue = deque()
    queue.append(root)
    while queue:
        temp = deque()
        while queue:
            node = queue.popleft()
            print(node.info, end = " ")
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        queue = temp
