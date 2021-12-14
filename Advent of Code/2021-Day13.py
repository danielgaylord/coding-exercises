def transparent_origami(points, folds, max_x, max_y):
    
    # Build the starting grid placing '#' on each point in coordinate list
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in points:
       grid[y][x] = "#"

    # For part 1 change len(folds) to the value 1 (for only 1 fold)
    for i in range(len(folds)):
        axis , line = folds[i]
        # rows and cols keep changing as the 'paper' gets folded
        rows = len(grid)
        cols = len(grid[0])
        # For part 1, keep track of how many '#' are visible after each fold
        count = 0
        if axis == "y":
            # Note how much 'paper' doesn't overlap itself
            # (to catch array out of bounds exceptions)
            offset = rows - (((rows - line) * 2) - 1)
            # lowest and highest row including offset
            low = min(0, offset)
            high = max(rows - 1, rows - 1 + offset)
            # Build new temp array to 'fold onto' can also mutate 'given'
            # array, but that could result in more bugs than I'd want to solve
            temp = [[" " for _ in range(cols)] for _ in range((high - low) // 2)]
            for row in range((high - low) // 2):
                # Count up from top and down from bottom
                top = low + row
                bottom = high - row
                for col in range(cols):
                    # If in negative offset (negative rows), avoid out of bounds
                    if top < 0 and grid[bottom][col] == "#":
                        count += 1
                        temp[row][col] = "#"
                    # If in positive offset (rows greater than height), avoid out of bounds
                    elif bottom > rows - 1 and grid[top][col] == "#":
                        count += 1
                        temp[row][col] = "#"
                    # Within bounds, if top or bottom has a '#'
                    elif top >= 0 and bottom <= rows - 1 and (grid[top][col] == "#" or grid[bottom][col] == "#"):
                        count += 1
                        temp[row][col] = "#"
            grid = temp
        # Same as for 'y' just replace 'row' and 'rows' with 'col' and 'cols', etc.
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

# Version 2...
# Instead of holding onto values in an array, due to memory this isn't good for larger datasets
def transparent_origami_v2(points, folds):
    # Hold onto, and keep track of, mins and maxs for final printing
    min_x = max_x = min_y = max_y = 0
    for i in range(len(folds)):
        axis , line = folds[i]
        temp = set()
        min_x, max_x = float('inf'), float('-inf')
        min_y, max_y = float('inf'), float('-inf')
        # For each point, mirror across x or y fold line
        for x, y in points:
            if axis == "y" and y > line:
                y = line - (y - line)
            elif axis == "x" and x > line:
                x = line - (x - line)
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)
            # Temp set for ease of adding new values so no dups occur, this makes temp size
            # equal to number of '#'
            if (x, y) not in temp:
                temp.add((x, y))
        points = temp

    # Represent points on grid
    grid = [[" " for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]
    for x, y in points:
       grid[y][x] = "#"
    
    # Print grid
    for row in grid:
        for col in row:
            print(col, end="")
        print()
    
    return len(points)

if __name__ == "__main__":
    points = set()
    folds = []
    max_x = 0
    max_y = 0
    with open('Advent of Code/crazy.txt', 'r') as input:
        for line in input:
            if line != "\n":

                # Bad way to check if I'm parsing a coordinate or instruction
                if line[0] != "f":
                    x, y = [int(ch) for ch in line.rstrip().split(",")]
                    # Keep track of max x and y along the way for the main function
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)
                    points.add((x, y))
                else:
                    instr = line.rstrip().split(" ")
                    axis, val = instr[2].split("=")
                    folds.append((axis, int(val)))            
    
    print(transparent_origami_v2(points, folds))
        