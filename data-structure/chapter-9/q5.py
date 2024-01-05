class Node:
    def __init__(self, value: int):
        self.parent: Node = None
        self.left: Node = None
        self.right: Node = None
        self.value = value


root = Node(None)


def insert(new_node: Node):
    next_node = root
    while next_node:
        parent_node = next_node
        if new_node.value <= next_node.value:
            next_node = next_node.left
        else:
            next_node = next_node.right

    if new_node.value <= parent_node.value:
        parent_node.left = new_node
    else:
        parent_node.right = new_node
    new_node.parent = parent_node


def find(key_val: int) -> Node:
    next_node = root
    if next_node.value is None:
        return None
    while next_node:
        if key_val == next_node.value:
            return next_node
        if key_val < next_node.value:
            next_node = next_node.left
        else:
            next_node = next_node.right
    return None


def delete(target_val: int):
    target = find(target_val)
    if target is None:
        return 'Error'

    if target.left is None and target.right is None:
        parent_node = target.parent
        setattr(parent_node,
                'left' if parent_node.left == target else 'right',
                None)

    elif target.left is not None and target.right is not None:
        # 通りがけ順で次のnodeを探す
        # まず、一度右小頂点をみる.これはnot None.
        next_node = target.right
        # 左小頂点を進めるだけ進む
        while next_node:
            if next_node.left:
                next_node = next_node.left
            else:
                break

        delete(next_node.value)
        target.value = next_node.value
    # left is None or right is None
    else:
        parent_node = target.parent
        child_node = target.right if target.left is None else target.left

        # targetの子と親を繋げる
        if parent_node is not None:
            if parent_node.left == target:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        child_node.parent = parent_node
    return 'Complete'


Q = int(input())

for _ in range(Q):
    query, v = map(int, input().split())
    if query == 0:
        new_node = Node(v)
        if root.value is None:
            root = new_node
        else:
            insert(new_node)
    elif query == 1:
        print('Yes' if find(v) is not None else 'No')
    else:
        print(delete(v))
