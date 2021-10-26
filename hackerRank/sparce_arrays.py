def matchingStrings(strings, queries):
    # Write your code here
    results = []
    counts = {}
    for string in strings:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1
    for query in queries:
        if query in counts:
            results.append(counts[query])
        else:
            results.append(0)
    return results