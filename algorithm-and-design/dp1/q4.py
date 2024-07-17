N = int(input())


def main():
    if(N == 1):
        return 1
    if(N == 2):
        return 2
    dp = [0] * (N+1) # [n]: 足してnになる組み合わせの個数
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3,N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[N]

print(main())