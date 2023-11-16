n = int(input())
a = list(map(int,input().split()))
ans = 0

for i in range(n):
   if a[i] > 10:
      while a[i] > 10:
        a[i] -= 1
        ans += 1

print(ans)