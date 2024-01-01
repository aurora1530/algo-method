# N, K = map(int, input().split())
# S = input()
N, K = 6, 2
S = '.<.><.'
right = [-1 for _ in range(N)]
left = [-1 for _ in range(N)]

for i in range(N):
    if i != N-1:
        right[i] = i+1
    if i != 0:
        left[i] = i-1

direction = 1
now_grid = K

sec = 0

while (1):
    right[left[now_grid]] = right[now_grid]
    left[right[now_grid]] = left[now_grid]

    if S[now_grid] == '>':
        direction = 1
    elif S[now_grid] == '<':
        direction = -1

    if direction == 1:
        next_grid = right[now_grid]
    elif direction == -1:
        next_grid = left[now_grid]

    sec += abs(now_grid - next_grid)
    now_grid = next_grid
    if now_grid == 0 or now_grid == N-1:
        break
print(sec)
