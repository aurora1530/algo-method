# 部下の人数
import sys
sys.setrecursionlimit(10**6)

N, X = map(int, input().split())

P = list(map(int, input().split()))

subordinates = [[] for _ in range(N)]
for i, p in enumerate(P):
    subordinates[p].append(i + 1)


def count_subordinate(x: int) -> int:
    counter = 0
    for buka in subordinates[x]:
        counter += count_subordinate(buka)
    return len(subordinates[x]) + counter


print(count_subordinate(X))
