import math
n = int(input())

for i in range(n,0,-1):
  sqrt_N = math.isqrt(i)
  if sqrt_N ** 2 == i:
    print(i)
    exit()