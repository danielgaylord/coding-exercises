class Solution(object):
    def mark(self, board, row, col):
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        board[row][col] = "+"
        for dir in directions:
            rc = dir[0]
            cc = dir[1]
            if 0 <= row + rc < len(board) and 0 <= col + cc < len(board[0]) and board[row + rc][col + cc] == "O":
                self.mark(board, row + rc, col + cc)
    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[row])):
                if (row == 0 or row == len(board) - 1 or col == 0 or col == len(board[row]) - 1) and board[row][col] == "O":
                    self.mark(board, row, col)
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "+":
                    board[row][col] = "O"
