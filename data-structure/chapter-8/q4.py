N = int(input())
P = [0] + list(map(int, input().split()))

children = [[] for _ in range(N)]

for i in range(1, N):
    children[P[i]].append(i)

for c in children:
    c.sort()

ans = []


def rec(v: int):
    ans.append(str(v))
    for v2 in children[v]:
        rec(v2)


rec(0)

print(' '.join(ans))
