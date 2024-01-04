N = int(input())
tree = []
for _ in range(N):
    tree.append(list(map(int, input().split())))

ans = []


def rec(v: int):
    if tree[v][0] != -1:
        rec(tree[v][0])
    ans.append(v)
    if tree[v][1] != -1:
        rec(tree[v][1])


rec(0)
print(*ans)
