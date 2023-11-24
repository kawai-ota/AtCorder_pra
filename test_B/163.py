n,m = map(int,input().split())
a = list(map(int,input().split()))
num = sum(a)

if n > m:
   print(n - num)
elif n == num:
   print(0)
else:
   print(-1)