N = int(input())

parent = [-1 for _ in range(N)]  # parent[i]:頂点iの親
children = [[] for _ in range(N)]  # children[i]:頂点iの子要素(list)

parent[0] = 0

neighbor = {key: [] for key in range(N)}  # key:val(list) keyとvalが隣接

for i in range(N-1):
    a, b = map(int, input().split())
    neighbor[a].append(b)
    neighbor[b].append(a)


def rec(parent_num):
    children[parent_num] = [child_num for child_num in neighbor[parent_num]
                            if child_num != parent[parent_num]]
    for child_num in children[parent_num]:
        parent[child_num] = parent_num
        rec(child_num)


rec(0)

for child in children:
    child.sort()

Q = int(input())
ans = []
for i in range(Q):
    v = int(input())
    print(' '.join(list(map(str, children[parent[v]]))))
