# フォロー
N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

for g in G:
    g.sort()
    output = ' '.join(map(str, g)) if len(g) > 0 else ''
    print(output)
