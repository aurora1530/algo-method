class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


Q = int(input())


root = None

for _ in range(Q):
    v = int(input())
    v_node = Node(v)
    if root is None:
        root = v_node
        continue

    target_v = root
    while True:
        if v_node.val <= target_v.val:
            if target_v.left is None:
                target_v.left = v_node
                break
            else:
                target_v = target_v.left
                continue
        elif v_node.val > target_v.val:
            if target_v.right is None:
                target_v.right = v_node
                break
            else:
                target_v = target_v.right
                continue

ans = []


def rec(v_node):
    ans.append(v_node.val)
    if v_node.left is not None:
        rec(v_node.left)
    if v_node.right is not None:
        rec(v_node.right)


rec(root)
print(*ans)
