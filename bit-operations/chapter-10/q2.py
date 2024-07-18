N, V = map(int, input().split())
A = list(map(int, input().split()))

# A[0]..A[N-1]を対象にするかどうか i番目が1

flag = False
for x in range(2 ** N):
    s = 0
    for i in range(N):
        if x & (1 << i) != 0:
            s += A[i]
    if V == s:
        flag = True
        break
print('Yes' if flag else 'No')
