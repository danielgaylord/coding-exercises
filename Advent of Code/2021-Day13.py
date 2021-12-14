def transparent_origami(points, folds, max_x, max_y):
    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in points:
       grid[y][x] = "#"

    for i in range(len(folds)):
        axis , line = folds[i]
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        if axis == "y":
            offset = rows - (((rows - line) * 2) - 1)
            low = min(0, offset)
            high = max(rows - 1, rows - 1 + offset)
            temp = [["." for _ in range(cols)] for _ in range((high - low) // 2)]
            for row in range((high - low) // 2):
                top = low + row
                bottom = high - row
                for col in range(cols):
                    if top < 0 and grid[bottom][col] == "#":
                        count += 1
                        temp[row][col] = "#"
                    elif bottom > rows - 1 and grid[top][col] == "#":
                        count += 1
                        temp[row][col] = "#"
                    elif top >= 0 and bottom <= rows - 1 and (grid[top][col] == "#" or grid[bottom][col] == "#"):
                        count += 1
                        temp[row][col] = "#"
            grid = temp
        if axis == "x":
            offset = cols - (((cols - line) * 2) - 1)
            low = min(0, offset)
            high = max(cols - 1, cols - 1 + offset)
            temp = [["." for _ in range((high - low) // 2)] for _ in range(rows)]
            for row in range(rows):
                for col in range((high - low) // 2):
                    left = low + col
                    right = high - col
                    if left < 0 and grid[row][right] == "#":
                        count += 1
                        temp[row][col] = "#"
                    elif right > cols - 1 and grid[row][left] == "#":
                        count += 1
                        temp[row][col] = "#"
                    elif left >= 0 and right <= cols - 1 and (grid[row][left] == "#" or grid[row][right] == "#"):
                        count += 1
                        temp[row][col] = "#"
            grid = temp

    for row in grid:
        for col in row:
            print(col, end="")
        print()
    
    return count

if __name__ == "__main__":
    points = []
    folds = []
    max_x = 0
    max_y = 0
    with open('Advent of Code/2021-Day13.txt', 'r') as input:
        for line in input:
            if line != "\n":
                if line[0] != "f":
                    x, y = [int(ch) for ch in line.rstrip().split(",")]
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)
                    points.append((x, y))
                else:
                    instr = line.rstrip().split(" ")
                    axis, val = instr[2].split("=")
                    folds.append((axis, int(val)))            
    
    print(transparent_origami(points, folds, max_x, max_y))
        