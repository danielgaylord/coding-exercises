import collections

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            leftNode = False
            rightNode = False
            currNode = queue.popleft()
            if currNode.left and (currNode.left.left or currNode.left.right):
                queue.append(currNode.left)
                leftNode = True
            if currNode.right and (currNode.right.left or currNode.right.right):
                queue.append(currNode.right)
                rightNode = True
            if currNode.val % 2 == 0:
                if leftNode:
                    if currNode.left.left:
                        result += currNode.left.left.val
                    if currNode.left.right:
                        result += currNode.left.right.val
                if rightNode:
                    if currNode.val % 2 == 0:
                        if currNode.right.left:
                            result += currNode.right.left.val
                        if currNode.right.right:
                            result += currNode.right.right.val
        return result
