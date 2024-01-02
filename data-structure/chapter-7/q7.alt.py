N = int(input())
S = input()

siz = 0
invalid_frag = False
for char in S:
    siz += 1 if char == '(' else -1
    if siz < 0:
        invalid_frag = True
        break

if siz != 0:
    invalid_frag = True

print('No' if invalid_frag else 'Yes')
