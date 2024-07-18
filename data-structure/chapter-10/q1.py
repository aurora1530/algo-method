class UnionFind:
    def __init__(self,n:int):
        self.parent = [-1] * n
        self.rank = [0] * n
        self.root = [-1] * n

