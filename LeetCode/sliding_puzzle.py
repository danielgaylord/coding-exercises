from collections import deque

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """       
        def swap(string, i, j):
            string = list(string)
            string[i], string[j] = string[j], string[i]
            return "".join(string)
        
        dirs= [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(board)
        cols = len(board[0])
        size = rows * cols
        empty = "0"
        solved = "".join(str(i) for i in range(1, size)) + empty
        moves = 0
        initial = "".join(str(col) for row in board for col in row)
        queue = deque()
        queue.append(initial)
        visited = set()
        visited.add(initial)
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == solved:
                    return moves
                zero = current.find(empty)
                for d in dirs:
                    newzero = zero + (3 * d[0]) + d[1]
                    if 0 <= newzero < size:
                        newstate = swap(current, zero, newzero)
                        if newstate not in visited:
                            queue.append(newstate)
                            visited.add(newstate)
            moves += 1
        return -1
                

