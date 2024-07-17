N = int(input())
A = list(map(int,input().split()))


dp = [0] * N
dp[1] = A[1]

for i in range(2,N):
    step1Sec = dp[i-1] + A[i]
    step2Sec = dp[i-2] + 2 * A[i]
    dp[i] = min(step1Sec,step2Sec)

print(dp[N-1])
