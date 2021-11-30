from collections import deque

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        queue = deque()
        queue.append([(0, 0), k, 0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        seen = {}
        while queue:
            loc, bombs, moves = queue.popleft()
            row, col = loc[0], loc[1]
            if row == rows - 1 and col == cols - 1:
                return moves
            for rm, cm in dirs:
                new_row = row + rm
                new_col = col + cm
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    space = grid[new_row][new_col]
                    new_k = bombs - space
                    if ((new_row, new_col) in seen and seen[(new_row, new_col)] < new_k) or (new_row, new_col) not in seen:
                        seen[(new_row, new_col)] = new_k
                        if bombs >= space:
                            queue.append([(new_row, new_col), new_k, moves + 1])
        return -1