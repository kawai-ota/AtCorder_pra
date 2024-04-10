N,K=map(int,input().split())
A=list(map(int,input().split()))
L=dict()
for i in A:
  L.setdefault(i,0)
  L[i]+=1
LIST=list(L.values())
lon=len(LIST)
LIST.sort()
if K<lon:
  print(sum(LIST[:lon-K]))
else:
  print(0)