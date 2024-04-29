import sys,math
from collections import defaultdict
sys.setrecursionlimit(500005)
mod=998244353
mod2=10**9+7
inf=1e20
def gyakugen(n,m):
    return (n*pow(m,mod-2,mod))%mod
n=int(input())
a=list(map(int,input().split()))
ans=a[0]
for i in a:
    ans=math.gcd(ans,i)
print(ans)
