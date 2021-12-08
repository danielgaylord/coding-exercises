def seven_segment_search(patterns):
    digit_count = [0 for _ in range(10)]
    output_sum = 0
    for pattern in patterns:
        digit_rep = ["" for _ in range(10)]
        digit_rep[1] = "".join(sorted(pattern[0][0]))
        digit_rep[4] = "".join(sorted(pattern[0][2]))
        digit_rep[7] = "".join(sorted(pattern[0][1]))
        digit_rep[8] = "".join(sorted(pattern[0][-1]))
        for i in range(3, 9):
            minus1, minus4, minus7, minus8 = pattern[0][i], pattern[0][i], pattern[0][i], digit_rep[8]
            for char in digit_rep[1]:
                minus1 = minus1.replace(char, "")
            for char in digit_rep[4]:
                minus4 = minus4.replace(char, "")
            for char in digit_rep[7]:
                minus7 = minus7.replace(char, "")
            for char in pattern[0][i]:
                minus8 = minus8.replace(char, "")
            if len(minus1) == 4 and len(minus4) == 3 and len(minus7) == 3 and len(minus8) == 1:
                digit_rep[0] = "".join(sorted(pattern[0][i]))
            elif len(minus1) == 4 and len(minus4) == 3 and len(minus7) == 3 and len(minus8) == 2:
                digit_rep[2] = "".join(sorted(pattern[0][i]))
            elif len(minus1) == 3 and len(minus4) == 2 and len(minus7) == 2 and len(minus8) == 2:
                digit_rep[3] = "".join(sorted(pattern[0][i]))
            elif len(minus1) == 4 and len(minus4) == 2 and len(minus7) == 3 and len(minus8) == 2:
                digit_rep[5] = "".join(sorted(pattern[0][i]))
            elif len(minus1) == 5 and len(minus4) == 3 and len(minus7) == 4 and len(minus8) == 1:
                digit_rep[6] = "".join(sorted(pattern[0][i]))
            elif len(minus1) == 4 and len(minus4) == 2 and len(minus7) == 3 and len(minus8) == 1:
                digit_rep[9] = "".join(sorted(pattern[0][i]))
        output = 0
        for digit in pattern[1]:
            output *= 10
            output += digit_rep.index("".join(sorted(digit)))
                
        output_sum += output

    return output_sum

if __name__ == "__main__":
    patterns = []
    with open('Advent of Code/2021-Day8.txt', 'r') as input:
        temp = [line.rstrip().split(" | ") for line in input]
        for line in temp:
            hold = []
            hold.append(line[0].split(" "))
            hold.append(line[1].split(" "))
            hold[0] = list(sorted(hold[0], key=len))
            patterns.append(hold)

    check = "abc"
    digit = "ac"
    for char in digit:
        check = check.replace(char, "")
    
    print(seven_segment_search(patterns))
        