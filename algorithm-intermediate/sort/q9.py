# ごはんを買う

N, K = map(int, input().split())
gohan = [list(map(int, input().split())) for _ in range(N)]

gohan.sort(key=lambda x: x[0])

total = 0
counter = 0
i = 0
while counter <= K and i < N:
    if counter + gohan[i][1] <= K:
        counter += gohan[i][1]
        total += gohan[i][0] * gohan[i][1]
    else:
        total += gohan[i][0] * (K - counter)
        counter = K
    i += 1

print(total)
