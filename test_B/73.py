n = int(input())
ans = 0

for _ in range(n):
  l,r = map(int,input().split())
  if l == r:
    ans += 1
  else:
    ans += (r - l) + 1

print(ans)