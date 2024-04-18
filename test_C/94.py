import math
import functools

al = "abcdefghijklmnopqrstuvwxyz"
au = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ii():
    return int(input())

def gl():
    return list(map(int, input().split()))

def gs():
    return list(input().split())

def glm(h,w):
    a = []
    for i in range(h):
        a.append(gl())
    return a

def gsm(h,w):
    a = []
    for i in range(h):
        a.append(input())
    return a

def kiriage(n, r):
    if n % r == 0:
        return n // r
    else:
        return (n // r) + 1

def yaku(n):
    ans = []
    for i in range(1, n+1):
        if n % i == 0:
            ans.append(i)
    return ans

def ketawa(n):
    ans = 0
    s = str(n)
    for i in s:
        ans += int(i)
    return ans

def rev(a):
    na = a[:]
    return list(reversed(a))

def lcm2(x, y):
    return (x * y) // math.gcd(x, y)

def lcm3(*ints):
    return functools.reduce(lcm2, ints)

def gcd3(*ints):
    return functools.reduce(math.gcd, ints)

ans = 10**10
cnt=0
ay="Yes"
an="No"

n = ii()
x = gl()
y = list(sorted(x))
med = y[n // 2 - 1]
for i in range(n):
    if x[i] <= med:
      print(y[n // 2])
    else:
        print(y[n // 2 - 1])

