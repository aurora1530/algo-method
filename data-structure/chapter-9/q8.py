H = int(input())
Q = int(input())

min_num = 2 ** (H) - 1
max_v_num = 2 ** (H+1) - 1 - 1  # 番号はインデックス表記なのでさらに-1している


def get_par_num(v: int):
    if v == 0:
        return -1
    if v % 2 == 0:
        return (v-2) // 2
    return (v-1)//2


# ある頂点vについて
# v.left = v * 2 + 1
# v.right = v.left + 1
for _ in range(Q):
    t, v = map(int, input().split())
    ans = -1
    if t == 0:
        ans = get_par_num(v)
    if t == 1:
        if min_num <= v <= max_v_num:
            ans = -1
        else:
            ans = v * 2 + 1
    if t == 2:
        if min_num <= v <= max_v_num:
            ans = -1
        else:
            ans = v * 2 + 2
    print(ans)
