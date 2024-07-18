H, W = map(int, input().split())
grid = [0] * H  # grid[i]は、i行目のマスの状態を表す数字Sが入る。Sは、ビット列で、上からi番目の値が1なら黒、0なら白を表す


def click(i, j, target_grid):
    target_list = [j]
    if j > 0:
        target_list.append(j-1)
    if j < W-1:
        target_list.append(j+1)

    reverse_row = sum(1 << x for x in target_list)
    target_grid[i] ^= reverse_row

    reverse_pre = 1 << j
    if i-1 > 0:
        target_grid[i-1] ^= reverse_pre
    if i+1 < H:
        target_grid[i+1] ^= reverse_pre
    return target_grid


def ok(target_grid):
    for row in target_grid:
        if row != 0:
            return False
    return True


for i in range(W):
    text = input()
    for j in range(W):
        grid[i] += 1 << j if text[W-j-1] == '#' else 0

flag = False
for i in range(H):
    for j in range(W):
        target_grid = click(i, j, grid.copy())
        if ok(target_grid):
            flag = True

print('Yes' if flag else 'No')
