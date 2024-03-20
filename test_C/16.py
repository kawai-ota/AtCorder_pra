from collections import deque

N,M=map(int,input().split())
G=[]
for i in range(N):
    G.append([])
for i in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

for i in range(N):
    Q=deque()
    Q.append(i)
    dist=[-1]*N
    dist[i]=0
    while len(Q)>0:
        j=Q.popleft()
        for k in G[j]:
            if dist[k]==-1:
                dist[k]=dist[j]+1
                Q.append(k)
    cnt=dist.count(2)
    print(cnt)
    
