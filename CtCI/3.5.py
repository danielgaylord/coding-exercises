class SortedStack():
    stack = []
    holder = []

    def __init__(self):
        pass

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1

    def push(self, val):
        while self.peek() < val and not self.isEmpty():
            self.holder.append(self.stack.pop())
        self.stack.append(val)
        while self.holder:
            self.stack.append(self.holder.pop())
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1

    def isEmpty(self):
        return len(self.stack) == 0
