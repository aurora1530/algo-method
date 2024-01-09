class Node:
    def __init__(self, val) -> None:
        self.parent = None
        self.left = None
        self.right = None
        self.val = val


N = int(input())
A = list(map(int, input().split()))
is_heap = True
for i in range(1, N):
    parent_index = (i-1) // 2
    if A[parent_index] < A[i]:
        is_heap = False
        break


print('Yes' if is_heap else 'No')
