N, X = map(int, input().split())

ans = N & (~(1 << X))

print('No' if ans == 0 else 'Yes')
