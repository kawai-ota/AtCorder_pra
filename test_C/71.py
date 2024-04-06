import sys
sys.setrecursionlimit(1000000)
input=lambda:sys.stdin.readline().strip()
write=lambda x:sys.stdout.write(str(x)+'\n')
from collections import deque,Counter,namedtuple
from math import inf,sqrt,gcd,ceil,floor,e,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
def solve():
    n=int(input())
    a=list(map(int,input().split()))
    c=Counter(a)
    c=list(c.items())
    ans=0;t=[]
    for k,v in c:
        if v>1:
            t.append(k)
            if v>=4:
                ans=max(ans,k*k)
    if not t:
        print(0)
        return
    t.sort()
    if len(t)>=2:
        ans=max(ans,t[-1]*t[-2])
    print(ans)
    return

test=1
for _ in range(test):
    solve()