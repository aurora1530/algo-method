N, Q = map(int, input().split())

A = [-1] * N
head = tail = 0

for _ in range(Q):
    query = input().split()
    if query[0] == '0':
        v = int(query[1])
        A[tail] = v
        tail += 1
        if tail == N:
            tail = 0
    else:
        A[head] = -1
        head += 1
        if head == N:
            head = 0

for a in A:
    print(a)
