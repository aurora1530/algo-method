from collections import deque
X = int(input())
Q = int(input())

current_time = 0
tasks = deque()  # 完了時刻が入る

done = 0
for _ in range(Q):
    query, t = map(int, input().split())
    if query == 0:
        tasks.append(t + X)
    else:
        if len(tasks) != 0:
            while (tasks[0] <= t):
                done += 1
                tasks.popleft()
                if len(tasks) == 0:
                    break
        print(done)
