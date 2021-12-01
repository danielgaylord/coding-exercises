def sonar_sweep():
    curr = None
    sweeps = []
    increases = 0
    while True:
        line = input()
        if line:
            sweeps.append(int(line))
        else:
            break
    
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
        