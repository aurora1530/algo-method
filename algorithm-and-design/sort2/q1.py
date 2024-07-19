import math

N = int(input())
A = list(map(int, input().split()))

A.sort()

mid = A[math.floor(
    (N-1)/2)] if N % 2 == 1 else (A[math.floor(N/2 - 1)] + A[math.floor(N/2)])/2

print(mid)