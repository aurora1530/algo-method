N, X = map(int, input().split())

ans = 0
for i in range(N):
    tmp = X & (1 << i)
    if tmp != 0:
        ans += 1
print(ans)
