N = int(input())
L = list(map(int, input().split()))

max_length = 10**5
count_len = [0] * (max_length+1)  # [i]:長さiの本数
for length in L:
    count_len[length] += 1

count_under = [0] * (max_length+1)  # 長さi以下の本数
for i in range(1, max_length+1):
    count_under[i] = count_under[i-1] + count_len[i]


Q = int(input())

for _ in range(Q):
    A, B = map(int, input().split())
    ans = count_under[B]-count_under[A-1]
    print(ans)
