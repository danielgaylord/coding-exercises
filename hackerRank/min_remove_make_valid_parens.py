class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pass_one = []
        balance = 0
        opens = 0
        for char in s:
            if char == "(":
                balance += 1
                opens += 1
            if char == ")":
                if balance == 0:
                    continue
                balance -= 1
            pass_one.append(char)
        
        result = []
        keep_open = opens - balance
        for char in pass_one:
            if char == "(":
                keep_open -= 1
                if keep_open < 0:
                    continue
            result.append(char)
        
        return "".join(result)