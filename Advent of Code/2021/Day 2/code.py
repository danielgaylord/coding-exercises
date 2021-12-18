import unittest

# Read puzzle input and return as usable data structure
def parse_input(file):
    moves = []
    with open(file, 'r') as input:
        moves = [line.rstrip().split(" ") for line in input]
    return moves

def dive(file, part):
    moves = parse_input(file)
    
    horiz = 0
    depth = 0
    new_depth = 0
    aim = 0

    for move in moves:
        if move[0] == "forward":
            horiz += int(move[1])
            new_depth += aim * int(move[1])
        elif move[0] == "down":
            depth += int(move[1])
            aim += int(move[1])
        elif move[0] == "up":
            depth -= int(move[1])
            aim -= int(move[1])

    if part == 1:
        return horiz * depth
    if part == 2:
        return horiz * new_depth

# Unit testing on given test input and expected results
class Day2Tests(unittest.TestCase):
    def test_packet_decoder_part1(self):
        self.assertEqual(dive('Advent of Code/2021/Day 2/example.txt', 1), 150)
    
    def test_packet_decoder_part2(self):
        self.assertEqual(dive('Advent of Code/2021/Day 2/example.txt', 2), 900)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(dive('Advent of Code/2021/Day 2/example.txt', 1))
    print(dive('Advent of Code/2021/Day 2/input.txt', 1))
    
    # Part 2 solution
    #print(dive('Advent of Code/2021/Day 2/example.txt', 2))
    print(dive('Advent of Code/2021/Day 2/input.txt', 2))