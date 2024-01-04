N = int(input())
A = list(map(int, input().split()))


sum_A = sum(A)


ans = 0
for i in range(N):
    ans += A[i] * sum_A

print(ans)
