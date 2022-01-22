class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        
        for stones in range(1, n + 1):
            for remove in range(1, int(stones ** .5) + 1):
                if not dp[stones - (remove ** 2)]:
                    dp[stones] = True
                    break
        return dp[n]