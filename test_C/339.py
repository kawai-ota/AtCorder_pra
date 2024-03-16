x = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(x):
  ans = max(ans+a[i], 0)

print(ans)