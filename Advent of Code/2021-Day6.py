def calc_fish(age, days_rem, spawn_check):
    spawn = days_rem - age
    family = 0
    while spawn >= 1:
        if spawn_check[spawn]:
            family += spawn_check[spawn]
        else:
            spawn_check[spawn] = 1 + calc_fish(8, spawn - 1, spawn_check)
            family += spawn_check[spawn]
        spawn -= 7
    return family


def laternfish():
    ages = []
    with open('Advent of Code/2021-Day6.txt', 'r') as input:
        ages = [int(age) for age in input.readline().split(",")]
    
    spawn_check = [None for _ in range(300)]
    total = 0
    for age in ages:
        total += 1 + calc_fish(age, 256, spawn_check)
    return total

    # for _ in range(256):
    #     new_ages = []
    #     for i in range(len(ages)):
    #         if ages[i] == 0:
    #             ages[i] = 7
    #             new_ages.append(8)
    #         ages[i] -= 1
    #     ages += new_ages

    # return len(ages)

if __name__ == "__main__":
    print(laternfish())
        