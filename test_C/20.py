import sys
from collections import deque
from collections import defaultdict
from copy import deepcopy
from bisect import bisect_left, bisect_right, insort_left, insort_right
from heapq import heapify, heappop, heappush
from itertools import product, permutations, combinations, combinations_with_replacement
from functools import reduce
from math import gcd, sin, cos, tan, asin, acos, atan, degrees, radians, pi
 
def lcm(x,y):
  return x*y//gcd(x,y)
def ii():
    return int(input())
def si():
    return str(input())
def mi():
    return map(int,input().split())
def ms():
    return map(str,input().split())
def li():
    return list(map(int,input().split()))
def ls():
    return list(map(str,input().split()))
  
sys.setrecursionlimit(10**6)
INF = float('inf')
mod7 = 10**9+7
mod9 = 998244353

h,w,t=mi()
a=[]

for i in range(h):
  s=si()
  a.append(s)
  if "S" in s:
    start=[i,s.index('S')]
    sx,sy=i,s.index('S')
  if "G" in s:
    goal=[i,s.index('G')]
    gx,gy=i,s.index('G')

ue=int(t)
st=0

while ue-st>1:
  md=(ue+st)//2
  
  H=[[0]+start]
  dist=[[INF]*w for i in range(h)]
  dist[sx][sy]=0
  
  while H:
    cost,x,y=heappop(H)
    
    for xx,yy in [[1,0],[0,1],[0,-1],[-1,0]]:
      xx,yy=x+xx,y+yy
      if 0<=xx<h and 0<=yy<w:
        if a[xx][yy]=='#':
          tcost=cost+md
        else:
          tcost=cost+1
        
        if dist[xx][yy]>tcost:
          dist[xx][yy]=tcost
          heappush(H,[tcost,xx,yy])
  if dist[gx][gy]>t:
    ue=md
  else:
    st=md
    
print(st)