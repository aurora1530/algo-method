N, X = map(int, input().split())
Q = int(input())

for _ in range(Q):
    query, v = map(int, input().split())
    if query == 0:
        X |= 1 << v
    elif query == 1:
        X &= ~(1 << v)
    else:
        ans = X & (1 << v)
        print('Yes' if ans != 0 else 'No')
