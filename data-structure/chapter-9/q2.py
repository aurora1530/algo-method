tree = {}  # key:[l,r] 頂点iの左側小頂点l,右側小頂点r

stdi = [5, 2, 3, 7, 9, 4, 1, 6, 8]
root = -1
for v in stdi:
    if len(tree) == 0:
        tree[v] = [-1, -1]
        root = v
        continue

    target_v = root
    while True:
        if v < target_v:
            if tree[target_v][0] == -1:
                tree[target_v][0] = v
                break
            else:
                target_v = tree[target_v][0]
                continue
        elif v > target_v:
            if tree[target_v][1] == -1:
                tree[target_v][1] = v
                break
            else:
                target_v = tree[target_v][1]
                continue
    tree[v] = [-1, -1]

ans = []


def rec(v):
    ans.append(v)
    if tree[v][0] != -1:
        rec(tree[v][0])
    if tree[v][1] != -1:
        rec(tree[v][1])


rec(root)
print(*ans)
