class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for l in range(1, k + 1):
            remainder = ((remainder * 10) + 1) % k
            if remainder == 0:
                return l
        return -1