N = int(input())
A = list(map(int, input().split()))

set_A = set(A)

flag = True
for n in range(1, N+1):
    if n not in set_A:
        flag = False
        break

print('Yes' if flag else 'No')
