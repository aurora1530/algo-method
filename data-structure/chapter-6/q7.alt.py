N = int(input())
A = list(map(int, input().split()))

counter = {}
for a in A:
    counter[a] = counter.get(a, 0) + 1

ans = 0
for key, val in counter.items():
    if val > 1:
        ans += (val-1)
print(ans)
