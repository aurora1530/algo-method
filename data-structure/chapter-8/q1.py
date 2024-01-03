N = int(input())
P = list(map(int, input().split()))

child = [[] for _ in range(N)]  # child[i]=頂点iを親にもつ頂点のlist
for i in range(0, N-1):  # 0の親は考えない
    child[P[i]].append(str(i+1))

Q = int(input())

for _ in range(Q):
    v = int(input())
    brothers = child[P[v-1]]
    print(' '.join(brothers))
