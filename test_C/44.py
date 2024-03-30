n,a=map(int,input().split())
q=[[0]*(n*a+1) for i in range(n+1)]
q[0][0]=1
for x in list(map(int,input().split())):
  nq=[[0]*(n*a+1) for i in range(n+1)]
  for i in range(n+1):
    for j in range(n*a+1):
      if q[i][j]>0:
        nq[i][j]+=q[i][j]
        if i+1<=n and j+x<=n*a:
          nq[i+1][j+x]+=q[i][j]
  q=nq
f=0
for i in range(1,n+1):
  f+=q[i][i*a]
print(f)