def linked_palindrome(root):
    stack = []
    pointer = root
    runner = root
    while runner:
        stack.append(pointer.val)
        pointer = pointer.next
        runner = runner.next
        if runner:
            runner = runner.next
        else:
            stack.pop()
    while pointer:
        if pointer.val != stack.pop():
            return False
        pointer = pointer.next
    return True
            
