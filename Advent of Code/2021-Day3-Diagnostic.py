def diagnose():
    report = []
    with open('Advent of Code/2021-Day3-Diagnostic.txt', 'r') as input:
        report = [line.rstrip() for line in input]
    
    report_size, diag_size = len(report), len(report[0])
    gamma, epsil = '', ''
    result = list(map(list, zip(*report)))

    for l in result:
        total = sum(map(int, l))
        gamma += "1" if total >= report_size / 2 else "0"
        epsil += "0" if total >= report_size / 2 else "1"

    oxygen = result[0]
    co2 = result[0]
    for row in range(len(result)):
        total = sum(map(int, oxygen[row]))
        if total >= report_size / 2:
            oxygen = [-1 for ]

    return int(int(gamma, 2)) * int(int(epsil, 2))

if __name__ == "__main__":
    print(diagnose())
        