N = int(input())
A = list(map(int, input().split()))

counter = 0
for i in range(1, N-1):
    a, b, c = A[i-1], A[i], A[i+1]
    if a <= b and b >= c:
        counter += 1

print(counter)
