Q = int(input())

counter = [0] * (2 * 10**4 + 1)
min = -10**2
max = 10**2
for x in range(min, max+1):
    for y in range(min, max+1):
        counter[x**2 + y ** 2] += 1

for _ in range(Q):
    P = int(input())
    print(counter[P])
