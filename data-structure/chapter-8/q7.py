N = int(input())
A = [0] + list(map(int, input().split()))


inner_boxes = [[] for _ in range(N)]
for i in range(1, N):
    inner_boxes[A[i]].append(i)

inner_count = [0] * N  # 箱iの中に入っている箱の数


def calc_inner(outer_num):
    for box_num in inner_boxes[outer_num]:
        inner_count[outer_num] += 1
        inner_count[outer_num] += calc_inner(box_num)
    return inner_count[outer_num]


calc_inner(0)


Q = int(input())
for _ in range(Q):
    v = int(input())
    print(inner_count[v])
