from math import isqrt

a = []
n = int(input())
for i in range(1, isqrt(n)+1):
    if n % i == 0:
        if n // i == i:
            a.append(i)
        else:
            a.append(n//i)
            a.append(i)
a.sort()
for x in a:
    print(x)