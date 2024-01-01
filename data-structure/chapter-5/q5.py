N, Q = map(int, input().split())

counter = [0]*5000  # counter[i]= user i のfollower数
# [i][j] == user i が user j をfollowしたら1
is_follow_list = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        counter[query[2]] += 1 - is_follow_list[query[1]][query[2]]
        is_follow_list[query[1]][query[2]] = 1
    elif query[0] == 1:
        counter[query[2]] -= is_follow_list[query[1]][query[2]]
        is_follow_list[query[1]][query[2]] = 0
    else:
        print(counter[query[1]])
