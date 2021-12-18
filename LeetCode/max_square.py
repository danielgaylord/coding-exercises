class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        max_square = 0
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "0":
                    continue
                
                if col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row][col - 1] + 1
                width = dp[row][col]
                
                for check in range(row, -1, -1):
                    width = min(width, dp[check][col])
                    length = min(width, row - check + 1)
                    max_square = max(max_square, length ** 2)
        
        return max_square
        