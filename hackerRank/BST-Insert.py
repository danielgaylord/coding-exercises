#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

def insert(self, val):
    #Enter you code here.
    node = self.root

    if not node:
        self.root = Node(val)
        return self.root
        
    while node:
        if val < node.info:
            if node.left:
                node = node.left
            else:
                node.left = Node(val)
                break
        else:
            if node.right:
                node = node.right
            else:
                node.right = Node(val)
                break
    
    return self.root
