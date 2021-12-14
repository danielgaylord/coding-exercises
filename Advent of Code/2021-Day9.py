from collections import deque
from functools import reduce
import heapq

# Function to go through a basin and mark each spot with a -1 to count as 'visited' and increase size by 1
def mark_basin(start, heightmap):
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = deque()
    queue.append(start)
    size = 0
    while queue:
        row, col = queue.popleft()
        if heightmap[row][col] != -1:
            size += 1
            heightmap[row][col] = -1
            for rc, cc in dirs:
                new_row = row + rc
                new_col = col + cc
                if 0 <= new_row < len(heightmap) and 0 <= new_col < len(heightmap[0]) and heightmap[new_row][new_col] != -1 and heightmap[new_row][new_col] != 9:
                    queue.append((new_row, new_col))
    return size

def smoke_basin(heightmap):
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    rows = len(heightmap)
    cols = len(heightmap[0])
    risk_sum = 0

    # Initialize heap to be of 'size' 3
    sizes = [float('-inf'), float('-inf'), float('-inf')]
    heapq.heapify(sizes)
    
    for row in range(rows):
        for col in range(cols):
            
            # Part 1
            # For each spot in the heightmap, check to make sure it is smaller than all of its neighbors
            # If so, add its height + 1 to the sum of risks
            all_less = True
            for rc, cc in dirs:
                new_row = row + rc
                new_col = col + cc
                if 0 <= new_row < rows and 0 <= new_col < cols and heightmap[row][col] >= heightmap[new_row][new_col]:
                    all_less = False
            if all_less:
                risk_sum += heightmap[row][col] + 1

            # Part 2
            # For each spot in the heightmap, if it hasn't been visited yet and is not a 9 it is a new basin
            # If so, find the size of the basin and mark all of its regions as visited (Heap ensures we only keep top 3 values)
            if heightmap[row][col] != -1 and heightmap[row][col] != 9:
                heapq.heappushpop(sizes, mark_basin((row, col), heightmap))
 
    return reduce((lambda x, y: x * y), sizes)

if __name__ == "__main__":
    heightmap = []
    with open('Advent of Code/2021-Day9.txt', 'r') as input:
        for line in input:
            heightmap.append([int(char) for char in line.rstrip()])
    
    print(smoke_basin(heightmap))
        