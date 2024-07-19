N, M = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

A.sort()

for x in X:
    print(A[x])
