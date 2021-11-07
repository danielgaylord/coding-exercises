def create_min_BST(array):
    if len(array) == 0:
        return None
    if len(array) == 1:
        return Node(array[0])
    mid = (0 + len(array)) // 2
    node = Node(array[min])
    node.left = create_min_BST(array[:mid])
    node.right = create_min_BST(array[mid + 1:])
    return node