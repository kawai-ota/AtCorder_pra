la_map = lambda: map(int, input().split())
la_int = lambda: int(input())
la_lis = lambda: list(la_map())
import sys
sys.setrecursionlimit(1000000)
from collections import deque, defaultdict

n,m = la_map()
arrive = [[] for _ in range(n)]
for _ in range(m):
    a,b = la_map()
    arrive[a-1].append(b-1)
ans = n
for i in range(n):
    stack = deque()
    stack.append(i)
    visited = [False]*n
    while stack:
        nd = stack.pop()
        visited[nd] = True
        for next in arrive[nd]:
            if not visited[next]:
                visited[next] = True
                ans += 1
                stack.append(next)
print(ans)