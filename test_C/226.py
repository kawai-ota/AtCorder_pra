N=int(input())
cost=[0]
G=[[] for i in range(N+1)]
for i in range(1,N+1):
  A=list(map(int,input().split()))
  cost.append(A[0])
  for j in range(A[1]):
    ten=A[j+2]
    G[i].append(ten)
import sys
sys.setrecursionlimit(1200000)
def dfs(pos,G,visited):
  global ans
  ans+=cost[pos]
  visited[pos]=True
  for i in G[pos]:
    if visited[i]==False:
      dfs(i,G,visited)
ans=0
visited=[0 for i in range(N+1)]
dfs(N,G,visited)
print(ans)