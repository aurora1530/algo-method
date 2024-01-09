Q = int(input())
H = []


def swap(i, j):
    H[i], H[j] = H[j], H[i]


def compare(target_idx: int):
    left_idx = 2 * target_idx + 1
    right_idx = left_idx + 1
    while 1:
        if left_idx >= len(H):
            break
        if right_idx >= len(H):
            if H[target_idx] < H[left_idx]:
                swap(target_idx, left_idx)
            break
        if H[target_idx] >= max(H[left_idx], H[right_idx]):
            break
        elif H[target_idx] < min(H[left_idx], H[right_idx]):
            if H[left_idx] >= H[right_idx]:
                swap(target_idx, left_idx)
                target_idx = left_idx
            else:
                swap(target_idx, right_idx)
                target_idx = right_idx
        elif H[target_idx] < H[left_idx]:
            swap(target_idx, left_idx)
            target_idx = left_idx
        elif H[target_idx] < H[right_idx]:
            swap(target_idx, right_idx)
            target_idx = right_idx
        left_idx = 2 * target_idx + 1
        right_idx = left_idx + 1


for _ in range(Q):
    query = input().split()
    if query[0] == '0':
        v = int(query[1])
        H.append(v)
        v_idx = len(H)-1
        while v_idx > 0:
            par_idx = (v_idx - 1)//2
            if H[v_idx] > H[par_idx]:
                swap(v_idx, par_idx)
                v_idx = par_idx
            else:
                break
    else:
        swap(0, len(H)-1)  # 末尾と入れ替える
        print(H.pop())  # 末尾、つまりrootの値を削除
        compare(0)
