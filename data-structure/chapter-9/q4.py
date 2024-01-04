class Node:
    def __init__(self, value: int):
        self.left = None
        self.right = None
        self.value = value


root = Node(None)


def insert(v_node: Node):
    next = root
    parent = root
    while next:
        if v_node.value <= next.value:
            parent = next
            next = next.left
        elif v_node.value > next.value:
            parent = next
            next = next.right
    if v_node.value <= parent.value:
        parent.left = v_node
    elif v_node.value > parent.value:
        parent.right = v_node


def key_exists(key: int):
    if root.value is None:
        return False
    next = root
    while next:
        if next.value == key:
            return True
        if key <= next.value:
            next = next.left
        elif key > next.value:
            next = next.right
    return False


Q = int(input())

for _ in range(Q):
    query, y = map(int, input().split())
    if query == 0:
        if root.value is None:
            root.value = y
        else:
            new_node = Node(y)
            insert(new_node)
    else:
        ans = 'Yes' if key_exists(y) else 'No'
        print(ans)
