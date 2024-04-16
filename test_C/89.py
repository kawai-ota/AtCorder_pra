import math
n = int(input())
m = a = r = c = h = 0
for i in range(n):
    s = str(input())
    if s[0] == "M":
        m += 1
    if s[0] == "A":
        a += 1
    if s[0] == "R":
        r += 1
    if s[0] == "C":
        c += 1
    if s[0] == "H":
        h += 1

def dX(x,y,z):
    a = math.comb(x,1)
    b = math.comb(y,1)
    c = math.comb(z,1)
    return a*b*c

ans = 0
ans += dX(m,a,r)
ans += dX(m,a,c)
ans += dX(m,a,h)
ans += dX(m,r,c)
ans += dX(m,r,h)
ans += dX(m,c,h)
ans += dX(a,r,c)
ans += dX(a,r,h)
ans += dX(a,c,h)
ans += dX(r,c,h)

print(ans)