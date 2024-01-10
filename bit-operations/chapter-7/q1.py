A, M = map(int, input().split())
for i in range(30):
    frag = M & (1 << i)
    if frag != 0:
        A |= 1 << i

print(A)
