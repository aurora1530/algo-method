from collections import deque
H, W = map(int, input().split())

grid = []
for i in range(H):
    row = input()
    if row.find('S') != -1:
        START_INDEX = [i, row.find('S')]
    if row.find('G') != -1:
        GOAL_INDEX = [i, row.find('G')]
    grid.append(list(row))

que = deque()

dist = [[-1 for _ in range(W)] for _ in range(H)]
dist[START_INDEX[0]][START_INDEX[1]] = 0
que.append([START_INDEX[0], START_INDEX[1]])

DIRECTION = [[0, 1], [0, -1], [1, 0], [-1, 0]]

while len(que) != 0 and dist[GOAL_INDEX[0]][GOAL_INDEX[1]] == -1:
    x, y = que.popleft()
    for dx, dy in DIRECTION:
        if x + dx < 0 or x + dx >= H or y+dy < 0 or y + dy >= W:
            continue
        if grid[x+dx][y+dy] == '#':
            continue
        if dist[x+dx][y+dy] != -1:  # 探索済み
            continue
        dist[x+dx][y+dy] = dist[x][y] + 1
        que.append([x+dx, y+dy])
print(dist[GOAL_INDEX[0]][GOAL_INDEX[1]])
