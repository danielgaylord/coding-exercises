# My version, TLE on larger data sets
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        
        def remove_digit(num: str) -> str:
            smallest_num = int(num)
            prev = 0
            
            for index in range(len(num)):
                if int(num[index]) >= prev:
                    new_num = num[:index] + num[index + 1:]
                    if new_num == "":
                        new_num = "0"
                    smallest_num = min(smallest_num, int(new_num))
                    prev = int(num[index])
                else:
                    break
            
            return str(smallest_num)
        
        for time in range(k):
            num = remove_digit(num)
        
        return num

# Stack solution from explaination
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            stack.append(digit)
        
        result = stack[:-k] if k else stack
        return "".join(result).lstrip("0") or "0"