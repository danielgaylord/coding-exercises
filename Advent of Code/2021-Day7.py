def whale_treachery():
    hor_pos = []
    with open('Advent of Code/2021-Day7.txt', 'r') as input:
        hor_pos = [int(age) for age in input.readline().split(",")]
    
    def check_fuel(x):
        cost = (x * (x + 1)) // 2
        return cost

    currMin = float('inf')
    for x in range(max(hor_pos)):
        subtotal = 0
        for num in hor_pos:
            subtotal += check_fuel(abs(num - x))
        currMin = min(subtotal, currMin)

    return currMin

if __name__ == "__main__":
    print(whale_treachery())
        