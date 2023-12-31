class Node:
    def __init__(self,val=''):
        self.nex = None
        self.pre = None
        self.val = val

nil = Node()
nil.nex = nil
nil.pre = nil

def insert(node):
    node.pre = nil
    node.nex = nil.nex
    nil.nex.pre = node
    nil.nex = node

def append(node):
    node.pre = nil.pre
    node.nex = nil
    nil.pre.nex = node
    nil.pre = node

def pop_head():
    if nil.nex == nil:
        print('Error')
    else:
        head =nil.nex
        print(head.val)
        nil.nex.nex.pre = nil
        nil.nex = nil.nex.nex
        del head

def pop_tail():
    if nil.pre == nil:
        print('Error')
    else:
        prev = nil.pre
        print(prev.val)
        prev.pre.nex = nil
        nil.pre = prev.pre
        del prev

Q = int(input())
for _ in range(Q):
    query = input().split()
    if query[0] == '0':
        new_node = Node(query[1])
        insert(new_node)
    elif query[0] =='1':
        new_node = Node(query[1])
        append(new_node)
    elif query[0] == '2':
        pop_head()
    else:
        pop_tail()

