N = int(input())
A = list(map(int, input().split()))
ans = sum(A) - min(A)

print(ans)
