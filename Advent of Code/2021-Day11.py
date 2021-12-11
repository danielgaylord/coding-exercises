from collections import deque

def dumbo_octopus(energy):
    rows = len(energy)
    cols = len(energy[0])
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    flashes = 0
    flash = deque()
    step = 0
    while True:
        step += 1
        flashed = []
        for row in range(rows):
            for col in range(cols):
                energy[row][col] += 1
                if energy[row][col] > 9:
                    energy[row][col] = -1
                    flash.append((row, col))
        while flash:
            row, col = flash.popleft()
            flashes += 1
            for rc, cc in dirs:
                new_row = row + rc
                new_col = col + cc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if energy[new_row][new_col] >= 0:
                        energy[new_row][new_col] += 1
                        if energy[new_row][new_col] > 9:
                            energy[new_row][new_col] = -1
                            flash.append((new_row, new_col))
            flashed.append((row, col))
        for row, col in flashed:
            energy[row][col] = 0
        print(energy)
        if len(flashed) == 100:
            return step

    return flashes

if __name__ == "__main__":
    energy = []
    with open('Advent of Code/2021-Day11.txt', 'r') as input:
        energy = [[int(char) for char in line.rstrip()] for line in input]
    
    print(dumbo_octopus(energy))
        