N,M = map(int,input().split())
D = list(map(int,input().split()))

def main():
    dp = [False] * (N+1) # [n]: nマス目に到達する可能性があるかどうか、bool
    dp[0] = True
    for i in range(1,N+1):
        for d in D:
            targetIdx = i-d
            if targetIdx < 0:
                continue
            canReach = dp[targetIdx]
            if canReach:
                dp[i] = True
                break
    return dp[N]

print('Yes' if main() else 'No')