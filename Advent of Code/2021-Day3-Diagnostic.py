def diagnose():
    report = []
    with open('Advent of Code/2021-Day3-Diagnostic.txt', 'r') as input:
        report = [line.rstrip() for line in input]
    
    report_size, diag_size = len(report), len(report[0])
    gamma, epsil = '', ''
    result = list(map(list, zip(*report)))
    oxygen = [1 for _ in range(report_size)]
    co2 = [1 for _ in range(report_size)]

    for l in result:
        total = sum(map(int, l))
        gamma += "1" if total >= report_size / 2 else "0"
        epsil += "0" if total >= report_size / 2 else "1"

        o_size = sum(oxygen)
        if o_size > 1:
            o_total = sum([int(r) * e for r, e in zip(l, oxygen)])
            if o_total >= o_size / 2:
                check = "1"
            else:
                check = "0"
            for i in range(report_size):
                oxygen[i] = 1 * oxygen[i] if l[i] == check else 0 

        c_size = sum(co2)
        if c_size > 1:
            c_total = sum([int(r) * e for r, e in zip(l, co2)])
            if c_total >= c_size / 2:
                check = "0"
            else:
                check = "1"
            for i in range(report_size):
                co2[i] = 1 * co2[i] if l[i] == check else 0

    gamma = int(int(gamma, 2))
    epsil = int(int(epsil, 2))
    first_reading = gamma * epsil

    oxygen = int(int(report[oxygen.index(1)], 2))
    co2 = int(int(report[co2.index(1)], 2))
    second_reading = oxygen * co2

    return second_reading

if __name__ == "__main__":
    print(diagnose())
        