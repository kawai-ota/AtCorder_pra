N=int(input())

for i in range(int(N**(1/3))+1,0,-1):
  A=i**3
  B=A
  L=[]
  while A!=0:
    r=A%10
    L+=[r]
    A=A//10

  l=len(L)
  
  p=0
  for i in range(l//2):
    q=-i-1
    if L[i]!=L[q]:
      p=1
  if p==0 and B<=N:
    print(B)
    break
