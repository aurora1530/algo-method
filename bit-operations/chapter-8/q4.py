X = list(map(int, [*input()]))

P, Q = input().split()
target = X[0] if P == 'o' else X[1] if P == 'g' else X[2]

x = 2 if Q == 'r' else 1 if Q == 'w' else 0

ans = target & 1 << x

print('Yes' if ans != 0 else 'No')
