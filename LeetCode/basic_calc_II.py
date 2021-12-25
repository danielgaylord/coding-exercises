class Solution:
    def calculate(self, s: str) -> int:
        if not s or s == "":
            return 0
        stack = []
        curr_num = 0
        op = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = (curr_num * 10) + int(s[i])
            if s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/" or i == len(s) - 1:
                if  op == "+" or op == "-":
                    stack.append(curr_num if op == "+" else -curr_num)
                elif op == "*":
                    stack.append(stack.pop() * curr_num)
                elif op == "/":
                    stack.append(int(stack.pop() / curr_num))
                op = s[i]
                curr_num = 0
        result = 0
        while stack:
            result += stack.pop()
        return result
                
                