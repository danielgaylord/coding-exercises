class Solution(object):   
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total_spc = 0
        start = [0, 0]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    total_spc += 1
                if grid[row][col] == 1:
                    start = [row, col]

        def step(row, col, visited):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0
            if grid[row][col] == -1:
                return 0
            if grid[row][col] == 2:
                if visited == total_spc + 1:
                    return 1
                return 0
            grid[row][col] = -1
            temp_count = 0
            for dir in directions:
                rc = dir[0]
                cc = dir[1]
                temp_count += step(row + rc, col + cc, visited + 1)
            grid[row][col] = 0
            return temp_count

        results = step(start[0], start[1], 0)
        return results
