N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = sum(1 << v for v in V)
print(ans)
