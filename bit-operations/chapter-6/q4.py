N = int(input())
F = list(map(int, input().split()))

ans = 0
for f in F:
    ans |= 1 << f

print(ans)
