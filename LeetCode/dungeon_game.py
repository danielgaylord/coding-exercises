from collections import deque

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[float('-inf') for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        queue.append((rows - 1, cols - 1))
        health = 0
        while queue:
            spacer, spacec = queue.popleft()
            if spacer == rows - 1 and spacec == cols - 1:
                health = max(-dungeon[spacer][spacec], 0) + 1
            elif spacer == rows - 1:
                health = max(dp[spacer][spacec + 1] - dungeon[spacer][spacec], 1)
            elif spacec == cols - 1:
                health = max(dp[spacer + 1][spacec] - dungeon[spacer][spacec], 1)
            else:
                health = min(dp[spacer][spacec - 1], dp[spacer - 1][spacec]) + max(-dungeon[spacer][spacec], 0)
            dp[spacer][spacec] = health
            if spacer - 1 >= rows:
                queue.append((spacer - 1, spacec))
            if spacec - 1 >= cols:
                queue.append((spacer, spacec - 1))
        return dp[0][0]