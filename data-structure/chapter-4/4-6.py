class Node:
    def __init__(self,num):
        self.nex = None
        self.pre = None
        self.num = num

N = int(input())
# N = 12
nodes = [Node(i+1) for i in range(N)]

for i in range(0,N):
    nodes[i].nex = nodes[i+1] if i != N-1 else nodes[0]
    nodes[i].pre = nodes[i-1] if i != 0 else nodes[N-1]

def contract(r):
    if r.nex is None and r.pre is None:
        return
    r.pre.nex = r.nex
    r.nex.pre = r.pre
    r.nex = None
    r.pre = None
    return

now_node = nodes[0]
while(now_node.nex.nex != now_node):
    # if now_node.nex is None:
    #     print(now_node.num)
    #     break
    next_node = now_node.nex.nex
    contract(now_node)
    now_node = next_node
print(now_node.nex.num)