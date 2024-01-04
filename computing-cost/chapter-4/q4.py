N, D = map(int, input().split())
X = list(map(int, input().split()))

sum_X = [0]*(N+1)  # [i]:初日からi-1日目までの合計値

for idx, x in enumerate(X):
    sum_X[idx+1] = sum_X[idx] + x

max_d = 0
ans_idx = -1
for i in range(N-D+1):
    # 日iからd日間の人数
    amount = sum_X[i+D]-sum_X[i]
    if amount >= max_d:
        max_d = amount
        ans_idx = i

print(f"{ans_idx}~{ans_idx+D-1}")
