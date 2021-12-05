def dive():
    moves = []
    with open('Advent of Code/2021-Day2.txt', 'r') as input:
        moves = [line.rstrip().split(" ") for line in input]
    
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

    first_reading = horiz * depth
    second_reading = horiz * new_depth
    return second_reading

if __name__ == "__main__":
    print(dive())
        