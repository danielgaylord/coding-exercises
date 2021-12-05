def hydrothermal_venture():
    segments = []
    with open('Advent of Code/2021-Day5.txt', 'r') as input:
        for line in input:
            line = line.rstrip().split(" -> ")
            seg = [[int(val) for val in point.split(",")] for point in line]
            segments.append(seg)
    
    maxRow = 0
    maxCol = 0
    for segment in segments:
        for point in segment:
            maxCol = max(maxCol, point[0])
            maxRow = max(maxRow, point[1])
    floor = [[0 for _ in range(maxCol + 1)] for _ in range(maxRow + 1)]
    
    for start, end in segments:
        beginX = start[0]
        beginY = start[1]
        endX = end[0]
        endY = end[1]
        xChange = 0
        yChange = 0
        if beginX < endX:
            xChange = 1
        elif beginX > endX:
            xChange = -1
        if beginY < endY:
            yChange = 1
        elif beginY > endY:
            yChange = -1
        while beginX != endX or beginY != endY:
            floor[beginY][beginX] += 1
            beginX += xChange
            beginY += yChange
        floor[beginY][beginX] += 1
    
    count = 0
    for r in floor:
        for c in r:
            if c > 1:
                count += 1
    return count

if __name__ == "__main__":
    print(hydrothermal_venture())
        