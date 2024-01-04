N, M = map(int, input().split())
ans = 0
for x in range(1, N+1):
    for y in range(1, N+1):
        z_max = M-(x+y)
        if 1 <= z_max:
            ans += z_max if z_max <= N else N
print(ans)
