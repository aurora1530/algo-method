N = int(input())
A = [0] + list(map(int, input().split()))
children = [[] for _ in range(N)]

for i in range(1, N):
    children[A[i]].append(i)

for c in children:
    c.sort()

ans = []


def rec(v):
    for v2 in children[v]:
        rec(v2)
    ans.append(str(v))


rec(0)
print(' '.join(ans))
