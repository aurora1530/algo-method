class UnionFind:
    def __init__(self, n: int):
        self.parent = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def root(self, x: int):
        if self.parent[x] == -1:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def is_same(self, x: int, y: int):
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int):
        root_x = self.root(x)
        root_y = self.root(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        self.siz[root_x] += self.siz[root_y]

        return True

    def size(self, x):
        return self.siz[self.root(x)]


N, M = map(int, input().split())

uf = UnionFind(N)

for _ in range(M):
    a, b = map(int, input().split())
    is_same_group = uf.is_same(a, b)
    if is_same_group:
        print('Yes')
    else:
        print('No')
        uf.unite(a, b)
