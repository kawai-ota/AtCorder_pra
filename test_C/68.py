n, m = map(int, input().split())

g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

flag = False

for i in range(1, len(g)-1):
    if 0 in g[i] and n-1 in g[i]:
        flag = True
        break
else:
    flag = False

print("POSSIBLE" if flag else "IMPOSSIBLE")
