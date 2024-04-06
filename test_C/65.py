from collections import defaultdict
import sys
from itertools import product,combinations_with_replacement
def error(*args, end="\n"): print(*args, end=end, file=sys.stderr)
sys.setrecursionlimit(10**6)

x=10**9+7
def s(t):
  a=1
  for i in range(1,t+1):
    a=(a*i)%x
  return a
n,m=map(int,input().split())
if abs(n-m)>1:
  print(0)
  exit()
if (n+m)%2==0:
  print((s(n)*s(m)*2)%x)
else:
  print((s(n)*s(m))%x)