from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))


counter = defaultdict(int)

for a in A:
    for b in A:
        v = a**2 + b ** 2
        counter[v] = 1
print(counter)
frag = False
for v in counter.values():

    if M - v in counter:
        print('Yes')
        frag = True
        break

if not frag:
    print('No')
