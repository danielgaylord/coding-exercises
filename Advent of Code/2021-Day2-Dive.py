def dive():
    moves = []
    while True:
        line = input()
        if line:
            moves.append(line.split(" "))
        else:
            break
    
    horiz = 0
    depth = 0

    for move in moves:
        if move[0] == "forward":
            horiz += int(move[1])
        elif move[0] == "down":
            depth += int(move[1])
        elif move[0] == "up":
            depth -= int(move[1])

    return horiz*depth

if __name__ == "__main__":
    print(dive())
        