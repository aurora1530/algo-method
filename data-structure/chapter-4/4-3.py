class Node:
    def __init__(self,val=''):
        self.nex =None
        self.back = None
        self.val = val

nil = Node()
nil.nex = nil
nil.back = nil

def insert(node):
    node.nex = nil.nex
    nil.nex.back = node
    nil.nex = node
    node.back = nil

def pop_tail():
    if nil.back == nil:
        print('Error')
    else:
        tail = nil.back
        print(tail.val)
        nil.back = tail.back
        tail.back.nex =nil
        del tail

Q = int(input())

for _ in range(Q):
    query = input().split()
    if query[0] == '0':
        new_node = Node(query[1])
        insert(new_node)
    else:
        pop_tail()