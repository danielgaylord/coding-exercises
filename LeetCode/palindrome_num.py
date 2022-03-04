class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        
        if x < 0:
            return False
        
        while x > 0:
            stack.append(x % 10)
            x //= 10
        
        length = len(stack)
        
        reverse = []
        for index in range(length // 2):
            reverse.append(stack.pop())
            
        if length % 2 == 1:
            stack.pop()
        
        return reverse == stack