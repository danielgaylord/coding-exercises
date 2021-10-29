import collections

class Solution:   
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minit = 0
        queue = collections.deque()
        directions = [[0,1], [1,0], [0,-1], [-1, 0]]
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    queue.append([row, col])
        
        while queue:
            curr_rot = queue.copy()
            queue.clear()
            while curr_rot:
                rot_row, rot_col = curr_rot.popleft()
                for cg_row, cg_col in directions:
                    if rot_row + cg_row >= 0 and rot_col + cg_col >= 0 and rot_row + cg_row < len(grid) and rot_col + cg_col < len(grid[0]):
                        if grid[rot_row + cg_row][rot_col + cg_col] == 1:
                            grid[rot_row + cg_row][rot_col + cg_col] = 2
                            queue.append([rot_row + cg_row, rot_col + cg_col])
            if queue:
                minit += 1
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return -1

        return minit