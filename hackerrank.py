from itertools import product

K, mod = [int(n) for n in input().split()]
all_narrs = []

for lists in range(K):
    all_narrs.append(list(map(lambda n: int(n) ** 2, input().split()[1:])))

S = 0
for cart in product(*all_narrs):
    print(cart)
    if (sum(cart) % mod) > S:
        S = sum(cart)

print(S)
