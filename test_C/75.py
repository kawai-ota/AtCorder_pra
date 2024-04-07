N, M = map(int, input().split())
P = []
for i in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  P.append([a, b])

class UnionFind():
  def __init__(self, n=N):
    self.n = n
    self.par = list(range(N))
    self.rank = [1]*n
    
  def root(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.root(self.par[x])
      return self.par[x]
  
  def same(self, x, y):
    return self.root(x) == self.root(y)
  
  def unite(self, x, y):
    x = self.root(x)
    y = self.root(y)
    if x == y:
      return
    
    if self.rank[x] < self.rank[y]:
      y, x = x, y
    
    self.par[y] = x
    if self.rank[x] == self.rank[y]:
      self.rank[x] += 1
  
  def showRank(self, x):
    self.rank[x] = self.rank[self.root(x)]
    return self.rank[x]

ans = 0
for i in range(M):
  uf = UnionFind()
  for j in range(M):
    if i != j:
      pa, pb = P[j]
      uf.unite(pa, pb)
  b = 0
  for j in range(N):
    if uf.par[j] == j:
      b += 1
    if b > 1:
      ans += 1
      break
print(ans)