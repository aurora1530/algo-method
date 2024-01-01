N = int(input())
A = list(map(int, input().split()))

counter = [0]*(10**5 + 1)
for a in A:
    counter[a] += 1
sum_all = sum(A)

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        counter[query[1]] += 1
        sum_all += query[1]
    elif query[0] == 1:
        x, y = query[1:]
        count_x = counter[x]
        count_y = counter[y]
        counter[x] = 0
        counter[y] += count_x
        sum_all -= x * count_x
        sum_all += y * count_x
    else:
        print(sum_all)
