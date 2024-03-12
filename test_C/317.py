import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
ans = 0
used=[False]*(n+1)
cnc = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    cnc[a].append((b, c))
    cnc[b].append((a, c))

def dfs(now, s):
    global ans
    used[now] = True
    ans = max(ans, s)
    for to in cnc[now]:
        if  not used[to[0]]:
            dfs(to[0], s+to[1])
    used[now]=False        

for i in range(1, 1+n):
    dfs(i, 0)

print(ans)
