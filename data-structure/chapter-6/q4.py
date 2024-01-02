from collections import defaultdict
N = int(input())

A = input().split()

Q = int(input())

count_dict = defaultdict(int)
for a in A:
    count_dict[a] += 1


for _ in range(Q):
    query, T = input().split()
    if query == '0':
        count_dict[T] += 1
    elif query == '1':
        count_dict[T] = 0
    else:
        print(count_dict[T])
