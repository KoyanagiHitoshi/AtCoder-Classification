class UnionFind():

    def __init__(self, n):
        self.par = [-1]*n
        self.rank = [0]*n

    def find(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.par[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


N, Q = map(int, input().split())
uf = UnionFind(N)
for _ in range(Q):
    P, A, B = map(int, input().split())
    if P == 0:
        uf.unite(A, B)
    if P == 1:
        print("Yes" if uf.find(A) == uf.find(B) else "No")
