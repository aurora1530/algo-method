class Node:
    def __ini__(self,val):
      self.nex = None
      self.val = val

nil = Node()
nil.nex = nil

def insert(node):
  node.nex = nil.nex
  nil.nex = node

Q = int(input())

for _ in range(Q):
    query = input().split()
    if query[0] == '0':
        new_node = Node()
        new_node.val = query[1]
        insert(new_node)
    else:
        k = int(query[1])
        list_str = []
        next = nil.nex
        for i in range(k):
            if next == nil:
                break
            list_str.append(next.val)
            next = next.nex
        print(' '.join(list_str))