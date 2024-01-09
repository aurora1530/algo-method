import heapq
from collections import deque

H = []
S = {}
Q = int(input())
for _ in range(Q):
    query = input().split()
    if query[0] == '0':
        t, s = int(query[1]), query[2]
        heapq.heappush(H, t)
        if t not in S:
            S[t] = deque()
        S[t].append(s)
    else:
        t = heapq.heappop(H)
        print(S[t].popleft())
