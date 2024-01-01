N = int(input())
A = list(map(int, input().split()))

MAX_NUM = 5 * (10 ** 5)
counter = [0 for _ in range(MAX_NUM+1)]
temp = [-1 for _ in range(MAX_NUM+1)]
for a in A:
    counter[a] += 1

Q = int(input())

for _ in range(Q):
    x = int(input())
    if temp[x] == -1:
        count = 0
        for i in range(1, MAX_NUM//x + 1):
            count += counter[i*x]
        temp[x] = count
    print(temp[x])
