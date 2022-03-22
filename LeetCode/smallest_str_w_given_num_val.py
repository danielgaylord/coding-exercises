class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        points = k - n
        result = []
        
        for pos in range(n):
            spend = min(k - (n - pos - 1), 26)
            char = chr(spend + ord('a') - 1)
            result.append(char)
            k -= spend
        
        return "".join(result[::-1])