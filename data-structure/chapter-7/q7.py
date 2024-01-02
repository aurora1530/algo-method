N = int(input())
S = input()

stack = []

invalid_frag = False
for char in S:
    if char == '(':
        stack.append(1)
    else:
        if len(stack) == 0:
            invalid_frag = True
            break
        stack.pop()

if len(stack) != 0:
    invalid_frag = True

if invalid_frag:
    print('No')
else:
    print('Yes')
