N = int(input())
A = list(map(int, input().split()))

MAX_NUM = 5 * (10 ** 5)
counter = [-1 for _ in range(MAX_NUM)]

# for a in A:
#     for d in range(1, a + 1):
#         if a % d == 0:
#             counter[d] += 1

Q = int(input())

for _ in range(Q):
    x = int(input())
    if counter[x] == -1:
        counter[x] = 0
        for a in A:
            if a % x == 0:
                counter[x] += 1

    print(counter[x])
