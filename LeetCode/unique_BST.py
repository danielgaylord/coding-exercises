class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        dp[0] = dp[1] = 1
        for nodes in range(2, n + 1):
            for rem in range(1, nodes + 1):
                dp[nodes] += dp[rem - 1] * dp[nodes - rem]
        return dp[n]