def contSeq(arr):
    maxVal = 0
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        if total < 0:
            total = 0
        maxVal = max(maxVal, total)
    return maxVal

if __name__ == "__main__":
    seq = [2, -8, 3, -2, 4, -10]
    print(contSeq(seq))