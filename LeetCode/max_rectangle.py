class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_area = 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '0':
                    continue
                
                if col:
                    width = dp[row][col] = dp[row][col - 1] + 1
                else:
                    width = dp[row][col] = 1
                    
                for k in range(row, -1, -1):
                    width = min(width, dp[k][col])
                    max_area = max(max_area, width * (row - k + 1))
        return max_area