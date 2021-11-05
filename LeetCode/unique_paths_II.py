class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for _ in range(rows)] for _ in range(cols)]
        for x in range(rows):
            for y in range(cols):
                if obstacleGrid[x][y] == 1:
                    dp[x][y] = 0
                elif x == 0 and y == 0:
                    dp[x][y] = 1
                elif x == 0:
                    dp[x][y] = dp[x][y - 1]
                elif y == 0:
                    dp[x][y] = dp[x - 1][y]
                else:
                    dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        return dp[rows - 1][cols - 1]

