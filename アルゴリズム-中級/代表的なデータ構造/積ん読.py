from typing import List

Q = int(input())

stack: List[str] = []

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        stack.append(query[1])
    else:
        title = stack.pop()
        print(title)
