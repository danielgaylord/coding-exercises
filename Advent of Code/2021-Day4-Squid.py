def mark(board, num):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == num:
                board[row][col] = -1

def check(board):
    tboard = list(map(list, zip(*board)))
    for row in board:
        if all(e == -1 for e in row):
            return True
    for row in tboard:
        if all(e == -1 for e in row):
            return True
    return False

def score(board):
    total = 0
    for row in board:
        for num in row:
            if num != -1:
                total += int(num)
    return total

def squid():
    draws = []
    boards = []
    with open('Advent of Code/2021-Day4-Squid.txt', 'r') as input:
        draws = input.readline().rstrip().split(",")
        while input.readline() == "\n":
            board = []
            for _ in range(5):
                board.append(input.readline().rstrip().split())
            boards.append(board)
    
    win_board = None
    last_num = -1
    for num in draws:
        for board in boards:
            mark(board, num)
        for board in boards:
            if check(board):
                win_board = board
                boards.remove(board)
        if len(boards) == 0:
            last_num = int(num)
            break
    
    return score(board) * last_num


if __name__ == "__main__":
    print(squid())
        