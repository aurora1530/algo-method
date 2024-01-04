N = int(input())
A = list(map(int, input().split()))


sum_A = [A[0]] + [0] * (N-1)  # sum_A[i]:A[0] ~ A[i]までの総和
for i in range(1, N):
    sum_A[i] = sum_A[i-1] + A[i]

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    before = sum_A[l-1] if l-1 >= 0 else 0
    ans = sum_A[r-1] - before
    print(ans)
