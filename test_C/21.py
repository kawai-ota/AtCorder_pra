from collections import deque
mod = 10**9 + 7
n = int(input())
a,b = map(int,input().split())

m = int(input())
G = [[] for i in range(n)]
for i in range(m):
    x,y = map(int,input().split())
    G[x-1].append(y-1)
    G[y-1].append(x-1)

depth = [0] * n
f = [True] * n
d = deque()
d.append(a-1)

while d:
    v = d.popleft()
    f[v] = False

    for v2 in G[v]:
        if f[v2]:
            depth[v2] = depth[v] + 1
            d.append(v2)
            f[v2] = False

p = [0] * n
p[a-1] = 1
l = []
for i in range(n):
    l.append([depth[i],i])

l.sort()

for i in range(1,n):
    dep = l[i][0]
    v = l[i][1]

    for v2 in G[v]:
        if depth[v2] == dep - 1:
            p[v] += p[v2]
            p[v] %= mod

print(p[b-1])

