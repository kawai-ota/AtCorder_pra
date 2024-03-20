N,M=map(int,input().split())
wa=[0 for i in range(M+1)]
allwa=0
for i in range(N):
  l,r,s=map(int,input().split())
  wa[l-1]+=s
  wa[r]-=s
  allwa+=s
ans=0
for i in range(M):
  ans=max(ans,allwa-wa[i])
  wa[i+1]+=wa[i]
print(ans)