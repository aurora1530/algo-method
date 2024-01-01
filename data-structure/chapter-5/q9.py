N, M = map(int, input().split())

A = list(map(int, input().split()))

frag = False
for a in A:
    if frag:
        break
    a2 = a**2
    if M-3 < a2:
        continue
    for b in A:
        if frag:
            break
        b2 = b**2
        if M-2 < a2 + b2:
            continue
        for c in A:
            if frag:
                break
            c2 = c**2
            if M-1 < a2+b2+c2:
                continue
            for d in A:
                if M == a2 + b2 + c2 + d**2:
                    print('Yes')
                    frag = True
                    break
if not frag:
    print('No')
