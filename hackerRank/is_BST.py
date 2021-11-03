""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    def dfs(node, min, max):
        if not node:
            return True
        if not (min < node.data < max):
            return False
        return dfs(node.left, min, node.data) and dfs(node.right, node.data, max)
    
    return dfs(root, float('-inf'), float('inf'))
