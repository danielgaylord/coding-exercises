def symmetric_diff():
    sizeA = int(input())
    setA = set(map(int, input().split()))
    sizeB = int(input())
    setB = set(map(int, input().split()))
    symdiffA = setA.difference(setB)
    symdiffB = setB.difference(setA)
    result = sorted(list(symdiffA.union(symdiffB)))
    for num in result:
        print(num)