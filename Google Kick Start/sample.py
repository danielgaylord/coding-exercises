cases = int(input())

for case in range(1, cases + 1):
    bags, kids = map(int, input().split())
    candy = sum(list(map(int, input().split())))
    remainder = candy % kids
    print(f"Case #{case}: {remainder}")