N,M = map(int,input().split())
A = list(map(int,input().split()))

def main():
    dp = [0] * N

    for i in range(1,N):
        dp[i] = dp[i-1] + A[i]
        for j in range(2,M+1):
            if i-j < 0:
                break
            dp[i] = min(dp[i],dp[i-j] + j * A[i])

    return dp[N-1]

print(main())