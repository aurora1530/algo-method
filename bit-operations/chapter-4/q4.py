N, S = map(int, input().split())
Q = int(input())

for _ in range(Q):
    query, x = map(int, input().split())
    if query == 0:
        S ^= 1 << x
    else:
        ans = S & (1 << x)
        print('off' if ans == 0 else 'on')
