n=int(input())
k=list(map(int,input().split()))
for i in range(n):
  k[i]+=1
l=[0 for i in range(10**6)]
for i in range(n):
  l[k[i]]+=1
  l[k[i]+1]+=1
  l[k[i]-1]+=1
print(max(l))