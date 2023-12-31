class Node:
    def __init__(self,val=''):
        self.nex = None
        self.val = val

nil = Node()
nil.nex = nil

def insert(node):
    node.nex = nil.nex
    nil.nex = node

def pop_head():
    if nil.nex == nil:
        print('Error')
    else:
        print(nil.nex.val)
        nil.nex = nil.nex.nex

Q = int(input())

for _ in range(Q):
    query = input().split()
    if query[0] == '0':
        new_node = Node(query[1])
        insert(new_node)
    else:
        pop_head()