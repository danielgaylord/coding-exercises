def pondSizes(grid):
    ponds = set()
    for row in range(len(grid)):
        for col in range(len(grid[r])):
            if grid[row][col] == 0:
                size = checkSize(grid, row, col)
                ponds.append(size)
    return ponds

def checkSize(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] != 0:
        return 0
    size = 1
    grid[row][col] = -1
    for rowDir in range(-1, 2):
        for colDir in range(-1, 2):
            size += checkSize(grid, row + rowDir, col + colDir)
    return size
