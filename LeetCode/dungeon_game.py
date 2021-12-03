from collections import deque

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        queue.append((rows - 1, cols - 1))
        health = 0
        #while queue:
        #   spacer, spacec = queue.popleft()
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col == cols - 1:
                    health = max(-dungeon[row][col], 0) + 1
                elif row == rows - 1:
                    health = max(dp[row][col + 1] - dungeon[row][col], 1)
                elif col == cols - 1:
                    health = max(dp[row + 1][col] - dungeon[row][col], 1)
                else:
                    health = min(max(dp[row + 1][col] - dungeon[row][col], 1), max(dp[row][col + 1] - dungeon[row][col], 1))
                dp[row][col] = health
        #    if spacer - 1 >= 0:
        #        queue.append((spacer - 1, spacec))
        #    if spacec - 1 >= 0:
        #        queue.append((spacer, spacec - 1))
        return dp[0][0]