class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        target = len(matrix)
        
        for row in matrix:
            if len(set(row)) != target:
                return False
        
        for col in range(len(matrix[0])):
            total = set()
            for row in range(len(matrix)):
                total.add(matrix[row][col])
            if len(total) != target:
                return False
            
        return True