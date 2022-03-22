class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def hashify(matrix):
            hashed = collections.defaultdict(list)
            
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if matrix[row][col]:
                        hashed[row].append([matrix[row][col], col])
            
            return hashed
        
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        
        A = hashify(mat1)
        B = hashify(mat2)
        
        result = [[0] * n for _ in range(m)]
        for matrixA_row in range(m):
            for elementA, matrixA_col in A[matrixA_row]:
                for elementB, matrixB_col in B[matrixA_col]:
                    result[matrixA_row][matrixB_col] += elementA * elementB
        
        return result
            