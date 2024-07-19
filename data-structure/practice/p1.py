H, W = map(int, input().split())

bombs = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    S = input()
    for j in range(W):
        is_bomb = S[j] == '#'
        if not is_bomb:
            continue
        if i + 1 < H:
            bombs[i+1][j] += 1
        if j + 1 < W:
            bombs[i][j+1] += 1
        if i != 0:
            bombs[i - 1][j] += 1
        if j != 0:
            bombs[i][j-1] += 1

Q = int(input())

for _ in range(Q):
    x, y = map(int, input().split())
    print(bombs[x][y])
