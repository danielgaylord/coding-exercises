class Solution:
    def myAtoi(self, s: str) -> int:
        numbers = "0123456789"
        max_val = (2 ** 31) - 1
        min_val = -(2 ** 31)
        
        ind = 0
        sign = 1
        val = 0
        
        if len(s) == 0:
            return val

        while ind < len(s) and s[ind] == " ":
            ind += 1
            
        if ind >= len(s):
            return val
        
        if s[ind] == "-":
            sign = -sign
            ind += 1
        elif s[ind] == "+":
            ind += 1
        
        while ind < len(s) and s[ind] in numbers:
            val *= 10
            val += numbers.index(s[ind])
            ind += 1
        
        val *= sign
        if val < min_val:
            val = min_val
        if val > max_val:
            val = max_val
        
        return val