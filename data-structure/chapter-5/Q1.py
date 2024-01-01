import collections
N = int(input())

A = list(map(int, input().split()))
# count_A = {num: A.count(num) for num in A}
count_A = collections.Counter(A)

Q = int(input())

for i in range(Q):
    x = int(input())
    num = count_A.get(x, 0)
    print(num)
