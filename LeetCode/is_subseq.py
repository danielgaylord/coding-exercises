class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_point = 0

        for index, char in enumerate(t):
            if char == s[s_point]:
                s_point += 1
                if s_point == len(s):
                    return True
        
        return False
        
        