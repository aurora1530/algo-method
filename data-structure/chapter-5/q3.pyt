N = int(input())
A = list(map(int, input().split()))

counter = [0]*(10**5+1)

for a in A:
    counter[a] += 1

Q = int(input())

for _ in range(Q):
    query, v = map(int, input().split())
    if query == 0:
        counter[v] += 1
    elif query == 1:
        counter[v] = 0
    else:
        print(counter[v])
