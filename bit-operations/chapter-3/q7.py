N, S = map(int, input().split())
Q = int(input())

for _ in range(Q):
    query, y = map(int, input().split())
    if query == 0:
        S |= 1 << y
    else:
        an = S & (1 << y)
        print('off' if an == 0 else 'on')
