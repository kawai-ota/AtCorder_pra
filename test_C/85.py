import math
N,Y=map(int,input().split())
if Y>10000*N or Y<1000*N:
  print(-1,-1,-1)
else:
  a=0
  b=N
  c=0
  target=5000*N-Y
  while target!=0:
    if target>0:
      c+=math.ceil(abs(target)/4000)
      b-=math.ceil(abs(target)/4000)
      target-=4000*(math.ceil(abs(target)/4000))
    elif target<0:
      a+=math.ceil(abs(target)/5000)
      b-=math.ceil(abs(target)/5000)
      target+=5000*(math.ceil(abs(target)/5000))
  if a>=0 and b>=0 and c>=0:
    print(a,b,c)
  else:
    print(-1,-1,-1)
  