N,X,Y = map(int,input().split())

dp = [0 for _ in range(N)]
dp[0] = X
dp[1] = Y
for i in range(2,N):
    dp[i] = (dp[i-1] + dp[i-2]) % 100


print(dp[N-1])