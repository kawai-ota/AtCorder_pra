h,n = map(int,input().split())
a = list(map(int,input().split()))

num = 0

for i in a:
  num += i

if h <= num:
   print("Yes")
else:
   print("No")