class Item():
    def __init__ (self, val, maxi):
        self.val = val
        self.maxi = maxi

def getMax(operations):
    stack = []
    maxi = float('-inf')
    answers = []
    
    for i in range(len(operations)):
        commands = operations[i].split()
        if commands[0] == "1":
            num = int(commands[1])
            if len(stack) > 0:
                maxi = max(num, stack[-1].maxi)
            else:
                maxi = max(num, float('-inf')
            item = Item(num, maxi)
            stack.append(item)
        if commands[0] == "2":
            if len(stack) > 0:
                stack.pop()
        if commands[0] == "3":
            if len(stack) > 0:
                answers.append(stack[-1].maxi)
    return answers