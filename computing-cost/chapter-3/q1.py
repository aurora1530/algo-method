N = int(input())
A = list(map(int, input().split()))

min = A[0]
max = A[0]
for i in range(1, N):
    min = A[i] if A[i] < min else min
    max = A[i] if A[i] > max else max

print(max-min)
