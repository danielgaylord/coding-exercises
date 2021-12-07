class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(grid)
        m = len(grid[0])
        islands = 0
        
        def mark_island(row, col):
            if grid[row][col] == "1":
                grid[row][col] = -1
                for rc, cc in dir:
                    if 0 <= row + rc < n and 0 <= col + cc < m:
                        mark_island(row + rc, col + cc)
            return
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    mark_island(row, col)
                    islands += 1
        
        return islands