# BFS Solution
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        return dp[m - 1][n - 1]

# DFS Solution
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for c in range(n)] for r in range(m)]
        
        def helper(row, col):
            if row >= m or col >= n:
                return 0
            if row == m - 1 and col == n - 1:
                return 1
            if dp[row][col] == 0:
                dp[row][col] = helper(row + 1, col) + helper(row, col + 1)
            return dp[row][col]
        return helper(0, 0)