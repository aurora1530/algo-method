N, M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

max_v = 0
for x in range(2 ** N):
    sum_w = sum(w for idx, w in enumerate(W) if x & 1 << idx != 0)
    if sum_w > M:
        continue
    sum_v = sum(v for idx, v in enumerate(V) if x & 1 << idx != 0)
    if max_v < sum_v:
        max_v = sum_v
print(max_v)
