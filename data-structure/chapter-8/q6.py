from collections import deque

# N = int(input())
# A = [0] + list(map(int, input().split()))
# v = int(input())

# N = 7
# A = [0, 0, 0, 1, 1, 4, 2]
# v = 1

with open('./Q6. 箱の内部の箱の個数 (1)_3_input.txt', 'r') as file:
    data = file.read().split('\n')
    N = int(data[0])
    A = [0] + list(map(int, data[1].split()))
    v = int(data[2])

inner_boxes = [[] for _ in range(N)]
for i in range(N):
    inner_boxes[A[i]].append(i)

ans = 0
if v == 0:
    print(N-1)
else:
    que = deque()
    que.append(v)
    while len(que) != 0:
        outer_num = que.popleft()
        inner = inner_boxes[outer_num]
        ans += len(inner)
        for num in inner:
            que.append(num)

    print(ans)
