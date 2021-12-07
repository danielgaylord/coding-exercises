def whale_treachery():
    hor_pos = []
    with open('Advent of Code/2021-Day7.txt', 'r') as input:
        hor_pos = [int(age) for age in input.readline().split(",")]

    currMin = float('inf')
    for x in range(min(hor_pos), max(hor_pos) + 1):
        subtotal = 0
        for num in hor_pos:
            pos_diff = abs(num - x)
            
            # Swap comments of below 2 lines to switch between part 1 and 2
            #subtotal += pos_diff
            subtotal += (pos_diff * (pos_diff + 1)) // 2

            # Quick exit if we can already tell we are getting too large
            if subtotal > currMin:
                break
        currMin = min(subtotal, currMin)
    return currMin

if __name__ == "__main__":
    print(whale_treachery())
        