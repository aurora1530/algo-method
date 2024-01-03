N = int(input())
P = [0] + list(map(int, input().split()))

children = [[] for _ in range(N)]

for i in range(N):
    children[P[i]].append(i)

ans = 0
for c in children:
    if len(c) == 0:
        ans += 1
print(ans)
