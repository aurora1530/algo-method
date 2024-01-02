from collections import defaultdict

N = int(input())
S = input().split()

counter = defaultdict(int)
for word in S:
    counter[''.join(sorted(word))] += 1

bottom = N*(N-1)
top = 0
for num in counter.values():
    top += num*(num-1)
print(top/bottom)
