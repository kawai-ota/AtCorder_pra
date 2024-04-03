n = int(input())

ans = 15
def keta(n):
  res = 0
  while n:
    n //= 10
    res += 1
  return res
  
i=1
while i*i <= n:
  if n%i == 0:
    ans = min(ans, keta(n//i))
  i += 1

print(ans)