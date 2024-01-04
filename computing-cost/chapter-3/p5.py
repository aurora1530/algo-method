N = int(input())
A = list(map(int, input().split()))

S = [sum(A)] + [0] * (N-1)  # S[i]:sum(S[i:N])
for i in range(1, N):
    S[i] = S[i-1] - A[i-1]

ans = 0
for i in range(N-1):
    ans += A[i] * S[i+1]
print(ans)
