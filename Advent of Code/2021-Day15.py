import unittest, heapq

# Read puzzle input and return as usable data structure
def parse_input(file):
    grid = []
    with open(file, 'r') as input:
        for line in input:
            row = [ch for ch in line.rstrip()]
            grid.append(row)
    return grid

def chiton(file, growth):
    grid = parse_input(file)
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    rows = len(grid)
    cols = len(grid[0])
    start = (0, 0)
    end = ((rows * growth) - 1, (cols * growth) - 1)
    to_visit = [(0, start)]
    distances = {}
    heapq.heapify(to_visit)
    while to_visit:
        dist, loc = heapq.heappop(to_visit)
        if loc == end:
            return dist
        row, col = loc[0], loc[1]
        if loc in distances and dist > distances[loc]:
            continue
        for rc, cc, in dirs:
            new_row = row + rc
            new_col = col + cc
            if 0 <= new_row < (rows * growth) and 0 <= new_col < (cols * growth):
                weight = int(grid[new_row % rows][new_col % rows])
                weight += (new_row // rows) + (new_col // cols)
                if weight > 9:
                    weight %= 9
                new_dist = dist + weight
                new_loc = (new_row, new_col)
                if (new_loc in distances and new_dist < distances[new_loc]) or new_loc not in distances:
                    distances[new_loc] = new_dist
                    heapq.heappush(to_visit, (new_dist, new_loc))
    
    return "You shouldn't be here..."

# Practicing unit testing on given test input and expected results
class Day15Tests(unittest.TestCase):
    def test_chiton_part1(self):
        self.assertEqual(chiton('Advent of Code/test.txt', 1), 40)
    
    def test_chiton_part2(self):
        self.assertEqual(chiton('Advent of Code/test.txt', 5), 315)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(chiton('Advent of Code/test.txt', 1))
    #print(chiton('Advent of Code/2021-Day15.txt'))
    
    # Part 2 solution
    #print(chiton('Advent of Code/test.txt', 5))
    print(chiton('Advent of Code/2021-Day15.txt', 5))
        