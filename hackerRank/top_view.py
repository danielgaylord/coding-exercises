"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    def leftview(node):
        if not node:
            return
        leftview(node.left)
        print(node.info, end = " ")
        return
    def rightview(node):
        if not node:
            return
        print(node.info, end = " ")
        rightview(node.right)
        return
    leftview(root.left)
    print(root.info, end = " ")
    rightview(root.right)