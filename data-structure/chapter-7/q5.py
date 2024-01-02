N = int(input())

S = input()

open_parentheses = []


ans = 0
for i in range(N):
    p = S[i]
    if p == '(':
        open_parentheses.append(1)
    else:
        if len(open_parentheses) == 1:
            ans = i
            break
        else:
            open_parentheses.pop(-1)
print(ans)
