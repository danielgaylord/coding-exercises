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
        if start[0] == end[0]:
            const = start[0]
            begin = min(start[1], end[1])
            end = max(start[1], end[1])
            for i in range(begin, end + 1):
                floor[i][const] += 1
        elif start[1] == end[1]:
            const = start[1]
            begin = min(start[0], end[0])
            end = max(start[0], end[0])
            for i in range(begin, end + 1):
                floor[const][i] += 1
    
    count = 0
    for r in floor:
        for c in r:
            if c > 1:
                count += 1
    
    return count

if __name__ == "__main__":
    print(hydrothermal_venture())
        