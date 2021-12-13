class Solution:
    def numTilings(self, n: int) -> int:
        mod = (10 ** 9) + 7
        dp = [0] * (n + 1)
        
        def tilingHelper(num):
            if dp[num] != 0:
                return dp[num]
            if 0 <= num <= 1:
                dp[num] = 1
                return dp[num]
            dp[num] += tilingHelper(num - 1) + tilingHelper(num - 2)
            if num >= 3:
                dp[num] += tilingHelper(num - 3) * 2
            if num >= 4:
                for i in range(4, num + 1):
                    dp[num] += tilingHelper(num - i) * 2
            return dp[num]
        
        return tilingHelper(n) % mod