def add_to_dict(element, dictionary, amount):
    if element in dictionary:
        dictionary[element] += amount
    else:
        dictionary[element] = amount

def extended_polymerization(template, pairs):
    ele_counts = {}
    pair_counts = {}
    add_to_dict(template[0], ele_counts, 1)
    for i in range(1, len(template)):
        add_to_dict(template[i], ele_counts, 1)
        add_to_dict(template[i - 1:i + 1], pair_counts, 1)
    print(ele_counts)
    print(pair_counts)

    for _ in range(40):
        temp = pair_counts.copy()
        for pair in pair_counts:
            if pair in pairs:
                amt_pair = pair_counts[pair]
                pair_add = pairs[pair]
                add_to_dict(pair_add, ele_counts, amt_pair)
                new_left = pair[0] + pair_add
                new_right = pair_add + pair[1]
                add_to_dict(new_left, temp, amt_pair)
                add_to_dict(new_right, temp, amt_pair)
                add_to_dict(pair, temp, -amt_pair)
        pair_counts = temp
    
    max_ele = max(ele_counts.values())
    min_ele = min(ele_counts.values())
    return max_ele - min_ele

if __name__ == "__main__":
    template = ""
    pairs = {}
    with open('Advent of Code/2021-Day14.txt', 'r') as input:
        template = input.readline().rstrip()
        input.readline()
        for line in input:
            temp = line.rstrip().split(" -> ")
            pairs[temp[0]] = temp[1]        
    
    print(extended_polymerization(template, pairs))
        