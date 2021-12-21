class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if len([ones for ones in bin(n)[2:] if ones == "1"]) == 1 and n > 0 else False