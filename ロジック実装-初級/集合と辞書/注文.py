N, M = map(int, input().split())

name_to_price = {}

for _ in range(N):
    f, c = input().split()
    name_to_price[f] = int(c)

total = 0
X = input().split()
for x in X:
    total += name_to_price.get(x)

print(total)
