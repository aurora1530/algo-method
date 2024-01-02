N = int(input())
S = input()

open_parentheses = []
open_indexes = {}
close_indexes = {}

for i in range(N):
    char = S[i]
    if char == '(':
        open_parentheses.append(i)
    else:
        index = open_parentheses.pop()
        open_indexes[i] = index
        close_indexes[index] = i

Q = int(input())
for _ in range(Q):
    k = int(input())
    char = S[k]
    if char == '(':
        print(close_indexes[k])
    else:
        print(open_indexes[k])
