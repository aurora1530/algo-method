N, K = map(int, input().split())
A = list(map(int, input().split()))


min_diff = 2 * 10 ** 9

A.sort()

i = 0
while i+K <= N:
    diff = A[i + K - 1] - A[i]
    min_diff = min(diff, min_diff)
    i += 1

print(min_diff)
