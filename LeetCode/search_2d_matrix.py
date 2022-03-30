class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        
        low, high = 0, rows * cols - 1
        while low <= high:
            mid = (low + high) // 2
            mid_element = matrix[mid // cols][mid % cols]
            if target == mid_element:
                return True
            else:
                if target < mid_element:
                    high = mid - 1
                else:
                    low = mid + 1
        return False
        