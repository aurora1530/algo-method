# vの頂点番号iについて。
# p.left.val = 2 * p.val +1
# p.right.val = p.left.val + 1
# p.val = (p.left.val-1)/2 or (p.right.val-2)/2


H = []
Q = int(input())
for _ in range(Q):
    v = int(input())
    H.append(v)
    v_idx = len(H)-1
    if v_idx == 0:
        continue
    par_idx = (v_idx-1)//2
    while H[v_idx] > H[par_idx]:
        temp_val = H[par_idx]
        H[par_idx] = H[v_idx]
        H[v_idx] = temp_val
        v_idx = par_idx
        par_idx = (v_idx-1)//2
        if par_idx < 0:
            break
print(*H)
