N = int(input())
A = list(map(int, input().split()))

count_A = [0 for i in range(10**5 + 1)]
for a in A:
    count_A[a] += 1
Q = int(input())
for _ in range(Q):
    x = int(input())
    num = count_A[x]
    print(num)
