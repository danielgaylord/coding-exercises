def syntax_scoring(chunks):
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    matches = {"(": ")", "[": "]", "{": "}", "<": ">"}
    open = "([{<"
    corrupt_score = 0
    incomplete = []
    for chunk in chunks:
        chars = []
        corrupt = False
        for char in chunk:
            if char in open:
                chars.append(char)
            else:
                check = chars.pop()
                if matches[check] != char:
                    corrupt_score += points[char]
                    corrupt = True
        if not corrupt:
            incomplete.append(chars)
    
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    incomp_scores = []
    for remain in incomplete:
        temp_score = 0
        for char in remain[::-1]:
            temp_score *= 5
            temp_score += points[matches[char]]
        incomp_scores.append(temp_score)
    incomp_scores = list(sorted(incomp_scores))

    return incomp_scores[len(incomp_scores) // 2]

if __name__ == "__main__":
    chunks = []
    with open('Advent of Code/2021-Day10.txt', 'r') as input:
        for line in input:
            chunks.append(line.rstrip())
    
    print(syntax_scoring(chunks))
        