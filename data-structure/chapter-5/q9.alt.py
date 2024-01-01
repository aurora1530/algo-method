N, M = map(int, input().split())

A = list(map(int, input().split()))
max_A = 10**3
sum_square_exists = [0 for _ in range(2 * (max_A ** 2) + 1)]

for a in A:
    for b in A:
        sum_square_exists[a**2 + b**2] = 1

frag = False
for ab in range(2 * (max_A ** 2)+1):
    if M-ab > 2 * (max_A ** 2):
        continue
    if sum_square_exists[M-ab] == 1 and sum_square_exists[ab] == 1:
        print('Yes')
        frag = True
        break

if not frag:
    print('No')
