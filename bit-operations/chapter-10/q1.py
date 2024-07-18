N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    flag = X & (1 << i)
    if flag != 0:
        ans.append(A[i])
print(sum(ans))
