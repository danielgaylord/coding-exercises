class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        chars = {}
        
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
                
        for char in t:
            if char in chars:
                if chars[char] == 0:
                    return char
                chars[char] -= 1
            else:
                return char