class Train:
    def __init__(self,num):
        self.nex = None
        self.pre = None
        self.num = num
    def __str__(self):
        return str(self.num)


def connect(p,q):
    p.nex = q
    q.pre = p

def contract(r):
    if r.nex is None and r.pre is None:
        return
    if r.nex is None:
        r.pre.nex = None
    elif r.pre is None:
        r.nex.pre = None
    else:
        connect(r.pre,r.nex)
    r.nex =None
    r.pre = None
    return

N,Q = map(int,input().split())
trains = [Train(i) for i in range(N)]

for i in range(Q):
    query = input().split()
    if query[0] == '0':
        p,q = map(int,query[1:])
        connect(trains[p],trains[q])
    else:
        r = int(query[1])
        contract(trains[r])


def count_pre_train(train,count):
    if train.pre is None:
        return count
    count+=1
    if train.num != trains[0].num:
        return count_pre_train(train.pre,count)
    count= count_pre_train(train.pre,count)
    return count

def count_nex_train(train,count):
    if train.nex is None:
        return count
    count+=1
    if train.num != trains[0].num:
            return count_nex_train(train.nex,count)
    count=count_nex_train(train.nex,count)
    return count

count = 1
count += count_pre_train(trains[0],0)
count += count_nex_train(trains[0],0)

print(count)
