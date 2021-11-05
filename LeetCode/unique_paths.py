from collections import deque

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        queue = deque()
        queue.append((0, 0))
        while queue:
            x, y = queue.popleft()
            if x == 0 and y == 0:
                dp[x][y] = 1
            elif x == 0:
                dp[x][y] = dp[x - 1][y]
            elif y == 0:
                dp[x][y] = dp[x][y - 1]
            else:
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
            if x == m - 1 and y == n - 1:
                return dp[x][y]
            queue.append((x + 1, y))
            queue.append((x, y + 1))
