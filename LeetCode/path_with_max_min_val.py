class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pq = []
        result = grid[0][0]
        visited = [[False] * cols for _ in range(rows)]
        heapq.heappush(pq, (-grid[0][0], 0, 0))
        visited[0][0] = True
        
        while pq:
            curr_val, curr_row, curr_col = heapq.heappop(pq)
            result = min(result, grid[curr_row][curr_col])
            
            if curr_row == rows - 1 and curr_col == cols - 1:
                break
            
            for dir_row, dir_col in dirs:
                new_row = curr_row + dir_row
                new_col = curr_col + dir_col
                
                if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                    heapq.heappush(pq, (-grid[new_row][new_col], new_row, new_col))
                    visited[new_row][new_col] = True
        
        return result
        
        