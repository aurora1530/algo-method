from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))

num = [0 for _ in range(N)]
total = 0
que = deque()

for i in range(N):
    num[i] = max(A[i] - total, 0)
    que.append(num[i])
    total += num[i]

    if len(que) == L:
        total -= que.popleft()

ans = 0
for i in range(N):
    ans += num[i]
print(ans)
