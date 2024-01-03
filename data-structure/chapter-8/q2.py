N = int(input())

parent = [0 for _ in range(N)]  # parent[i] iの親の頂点番号
children = [[] for _ in range(N)]  # chidren[i] 頂点iを親に持つ頂点番号のリスト

for _ in range(N-1):
    a, b = map(int, input().split())
    children[a].append(b)
    parent[b] = a

for row in children:
    row.sort()

Q = int(input())
for _ in range(Q):
    v = int(input())
    print(' '.join(list(map(str, children[parent[v]]))))
