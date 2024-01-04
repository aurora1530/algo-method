N = int(input())
A = list(map(int, input().split()))

sum_A = [A[0]] + [0] * (N-1)  # sum_A[i]:sum(A[:i+1])
for i in range(N):
    sum_A[i] = sum_A[i-1] + A[i]

Q = int(input())

for _ in range(Q):
    k = int(input())
    ans = sum_A[k-1] if k > 0 else 0
    print(ans)
