def diagonalDifference(arr):
    slash, backslash = 0, 0
    for row in range(len(arr)):
        slash += arr[row][len(arr) - row - 1]
        backslash += arr[row][row]
    return abs(backslash - slash)

if __name__ == "__main__":
    print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))