"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def postOrder(root):
    #Write your code here
    node = root
    if not node:
        return 
    postOrder(node.left)
    postOrder(node.right)
    print(node.info, end = " ")
    return