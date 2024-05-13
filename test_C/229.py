n, w = [int(x) for x in input().split()]
ab = [[int(x) for x in input().split()] for _ in range(n)]
ab.sort()

rem = w
ans = 0

while len(ab) > 0 and rem > 0:
  ai, bi = ab.pop()
  use = min(rem, bi)
  ans += ai * use
  rem -= use
  
print(ans)