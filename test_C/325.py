import sys
sys.setrecursionlimit(10**6)
from collections import deque
que=deque()
input = sys.stdin.readline
h,w = map(int,input().split())
s=[]
for _ in range(h):
    s.append(input()[:-1])
dx=[1,1,1,0,0,-1,-1,-1]
dy=[1,0,-1,1,-1,1,-1,0]
visited=[[False]*w for _ in range(h)]
ans=0
for i in range(h):
    for j in range(w):
        if s[i][j]=="." or visited[i][j]:
            continue
        else:       
            que.append([i,j])
            while len(que)>0:
                x,y=que.popleft()
                for k in range(8):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if 0<=nx<h and 0<=ny<w and s[nx][ny]=="#" and (not visited[nx][ny]):
                        visited[nx][ny]=True
                        que.append([nx,ny])
            ans +=1
print(ans)