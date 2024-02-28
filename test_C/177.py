n = int(input())
s = list(map(int,input().split()))
sums = sum(s)
ans = 0
for i in s:
  ans+=i*(sums-i)
print((ans//2)%(10**9+7))