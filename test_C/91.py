n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
cd=[list(map(int,input().split())) for _ in range(n)]
ab.sort()
cd.sort()

res=0
for i in range(n):
  x=-1
  x_idx=0
  for j in range(len(ab)):
    a,b=ab[j]
    c,d=cd[i]
    if a<c and b<d and x<b:
      x=b
      x_idx=j

  if x!=-1:
    res+=1
    ab.pop(x_idx)
print(res)
