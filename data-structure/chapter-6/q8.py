N, Q = map(int, input().split())

follower_dict = {
    user_y: set()
    for user_y in range(N)
}

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        follower_dict[query[2]].add(query[1])
    elif query[0] == 1:
        follower_dict[query[2]].discard(query[1])
    else:
        ans = 0
        z_follower = follower_dict[query[1]]
        for key, user_follower in follower_dict.items():
            if key == query[1]:
                continue
            if z_follower == user_follower:
                ans += 1
        print(ans)
