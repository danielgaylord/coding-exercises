def rotate_matrix(matrix):
    for row in range(len(matrix) // 2):
        end = len(matrix[row]) - row - 1
        for col in range(row, end):
            matrix[row, col], matrix[row, end], matrix[end, end], matrix[end, col] = matrix[row, end], matrix[end, end], matrix[end, col], matrix[row, col]
