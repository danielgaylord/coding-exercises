import unittest

# Read puzzle input and return as usable data structure
def parse_input(file):
    grid = []
    with open(file, 'r') as input:
        for line in input:
            row = [ch for ch in line.rstrip()]
            grid.append(row)
    return grid

def chiton(file):
    grid = parse_input(file)
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)
    return grid

# Practicing unit testing on given test input and expected results
class Day15Tests(unittest.TestCase):
    def test_extended_polymerization_part1(self):
        self.assertEqual(chiton('Advent of Code/test.txt', 10), 40)
    
    def test_extended_polymerization_part2(self):
        self.assertEqual(chiton('Advent of Code/test.txt', 40), 2188189693529)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    print(chiton('Advent of Code/test.txt'))
    #print(chiton('Advent of Code/2021-Day15.txt'))
    
    # Part 2 solution
    #print(chiton('Advent of Code/2021-Day15.txt'))
        