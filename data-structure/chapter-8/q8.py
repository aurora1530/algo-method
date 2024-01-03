# N = int(input())
with open('./Q8. 兄弟は誰だ？ (3)_2_input.txt', 'r') as file:
    data = file.read().split('\n')
    N = int(data[0])
    test_list = data[1:N]
    Q = int(data[N])
    query_list = data[N+1:]

parent = [-1 for _ in range(N)]  # parent[i]:頂点iの親
children = [[] for _ in range(N)]  # children[i]:頂点iの子要素(list)

parent[0] = 0

neighbor = {key: [] for key in range(N)}  # key:val(list) keyとvalが隣接

for i in range(N-1):
    # a, b = map(int, input().split())
    a, b = map(int, test_list[i].split())
    neighbor[a].append(b)
    neighbor[b].append(a)


def rec(parent_num):
    children[parent_num] = [child_num for child_num in neighbor[parent_num]
                            if child_num != parent[parent_num]]
    for child_num in children[parent_num]:
        parent[child_num] = parent_num
        rec(child_num)


rec(0)

for child in children:
    child.sort()
print(N, Q)
# Q = int(input())
ans = []
for i in range(Q):
    # v = int(input())
    v = int(query_list[i])
    ans.append(' '.join(list(map(str, children[parent[v]]))))
    # print(' '.join(list(map(str, children[parent[v]]))))

with open('./output.txt', 'w') as file:
    file.write('\n'.join(ans))
