class MinElement():
    def __init__(self, val, minVal):
        self.minVal = minVal
        self.val = val

class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append(MinElement(val, val))
        else:
            minVal = min(self.stack[-1].minVal, val)
            self.stack.append(MinElement(val, minVal))
        return None

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) != 0:
            self.stack.pop()
        return None

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.stack[-1].val

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
           return self.stack[-1].minVal
