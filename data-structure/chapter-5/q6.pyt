N = int(input())
A = list(map(int, input().split()))


length = 10**5 + 1
counter = [0]*(length)

for a in A:
    counter[a] += 1

bottom = N*(N-1)
top = 0
for i in range(length):
    count = counter[i]
    if count < 2:
        continue
    top += count*(count-1)

print(top/bottom)
