import unittest

def sonar_sweep():
    curr = None
    sweeps = []
    increases = 0
    new_increases = 0
    with open('Advent of Code/2021-Day1.txt', 'r') as input:
        sweeps = [int(line.rstrip()) for line in input]
    
    sum = sweeps[0] + sweeps[1]
    for i in range(len(sweeps) - 2):
        sum += sweeps[i + 2]
        if curr != None and sum > curr:
            increases += 1
        curr = sum
        sum -= sweeps[i]

    return increases

if __name__ == "__main__":
    print(sonar_sweep())
        