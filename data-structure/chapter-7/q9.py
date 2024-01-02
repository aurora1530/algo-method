from collections import deque

Q = int(input())


todo = deque()

for _ in range(Q):
    query = input().split()
    if query[0] == '0':
        todo.append(query[1])
    else:
        print(todo.popleft())
