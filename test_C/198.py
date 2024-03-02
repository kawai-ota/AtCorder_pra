from math import *
R, X, Y = map(int, input().split())
d = sqrt(X ** 2 + Y ** 2)
p = d / R
if p - int(p) > 0:
    q = int(p) + 1
    if q == 1:
        q = 2
else:
    q = int(p)
print(q)
