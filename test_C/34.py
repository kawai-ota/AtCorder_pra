from math import comb
H,W = map(int,input().split())
a = H-1
b = W-1
c = min(a,b)
d = 10**9+7
ans = comb(a+b, c)
ans %= d
print(ans)