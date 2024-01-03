from collections import deque

N, L = map(int, input().split())
A = deque(map(int, input().split()))


temp = deque()

ans = 0
while len(A) != 0 or len(temp) != 0:
    target_deque = temp if len(temp) > 0 else A
    head = target_deque.popleft()
    num_seal = head
    ans += num_seal
    now_temp_len = len(temp)
    for _ in range(L-1):
        if len(temp) == 0:
            target_deque = A
        if len(A) == 0:
            break
        next_head = target_deque.popleft() - num_seal
        if next_head > 0:
            temp.append(next_head)

print(ans)
