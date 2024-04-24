import math
N, X = map(int, input().split())
x = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans = math.gcd(ans, abs(x[i] - X))
print(ans)