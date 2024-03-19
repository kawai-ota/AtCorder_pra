import sys
import math
sx,sy,ex,ey,t,v=map(int,input().split())
for i in range(int(input())):
  xx,xy=map(int,input().split())
  if math.sqrt((xx-sx)**2+(xy-sy)**2)+math.sqrt((xx-ex)**2+(xy-ey)**2)<=t*v:
    print("YES")
    sys.exit()
print("NO")
