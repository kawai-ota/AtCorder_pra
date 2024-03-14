import math

d = int(input())
ans = float("INF")
for x in range(int(d**0.5) + 1):
    y = math.sqrt(d - x**2)
    y1 = int(y)
    y2 = y1 + 1
    ans = min(ans, abs(x**2 + y1**2 - d))
    ans = min(ans, abs(x**2 + y2**2 - d))

print(ans)
