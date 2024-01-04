N = int(input())
d = list(map(int, input().split()))  # d[i]:iからi+1までの距離

list_d = [0] * N  # 駅0から駅iまでの距離 (list_d[0]=0としておく)

for i in range(1, N):
    list_d[i] = list_d[i-1] + d[i-1]

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    ans = list_d[r]-list_d[l]
    print(ans)
