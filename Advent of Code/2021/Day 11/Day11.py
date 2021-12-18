from collections import deque

def dumbo_octopus(energy):
    rows = len(energy)
    cols = len(energy[0])
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    flashes = 0
    step = 0
    
    # Swap the comment in the following 2 lines to switch between part 1 and part 2
    #for _ in range(100):
    while True:

        step += 1
        flash = deque()
        flashed = []

        # Step 1: 
        # - Increase all octopus energy levels by 1
        # - If octpous energy becomes greater than 9, set energy to -1 to count 
        #   as 'visited' and flash it
        for row in range(rows):
            for col in range(cols):
                energy[row][col] += 1
                if energy[row][col] > 9:
                    energy[row][col] = -1
                    flash.append((row, col))
        
        # Step 2:
        # - For part 1, capture the number of flashes that occur
        # - Each octopus that flashed increases all adjacent octopus energy levels
        #   - To account for an octopus only flashing once per step, only increase 
        #     energy if it hasn't flashed (not -1)
        # - If adjacent octpous energy becomes greater than 9, set energy to -1 to 
        #   count as 'visited' and flash it
        # - To prepare for next step, keep track of which octopuses flashed this step
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
        
        # Step 3:
        # - Every octopus that flashed this step has energy set to 0
        for row, col in flashed:
            energy[row][col] = 0

        # For part 2: If all octopi flashed, we done 
        if len(flashed) == rows * cols:
            return step

    # For part 1: Return number of flashes after step 100
    return flashes

if __name__ == "__main__":
    energy = []
    with open('Advent of Code/2021-Day11.txt', 'r') as input:
        energy = [[int(char) for char in line.rstrip()] for line in input]
    
    print(dumbo_octopus(energy))
        