class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def dp(row, col1, col2):
            if not (0 <= col1 < len(grid[0])) or not (0 <= col2 < len(grid[0])):
                return float(-inf)
            subtotal = 0
            subtotal += grid[row][col1]
            if col1 != col2:
                subtotal += grid[row][col2]
            if row != len(grid) - 1:
                new_row = row + 1
                subtotal += max(dp(new_row, col1 - 1, col2 - 1), dp(new_row, col1, col2 - 1), dp(new_row, col1 + 1, col2 - 1), dp(new_row, col1 - 1, col2), dp(new_row, col1, col2), dp(new_row, col1 + 1, col2), dp(new_row, col1 - 1, col2 + 1), dp(new_row, col1, col2 + 1), dp(new_row, col1 + 1, col2 + 1))
            return subtotal
        
        return dp(0, 0, len(grid[0]) - 1)