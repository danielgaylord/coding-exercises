import collections

def countNodes(self, root):
    curr = None
    count = 0
    queue = collections.deque()
    if root == None:
        return count
    queue.append(root)
    while queue:
        curr = queue.popleft()
        count += 1
        if curr.left != None:
            queue.append(curr.left)
        if curr.right != None:
            queue.append(curr.right)
    return count
